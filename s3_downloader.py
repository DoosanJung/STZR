import os
import boto
from boto.exception import S3ResponseError
from datetime import date, timedelta
#import glob
import gzip
import pandas as pd

def get_dates(start_year, start_month, start_day, end_year, end_month, end_day):
    '''
    INPUT: start_year, start_month, start_day, end_year, end_month, end_day
    OUTPUT: dates list (will be used to fetch data from s3)
    '''
    d1 = date(start_year, start_month, start_day)  # start date
    d2 = date(end_year, end_month, end_day)  # end date
    delta = d2 - d1  # timedelta
    dates = []
    for i in range(delta.days + 1):
        dates.append( "".join(str(d1 + timedelta(days=i)).split('-')) ) # strip('-') not working
    return dates

def str_to_int_ftn(df, column_name):
    '''
    INPUT: Pandas DataFrame, string
    OUTPUT: Pandas DataFrame
    '''
    df[column_name] = df[column_name].fillna(0).astype(int)

def get_tid_lst_frm_uid(uid_grouped_rmv_tid_Uns, uid):
    '''
    INPUT: Pandas DataFrame, groupby a uid
    OUTPUT: list, tids of a uid
    '''
    uid_tid_lst = []
    for tid in uid_grouped_rmv_tid_Uns.get_group(uid)['tid']:
        if tid not in uid_tid_lst:
            uid_tid_lst.append(tid)
    return uid_tid_lst

def get_sum_df(uid_grouped_rmv_tid_Uns,uid):
    '''
    INPUT: Pandas DataFrame, groupby uid
    OUTPUT: Pandas DataFrame, counted and summed by uid, tid
    '''
    uid_tid_grouped_rmv_tid_Uns = uid_grouped_rmv_tid_Uns.get_group(uid).groupby('tid')
    uid_tid_lst = get_tid_lst_frm_uid(uid_grouped_rmv_tid_Uns, uid)
    sum_lst=[]
    for tid in uid_tid_lst:
        tid_dict={}
        tid_dict['uid'] = uid
        tid_dict['tid'] = tid
        tid_dict['tBuf_sum'] = uid_tid_grouped_rmv_tid_Uns.get_group(tid)['tBuf'].sum()
        tid_dict['tIBuf_sum'] = uid_tid_grouped_rmv_tid_Uns.get_group(tid)['tIBuf'].sum()
        tid_dict['tLBuf_sum'] = uid_tid_grouped_rmv_tid_Uns.get_group(tid)['tLBuf'].sum()
        tid_dict['tPld_sum'] = uid_tid_grouped_rmv_tid_Uns.get_group(tid)['tPld'].sum()
        tid_dict['tVH'] = uid_tid_grouped_rmv_tid_Uns.get_group(tid)['tVH'].sum()
        # Unzip the dictionary
        for key in uid_tid_grouped_rmv_tid_Uns.get_group(tid)['type'].value_counts().to_dict().keys():
            tid_dict['#type_'+ key] = uid_tid_grouped_rmv_tid_Uns.get_group(tid)['type'].value_counts().to_dict()[key]
        # Unzip the dictionary
        for key in uid_tid_grouped_rmv_tid_Uns.get_group(tid)['mplyevnt'].value_counts().to_dict().keys():
            tid_dict['#mplyevnt_'+key] = uid_tid_grouped_rmv_tid_Uns.get_group(tid)['mplyevnt'].value_counts().to_dict()[key]
        sum_lst.append(tid_dict)
    return pd.DataFrame(sum_lst)

def gzip_to_csv(s3_path):
    '''
    INPUT: gzip file; raw data
    OUTPUT: csv file
    '''
    with gzip.open(s3_path,'rb') as f:
        df = pd.read_json(f.read(),lines=True)
        df = df[df['ckey']==CKEY]
        # drop ts column
        if 'ts' in df.columns:
            df = df.drop('ts',axis=1)
        # Convert string into int
        str_to_int_lst = ['tPld','tIBuf','tBuf','tLBuf','tVH','drt']
        for column_name in str_to_int_lst:
            str_to_int_ftn(df,column_name)
        # Keep only those columns
        tmp_df = df[['ts2','eps','drt','mplyevnt','spos','ssid',\
                'szrid','tBuf','tIBuf','tLBuf','tPld','tVH','tid','type','uid']]
                ## 'errmsg' deleted for 20170504 ~
        # remove tid == Unset
        tmp_df_rmv_tid_Uns = tmp_df[tmp_df['tid']!='Unset']
        # Groupby uid
        uid_grouped_rmv_tid_Uns = tmp_df_rmv_tid_Uns.groupby('uid')
        uid_lst = uid_grouped_rmv_tid_Uns.groups.keys()
        # group by tid
        Frame = []
        for uid in uid_lst:
            Frame.append(get_sum_df(uid_grouped_rmv_tid_Uns,uid))
        sum_df = pd.concat(Frame).fillna(0)
        # Save to csv
        csv_name = "".join(s3_path[s3_path.find('dd'):])+'.csv'
        sum_df.to_csv(str(DOWNLOAD_LOCATION_PATH + csv_name),index=False)

def get_files_from_s3(start_year, start_month, start_day, end_year, end_month, end_day):
    '''
    INPUT: Start date, End date
    OUTPUT: csv file
    '''
    # connect
    bucket_name = 'szrachiever'
    access_key = os.environ['AWS_ACCESS_KEY']
    secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    conn = boto.connect_s3(access_key, secret_access_key)
    my_bucket = conn.get_bucket(bucket_name)

    # downloading period
    dates = get_dates(start_year, start_month, start_day, end_year, end_month, end_day)

    for date in dates:
        bucket_entries = my_bucket.list(prefix = 'Streamlyzer/dd=' + date)
        for entry in bucket_entries:
            key_string = str(entry.key).replace('/','_')
            s3_path = DOWNLOAD_LOCATION_PATH + key_string
            try:
                print "Current File is : ", s3_path
                entry.get_contents_to_filename(s3_path)
                gzip_to_csv(s3_path)

                # remove raw data files ('s3_path')
                os.remove(s3_path)

                # TODO: Merge csv files into a csv file using concatenate_csv func.
                # if next file has same uid and tid, just sum it up!
                # NOT_TODO: merge multiple gz files into one datafile

                # TODO: remove all other csv files

            except (OSError,S3ResponseError) as e:
                pass
    			# check if the file has been downloaded locally
                if not os.path.exists(s3_path):
                    try:
                        os.makedirs(s3_path)
                        print 'makedir'
                    except OSError as exc:
    					# let guard againts race conditions
                        import errno
                        if exc.errno != errno.EEXIST:
                            raise


def concatenate_csv():
    '''
    INPUT: multiple csvs
    OUTPUT: a csv file having sum up value for same uid,tid data;
            while merging, sum up the values for same uid,tid data
    '''



if __name__=="__main__":
    # Specify DOWNLOAD_LOCATION_PATH
    DOWNLOAD_LOCATION_PATH = os.path.expanduser('~')+'/Downloads/local_szrachiever/'
    if not os.path.exists(DOWNLOAD_LOCATION_PATH):
        print ("Making download directory")
        os.mkdir(DOWNLOAD_LOCATION_PATH)

    # Specify CKEY
    CKEY = '17943e6c6eec49cdb6'

    # run the function
    get_files_from_s3(2017,05,04,2017,06,30)
