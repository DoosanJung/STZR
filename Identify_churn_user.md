
### Import modules and DataFrame


    import pandas as pd
    import pickle
    import numpy


    dfs = pickle.load(open('dfs_2000_0401_0630.p','rb'))


    dfs.head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>abtm</th>
      <th>br</th>
      <th>brn</th>
      <th>brv</th>
      <th>chn</th>
      <th>ckey</th>
      <th>co</th>
      <th>coiso</th>
      <th>ct</th>
      <th>devm</th>
      <th>...</th>
      <th>tPld</th>
      <th>tVH</th>
      <th>tid</th>
      <th>ts</th>
      <th>ts2</th>
      <th>type</th>
      <th>uid</th>
      <th>utype</th>
      <th>v</th>
      <th>yob</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Release</td>
      <td>3614101</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>Canada</td>
      <td>CA</td>
      <td>Coquitlam</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>49377</td>
      <td>59880</td>
      <td>4e7475b2-0b88-461f-9387-0a9b77251df8</td>
      <td>1491004567535</td>
      <td>2017-03-31T23:56:07.535Z</td>
      <td>vh</td>
      <td>WUCH155103440</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Release</td>
      <td>3328416</td>
      <td>KOOLi_Player</td>
      <td>2.0.6</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Los Angeles</td>
      <td>h3</td>
      <td>...</td>
      <td>72154</td>
      <td>36047</td>
      <td>7e588404-453f-4a45-a8aa-05b6b0ae5be4</td>
      <td>1491004632602</td>
      <td>2017-03-31T23:57:12.602Z</td>
      <td>lBuf</td>
      <td>14110963601665</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Release</td>
      <td>3587620</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Laguna Woods</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>69839</td>
      <td>12022</td>
      <td>f19a8414-64cd-418a-985e-61ae073d8915</td>
      <td>1491004617448</td>
      <td>2017-03-31T23:56:57.448Z</td>
      <td>lBuf</td>
      <td>WUCH155102826</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Release</td>
      <td>1373174</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>West Springfield</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>73567</td>
      <td>39988</td>
      <td>7efccc8b-436d-40bf-8bd5-fe45d08039ca</td>
      <td>1491004547792</td>
      <td>2017-03-31T23:55:47.792Z</td>
      <td>mplyevent</td>
      <td>WUCH161600388</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Release</td>
      <td>1322244</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Medfield</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>70656</td>
      <td>16127</td>
      <td>14bd5375-4a03-460c-b0aa-d73fe16628b7</td>
      <td>1491004467751</td>
      <td>2017-03-31T23:54:27.751Z</td>
      <td>vh</td>
      <td>WUCH155101681</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 54 columns</p>
</div>




    #dfs.info()
    dfs.shape




    (182000, 54)



### Here's what needs to be done..
    1. Identify each user's last activity
    2. If the last activity falls in recent 30 days, then the user = not churned
    3. Otherwise(i.e. the last activity is earlier than 30 days), the user has churned
    
    #=> Which means that I need to deal with date..

### 'ts' and 'ts2' for date


    from datetime import datetime, timedelta


    # (optional)
    # Pandas Series works too..
    # before we convert 'ts2' column type from string to datetime
    print dfs['ts2'][:1]; print type(dfs['ts2'][:1]) 
    print '\n'
    
    print 'extract the value only: ',dfs['ts2'][:1].values[0]
    a_not_used = datetime.strptime(dfs['ts2'][:1].values[0],'%Y-%m-%dT%H:%M:%S.%fZ')
    print '\n'
    print a_not_used ; print type(a_not_used)

    0    2017-03-31T23:56:07.535Z
    Name: ts2, dtype: object
    <class 'pandas.core.series.Series'>
    
    
    extract the value only:  2017-03-31T23:56:07.535Z
    
    
    2017-03-31 23:56:07.535000
    <type 'datetime.datetime'>



    # But we use this..
    # First row
    print type(dfs.ix[0,:]['ts2'])

    <type 'unicode'>



    a = datetime.strptime(dfs.ix[0,:]['ts2'],'%Y-%m-%dT%H:%M:%S.%fZ')
    print a; print type(a)
    # same as using Pandas Series, except it's shorter..

    2017-03-31 23:56:07.535000
    <type 'datetime.datetime'>



    a.microsecond




    535000




    a.date()




    datetime.date(2017, 3, 31)




    a.time()




    datetime.time(23, 56, 7, 535000)




    a_str = datetime.strptime(dfs.ix[0,:]['ts2'],'%Y-%m-%dT%H:%M:%S.%fZ').strftime('%s')
    print a_str
    a_in_ms = a_str + str(a.microsecond/1000)
    print 'time in milliseconds in ts2: ', a_in_ms
    print 'time in milliseconds in ts : ', dfs.ix[0,:]['ts']

    1491029767
    time in milliseconds in ts2:  1491029767535
    time in milliseconds in ts :  1491004567535


    Wait.. What's up with that? Possibly the timezone issue?


    import pytz


    def utc_to_each_tz(utc_dt, region):
        import pytz
        local_tz = pytz.timezone(region)
        local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
        return local_tz.normalize(local_dt)


    ## First row comes from 'Coquitlam, Canada' (same timezone with LA)
    a_in_ms_tz = utc_to_each_tz(a,'America/Los_Angeles').strftime('%s')  + str(a.microsecond/1000)
    print 'time in milliseconds in ts2 (tz adjusted): ', a_in_ms_tz
    print 'time in milliseconds in ts               : ', dfs.ix[0,:]['ts']
    print 'Are they same? ',a_in_ms_tz == dfs.ix[0,:]['ts']
    # 

    time in milliseconds in ts2 (tz adjusted):  1491004567535
    time in milliseconds in ts               :  1491004567535
    Are they same?  True


    Ahh.. It was timezone issue 
    ts is in UTC
    We'll get rid of 'ts' anyway...


    dfs.shape




    (182000, 54)




    # Dropping the column 'ts'
    if 'ts' in dfs.columns:
        dfs = dfs.drop('ts',axis=1)


    dfs.shape




    (182000, 53)




    print dfs.ix[0,:]['ts2']
    print type(dfs.ix[0,:]['ts2'])
    # it's string..

    2017-03-31T23:56:07.535Z
    <type 'unicode'>


### A special object will be easier for me to handle..


    # Convert 'ts2' column type from string to datetime
    if isinstance(dfs.ix[0,:]['ts2'], unicode):
        dfs['ts2'] = pd.to_datetime(dfs['ts2'])


    # Converted into datetime object
    print dfs.ix[0,:]['ts2']
    print type(dfs.ix[0,:]['ts2'])

    2017-03-31 23:56:07.535000
    <class 'pandas.tslib.Timestamp'>


### Also, we'll match the date type


    dfs.info()

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 182000 entries, 0 to 181999
    Data columns (total 53 columns):
    abtm        182000 non-null object
    br          167826 non-null object
    brn         140477 non-null object
    brv         140477 non-null object
    chn         182000 non-null object
    ckey        182000 non-null object
    co          182000 non-null object
    coiso       182000 non-null object
    ct          182000 non-null object
    devm        140477 non-null object
    devv        140477 non-null object
    drt         56448 non-null object
    eps         182000 non-null object
    errmsg      2262 non-null object
    gen         173329 non-null object
    img         9289 non-null object
    isp         182000 non-null object
    lang        182000 non-null object
    live        182000 non-null object
    lrg         182000 non-null object
    mplyevnt    41523 non-null object
    mpv         182000 non-null object
    mvcp        182000 non-null object
    mvctg       182000 non-null object
    mvid        182000 non-null object
    mvrt        182000 non-null object
    mvsctg      182000 non-null object
    osn         140477 non-null object
    osv         140477 non-null object
    pltn        182000 non-null object
    ppv         182000 non-null object
    res         167826 non-null object
    rg          182000 non-null object
    rgiso       182000 non-null object
    sid         182000 non-null object
    spos        167826 non-null object
    srn         182000 non-null object
    ssid        182000 non-null object
    stype       182000 non-null object
    svr         182000 non-null object
    szrid       182000 non-null object
    tBuf        8684 non-null object
    tIBuf       2579 non-null object
    tLBuf       61171 non-null float64
    tPld        2924 non-null object
    tVH         56448 non-null object
    tid         182000 non-null object
    ts2         182000 non-null datetime64[ns]
    type        182000 non-null object
    uid         182000 non-null object
    utype       182000 non-null object
    v           182000 non-null object
    yob         173329 non-null object
    dtypes: datetime64[ns](1), float64(1), object(51)
    memory usage: 75.0+ MB



    # Convert string into int
    
    print dfs.ix[0,:]['tPld'] # player loading time
    print type(dfs.ix[0,:]['tPld'])
    print ''
    print dfs.ix[0,:]['tIBuf'] # Initial Buffering time
    print type(dfs.ix[0,:]['tIBuf'])
    print ''
    print dfs.ix[0,:]['tBuf'] # Re-buffering time
    print type(dfs.ix[0,:]['tBuf'])
    print ''
    print dfs.ix[0,:]['tLBuf'] # Long buffering time
    print type(dfs.ix[0,:]['tLBuf'])
    print ''
    print dfs.ix[0,:]['tVH'] # Viewing Time (in a minute)
    print type(dfs.ix[0,:]['tVH'])
    
    
    # what to convert
    str_to_int_lst = ['tPld','tIBuf','tBuf','tLBuf','tVH']

    49377
    <type 'unicode'>
    
    6
    <type 'unicode'>
    
    821
    <type 'unicode'>
    
    5003.0
    <type 'numpy.float64'>
    
    59880
    <type 'unicode'>



    def str_to_int_ftn(column_name):
        dfs[column_name] = dfs[column_name].fillna(0).astype(int)


    for column_name in str_to_int_lst:
        str_to_int_ftn(column_name)


    dfs.info()

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 182000 entries, 0 to 181999
    Data columns (total 53 columns):
    abtm        182000 non-null object
    br          167826 non-null object
    brn         140477 non-null object
    brv         140477 non-null object
    chn         182000 non-null object
    ckey        182000 non-null object
    co          182000 non-null object
    coiso       182000 non-null object
    ct          182000 non-null object
    devm        140477 non-null object
    devv        140477 non-null object
    drt         56448 non-null object
    eps         182000 non-null object
    errmsg      2262 non-null object
    gen         173329 non-null object
    img         9289 non-null object
    isp         182000 non-null object
    lang        182000 non-null object
    live        182000 non-null object
    lrg         182000 non-null object
    mplyevnt    41523 non-null object
    mpv         182000 non-null object
    mvcp        182000 non-null object
    mvctg       182000 non-null object
    mvid        182000 non-null object
    mvrt        182000 non-null object
    mvsctg      182000 non-null object
    osn         140477 non-null object
    osv         140477 non-null object
    pltn        182000 non-null object
    ppv         182000 non-null object
    res         167826 non-null object
    rg          182000 non-null object
    rgiso       182000 non-null object
    sid         182000 non-null object
    spos        167826 non-null object
    srn         182000 non-null object
    ssid        182000 non-null object
    stype       182000 non-null object
    svr         182000 non-null object
    szrid       182000 non-null object
    tBuf        182000 non-null int64
    tIBuf       182000 non-null int64
    tLBuf       182000 non-null int64
    tPld        182000 non-null int64
    tVH         182000 non-null int64
    tid         182000 non-null object
    ts2         182000 non-null datetime64[ns]
    type        182000 non-null object
    uid         182000 non-null object
    utype       182000 non-null object
    v           182000 non-null object
    yob         173329 non-null object
    dtypes: datetime64[ns](1), int64(5), object(47)
    memory usage: 75.0+ MB


### Identify each user's last activity


    print 'The number of unique users:',len(dfs['uid'].unique())
    print type(dfs['uid'].unique())
    unique_uid = dfs['uid'].unique()

    The number of unique users: 4197
    <type 'numpy.ndarray'>



    ##unique uid looks like..
    unique_uid[:10]




    array([u'WUCH155103440', u'14110963601665', u'WUCH155102826',
           u'WUCH161600388', u'WUCH155101681', u'WUCH155102162',
           u'WUCH155101131', u'WUCH155101270', u'WUCH155102245',
           u'WUCH155102068'], dtype=object)




    # to get the last activity for unique users
    dfs_last = dfs.groupby('uid').last()
    print dfs_last.shape

    (4197, 52)



    # This DataFrame shows the last activity of each unique user'
    dfs_last.head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>abtm</th>
      <th>br</th>
      <th>brn</th>
      <th>brv</th>
      <th>chn</th>
      <th>ckey</th>
      <th>co</th>
      <th>coiso</th>
      <th>ct</th>
      <th>devm</th>
      <th>...</th>
      <th>tIBuf</th>
      <th>tLBuf</th>
      <th>tPld</th>
      <th>tVH</th>
      <th>tid</th>
      <th>ts2</th>
      <th>type</th>
      <th>utype</th>
      <th>v</th>
      <th>yob</th>
    </tr>
    <tr>
      <th>uid</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13110946900174</th>
      <td>Release</td>
      <td>3425963</td>
      <td>KOOLi_Player</td>
      <td>1.0.11</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Santa Ana</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>5004</td>
      <td>0</td>
      <td>23978</td>
      <td>0ceeb774-b2ff-4fae-a8e4-e26b09862c98</td>
      <td>2017-06-25 23:53:40.532</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>14110954700477</th>
      <td>Release</td>
      <td>5473981</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>China</td>
      <td>CN</td>
      <td>Guangzhou</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7601f004-5675-4369-8403-7bcc26574bd2</td>
      <td>2017-06-05 23:51:55.457</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>14110962300001</th>
      <td>Release</td>
      <td>3577044</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Teaneck</td>
      <td>h3</td>
      <td>...</td>
      <td>0</td>
      <td>5003</td>
      <td>0</td>
      <td>59858</td>
      <td>aa8c169e-ca28-4463-b7eb-6f3a92ab85d4</td>
      <td>2017-06-11 23:49:44.582</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>14110962300002</th>
      <td>Release</td>
      <td>3428368</td>
      <td>KOOLi_Player</td>
      <td>1.0.11</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Fort Lee</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>384d9f1f-e366-4ba0-adbd-1ae5c3c2a267</td>
      <td>2017-06-27 23:57:21.619</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>14110962300003</th>
      <td>Release</td>
      <td>3530742</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Fort Lee</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>5003</td>
      <td>0</td>
      <td>0</td>
      <td>611de4d6-8403-4e2d-a0f4-8986773a5350</td>
      <td>2017-04-28 23:46:52.640</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 52 columns</p>
</div>




    # The number of rows in dfs_last eqauls to the number of unique users
    dfs_last.shape[0] == len(unique_uid)




    True




    # (Optional)
    # to get the first activity for unique users
    dfs_first = dfs.groupby('uid').first()
    print dfs_first.shape

    (4197, 52)



    # (Optional)
    dfs_first.head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>abtm</th>
      <th>br</th>
      <th>brn</th>
      <th>brv</th>
      <th>chn</th>
      <th>ckey</th>
      <th>co</th>
      <th>coiso</th>
      <th>ct</th>
      <th>devm</th>
      <th>...</th>
      <th>tIBuf</th>
      <th>tLBuf</th>
      <th>tPld</th>
      <th>tVH</th>
      <th>tid</th>
      <th>ts2</th>
      <th>type</th>
      <th>utype</th>
      <th>v</th>
      <th>yob</th>
    </tr>
    <tr>
      <th>uid</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13110946900174</th>
      <td>Release</td>
      <td>3649390</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Irvine</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>60002</td>
      <td>4695ba6e-5e33-49ce-9210-4977385df779</td>
      <td>2017-04-02 23:56:54.163</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>14110954700477</th>
      <td>Release</td>
      <td>899884</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>China</td>
      <td>CN</td>
      <td>Guangzhou</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>5004</td>
      <td>0</td>
      <td>7956</td>
      <td>7601f004-5675-4369-8403-7bcc26574bd2</td>
      <td>2017-06-05 23:51:16.066</td>
      <td>upImg</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>14110962300001</th>
      <td>Release</td>
      <td>3464687</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Teaneck</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>e2272e69-00dc-459d-9d67-31c50b4d6454</td>
      <td>2017-04-06 23:56:43.105</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>14110962300002</th>
      <td>Release</td>
      <td>5510220</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Fort Lee</td>
      <td>h3</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>adb4c1dd-5817-4df8-97ef-7789624e0bdc</td>
      <td>2012-03-29 07:36:03.186</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>14110962300003</th>
      <td>Release</td>
      <td>3453604</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Fort Lee</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>5005</td>
      <td>0</td>
      <td>0</td>
      <td>73ce457f-45a3-4f0e-808b-bf61e174456e</td>
      <td>2017-04-15 23:47:47.132</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 52 columns</p>
</div>




    # (Optional)
    # Sanity check
    dfs_first['ts2'] <= dfs_last['ts2']




    uid
    13110946900174    True
    14110954700477    True
    14110962300001    True
    14110962300002    True
    14110962300003    True
    14110962300004    True
    14110962300005    True
    14110962300006    True
    14110962300007    True
    14110962300008    True
    14110962300010    True
    14110962300011    True
    14110962300012    True
    14110962300013    True
    14110962300014    True
    14110962300015    True
    14110962300017    True
    14110962300018    True
    14110962300019    True
    14110962300020    True
    14110962300021    True
    14110962300022    True
    14110962300023    True
    14110962300025    True
    14110962300026    True
    14110962300027    True
    14110962300028    True
    14110962300029    True
    14110962300030    True
    14110962300031    True
                      ... 
    WUCH161600453     True
    WUCH161600454     True
    WUCH161600455     True
    WUCH161600456     True
    WUCH161600457     True
    WUCH161600458     True
    WUCH161600459     True
    WUCH161600460     True
    WUCH161600463     True
    WUCH161600464     True
    WUCH161600465     True
    WUCH161600466     True
    WUCH161600467     True
    WUCH161600469     True
    WUCH161600470     True
    WUCH161600473     True
    WUCH161600475     True
    WUCH161600477     True
    WUCH161600480     True
    WUCH161600481     True
    WUCH161600482     True
    WUCH161600486     True
    WUCH161600487     True
    WUCH161600490     True
    WUCH161600491     True
    WUCH161600492     True
    WUCH161600493     True
    WUCH161600496     True
    WUCH161600499     True
    WUCH161600500     True
    Name: ts2, dtype: bool



### See If the last activity falls in recent 30 days or not


    dfs_last.head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>abtm</th>
      <th>br</th>
      <th>brn</th>
      <th>brv</th>
      <th>chn</th>
      <th>ckey</th>
      <th>co</th>
      <th>coiso</th>
      <th>ct</th>
      <th>devm</th>
      <th>...</th>
      <th>tIBuf</th>
      <th>tLBuf</th>
      <th>tPld</th>
      <th>tVH</th>
      <th>tid</th>
      <th>ts2</th>
      <th>type</th>
      <th>utype</th>
      <th>v</th>
      <th>yob</th>
    </tr>
    <tr>
      <th>uid</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13110946900174</th>
      <td>Release</td>
      <td>3425963</td>
      <td>KOOLi_Player</td>
      <td>1.0.11</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Santa Ana</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>5004</td>
      <td>0</td>
      <td>23978</td>
      <td>0ceeb774-b2ff-4fae-a8e4-e26b09862c98</td>
      <td>2017-06-25 23:53:40.532</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>14110954700477</th>
      <td>Release</td>
      <td>5473981</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>China</td>
      <td>CN</td>
      <td>Guangzhou</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7601f004-5675-4369-8403-7bcc26574bd2</td>
      <td>2017-06-05 23:51:55.457</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>14110962300001</th>
      <td>Release</td>
      <td>3577044</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Teaneck</td>
      <td>h3</td>
      <td>...</td>
      <td>0</td>
      <td>5003</td>
      <td>0</td>
      <td>59858</td>
      <td>aa8c169e-ca28-4463-b7eb-6f3a92ab85d4</td>
      <td>2017-06-11 23:49:44.582</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>14110962300002</th>
      <td>Release</td>
      <td>3428368</td>
      <td>KOOLi_Player</td>
      <td>1.0.11</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Fort Lee</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>384d9f1f-e366-4ba0-adbd-1ae5c3c2a267</td>
      <td>2017-06-27 23:57:21.619</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
    <tr>
      <th>14110962300003</th>
      <td>Release</td>
      <td>3530742</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Fort Lee</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>5003</td>
      <td>0</td>
      <td>0</td>
      <td>611de4d6-8403-4e2d-a0f4-8986773a5350</td>
      <td>2017-04-28 23:46:52.640</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 52 columns</p>
</div>




    dfs_last['ts2'] <= '2017-05-31'




    uid
    13110946900174    False
    14110954700477    False
    14110962300001    False
    14110962300002    False
    14110962300003     True
    14110962300004    False
    14110962300005    False
    14110962300006    False
    14110962300007    False
    14110962300008    False
    14110962300010    False
    14110962300011    False
    14110962300012    False
    14110962300013    False
    14110962300014    False
    14110962300015    False
    14110962300017    False
    14110962300018    False
    14110962300019    False
    14110962300020    False
    14110962300021    False
    14110962300022    False
    14110962300023     True
    14110962300025    False
    14110962300026    False
    14110962300027    False
    14110962300028    False
    14110962300029     True
    14110962300030    False
    14110962300031    False
                      ...  
    WUCH161600453      True
    WUCH161600454     False
    WUCH161600455     False
    WUCH161600456      True
    WUCH161600457     False
    WUCH161600458     False
    WUCH161600459      True
    WUCH161600460     False
    WUCH161600463     False
    WUCH161600464     False
    WUCH161600465      True
    WUCH161600466     False
    WUCH161600467     False
    WUCH161600469     False
    WUCH161600470     False
    WUCH161600473      True
    WUCH161600475      True
    WUCH161600477     False
    WUCH161600480     False
    WUCH161600481     False
    WUCH161600482     False
    WUCH161600486      True
    WUCH161600487     False
    WUCH161600490     False
    WUCH161600491     False
    WUCH161600492     False
    WUCH161600493     False
    WUCH161600496      True
    WUCH161600499     False
    WUCH161600500     False
    Name: ts2, dtype: bool




    # Using boolen mask
    # Add one more column 'churn'
    dfs_last['churn'] = (dfs_last['ts2'] <= '2017-05-31')


    # (Optional)
    # Instead of hard code the date
    # We could use 'N days ago from now'
    print datetime.now() 
    print datetime.now() - timedelta(days=30) # crietia for churn

    2017-08-09 17:38:22.048205
    2017-07-10 17:38:22.048375



    dfs_last.shape
    # (4197, 52) => (4197,53)




    (4197, 53)




    dfs_last.head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>abtm</th>
      <th>br</th>
      <th>brn</th>
      <th>brv</th>
      <th>chn</th>
      <th>ckey</th>
      <th>co</th>
      <th>coiso</th>
      <th>ct</th>
      <th>devm</th>
      <th>...</th>
      <th>tLBuf</th>
      <th>tPld</th>
      <th>tVH</th>
      <th>tid</th>
      <th>ts2</th>
      <th>type</th>
      <th>utype</th>
      <th>v</th>
      <th>yob</th>
      <th>churn</th>
    </tr>
    <tr>
      <th>uid</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13110946900174</th>
      <td>Release</td>
      <td>3425963</td>
      <td>KOOLi_Player</td>
      <td>1.0.11</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Santa Ana</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>5004</td>
      <td>0</td>
      <td>23978</td>
      <td>0ceeb774-b2ff-4fae-a8e4-e26b09862c98</td>
      <td>2017-06-25 23:53:40.532</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>False</td>
    </tr>
    <tr>
      <th>14110954700477</th>
      <td>Release</td>
      <td>5473981</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>China</td>
      <td>CN</td>
      <td>Guangzhou</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7601f004-5675-4369-8403-7bcc26574bd2</td>
      <td>2017-06-05 23:51:55.457</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>False</td>
    </tr>
    <tr>
      <th>14110962300001</th>
      <td>Release</td>
      <td>3577044</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Teaneck</td>
      <td>h3</td>
      <td>...</td>
      <td>5003</td>
      <td>0</td>
      <td>59858</td>
      <td>aa8c169e-ca28-4463-b7eb-6f3a92ab85d4</td>
      <td>2017-06-11 23:49:44.582</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>False</td>
    </tr>
    <tr>
      <th>14110962300002</th>
      <td>Release</td>
      <td>3428368</td>
      <td>KOOLi_Player</td>
      <td>1.0.11</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Fort Lee</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>384d9f1f-e366-4ba0-adbd-1ae5c3c2a267</td>
      <td>2017-06-27 23:57:21.619</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>False</td>
    </tr>
    <tr>
      <th>14110962300003</th>
      <td>Release</td>
      <td>3530742</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Fort Lee</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>5003</td>
      <td>0</td>
      <td>0</td>
      <td>611de4d6-8403-4e2d-a0f4-8986773a5350</td>
      <td>2017-04-28 23:46:52.640</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 53 columns</p>
</div>




    churn_usr_df = dfs_last[dfs_last['churn']==True]


    churn_usr_df.shape




    (708, 53)




    churn_usr_df




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>abtm</th>
      <th>br</th>
      <th>brn</th>
      <th>brv</th>
      <th>chn</th>
      <th>ckey</th>
      <th>co</th>
      <th>coiso</th>
      <th>ct</th>
      <th>devm</th>
      <th>...</th>
      <th>tLBuf</th>
      <th>tPld</th>
      <th>tVH</th>
      <th>tid</th>
      <th>ts2</th>
      <th>type</th>
      <th>utype</th>
      <th>v</th>
      <th>yob</th>
      <th>churn</th>
    </tr>
    <tr>
      <th>uid</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>14110962300003</th>
      <td>Release</td>
      <td>3530742</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Fort Lee</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>5003</td>
      <td>0</td>
      <td>0</td>
      <td>611de4d6-8403-4e2d-a0f4-8986773a5350</td>
      <td>2017-04-28 23:46:52.640</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300023</th>
      <td>Release</td>
      <td>3499534</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Madison</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>faeffc44-57e8-4918-992e-d675ced3e774</td>
      <td>2017-04-20 23:48:42.502</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300029</th>
      <td>Release</td>
      <td>2547806</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Sacramento</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>f78cef04-1602-4709-95cc-3d8872c57bbe</td>
      <td>2017-04-02 23:57:22.418</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300038</th>
      <td>Release</td>
      <td>3468135</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Burke</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>80489625-144a-4f7a-9253-82c2a18e8d66</td>
      <td>2017-04-20 23:49:14.612</td>
      <td>lBuf</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300042</th>
      <td>Release</td>
      <td>3598791</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Chino Hills</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6e096619-d741-4ffd-b100-b04002c87f69</td>
      <td>2017-04-28 23:47:26.992</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300051</th>
      <td>Release</td>
      <td>3716777</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Buena Park</td>
      <td>h3</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5ff978f1-ab0e-4105-9b4b-c7356c79f071</td>
      <td>2017-04-24 23:50:48.936</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300069</th>
      <td>Release</td>
      <td>3580124</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Los Angeles</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>455f8f79-03e2-4c0e-8dab-7bd78088e4f8</td>
      <td>2017-04-10 23:52:44.436</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300073</th>
      <td>Release</td>
      <td>2180614</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Santa Rosa</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>59866</td>
      <td>5259d3e8-35e7-4fde-b614-615242bc6de5</td>
      <td>2017-04-09 23:45:31.087</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300074</th>
      <td>Release</td>
      <td>3619018</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Long Beach</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>5003</td>
      <td>0</td>
      <td>60031</td>
      <td>c19ceef5-3eb4-4cff-83cc-5a0af213fdf9</td>
      <td>2017-04-08 23:46:09.788</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300077</th>
      <td>Release</td>
      <td>3423889</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Burbank</td>
      <td>h3</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>110f72f6-bc3e-463f-9868-6eb1e87bf097</td>
      <td>2017-05-14 23:51:30.789</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300079</th>
      <td>Release</td>
      <td>1344884</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>Canada</td>
      <td>CA</td>
      <td>Ottawa</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>5004</td>
      <td>0</td>
      <td>7940</td>
      <td>47c16ae3-593d-4337-9366-9d9620c031ed</td>
      <td>2017-04-08 23:45:57.282</td>
      <td>upImg</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300091</th>
      <td>Release</td>
      <td>1300940</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>unknown</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>a4f3580e-69ae-4793-8c06-46669cf9633b</td>
      <td>2017-05-24 23:51:46.149</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300102</th>
      <td>Release</td>
      <td>3331364</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Englewood Cliffs</td>
      <td>h3</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0189d60a-560b-472b-9543-34b94647f8ee</td>
      <td>2017-05-19 23:51:21.035</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300107</th>
      <td>Release</td>
      <td>1977691</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Lomita</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>d0ee51c1-4e7b-45f4-961d-ded027bbd579</td>
      <td>2017-05-09 23:56:18.605</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300114</th>
      <td>Release</td>
      <td>3427301</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Buena Park</td>
      <td>h3</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>f6e7d75c-b9c1-498b-abba-5595bf57f8cc</td>
      <td>2017-05-08 23:55:14.966</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300115</th>
      <td>Release</td>
      <td>5508162</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Buffalo Grove</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1b7c5ed7-fb9b-4e51-a045-43b09b277cd9</td>
      <td>2017-04-28 23:47:06.391</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300118</th>
      <td>Release</td>
      <td>2449459</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Irvine</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>769499c7-c430-46c9-8214-14fc1236767a</td>
      <td>2017-05-29 23:51:34.193</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300119</th>
      <td>Release</td>
      <td>3662463</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Colton</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>5004</td>
      <td>0</td>
      <td>59872</td>
      <td>2ed5da07-5370-4fe8-a94c-fa65cbbd4678</td>
      <td>2017-04-16 23:46:11.989</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300131</th>
      <td>Release</td>
      <td>3449491</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>La Habra</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>c7060ad1-ba80-4e9b-8ca6-1716a946df05</td>
      <td>2017-05-02 23:49:54.835</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300133</th>
      <td>Release</td>
      <td>3527629</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Brooklyn</td>
      <td>h3</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>25bf8e1d-b0dd-4dd8-91c4-77d3d9bd2d39</td>
      <td>2017-04-06 23:56:15.283</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300136</th>
      <td>Release</td>
      <td>2468165</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Yucaipa</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>5003</td>
      <td>0</td>
      <td>59903</td>
      <td>9eb91b0d-018a-4657-a211-ddc7339a1fda</td>
      <td>2017-05-25 23:53:18.587</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300144</th>
      <td>Release</td>
      <td>3626274</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Philadelphia</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>fd225f88-2ea6-46d0-8965-d5bbf3d0fae3</td>
      <td>2017-04-15 23:47:52.989</td>
      <td>lBuf</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300169</th>
      <td>Release</td>
      <td>1331298</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Severna Park</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>e1b9f31e-5933-4b4f-9ca8-4534df005260</td>
      <td>2017-05-21 23:48:39.342</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300172</th>
      <td>Release</td>
      <td>3665383</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Greenbrae</td>
      <td>h3</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>840e8835-d3aa-4ff6-ac7e-194aa83a9545</td>
      <td>2017-04-11 23:52:15.323</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110962300178</th>
      <td>Release</td>
      <td>1363586</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Monterey</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>5003</td>
      <td>0</td>
      <td>59892</td>
      <td>6d9364c8-8ffe-43b8-9e2f-c46041be4fbf</td>
      <td>2017-05-29 23:51:06.410</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110963600005</th>
      <td>Release</td>
      <td>3218519</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Hacienda Heights</td>
      <td>h3</td>
      <td>...</td>
      <td>5003</td>
      <td>7</td>
      <td>59867</td>
      <td>588c140d-a17b-42c7-a903-1d3177db7638</td>
      <td>2017-05-11 23:52:51.136</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110963600022</th>
      <td>Release</td>
      <td>3474814</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Severn</td>
      <td>h3</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1870996e-9485-4fe0-ad4d-042cfeef1efd</td>
      <td>2017-05-08 23:55:20.887</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110963600051</th>
      <td>Release</td>
      <td>290709</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Irvine</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>87a2c6ce-c2e1-4729-8982-7bd522df2724</td>
      <td>2017-05-14 23:51:58.695</td>
      <td>upImg</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110963600062</th>
      <td>Release</td>
      <td>3631799</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>unknown</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>5003</td>
      <td>2664748</td>
      <td>51981</td>
      <td>8b3de651-256a-441d-b351-ee6e4830677d</td>
      <td>2017-05-13 23:49:19.290</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>14110963600069</th>
      <td>Release</td>
      <td>5500451</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Palisades Park</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>7f498ba5-6317-46ed-a51a-515781167af7</td>
      <td>2017-05-29 23:51:45.893</td>
      <td>lBuf</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>WUCH155104932</th>
      <td>Release</td>
      <td>1319092</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Irvine</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>47b36786-2ca1-4dec-a420-7f67bb7b8cad</td>
      <td>2017-05-06 23:50:39.239</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH155104933</th>
      <td>Release</td>
      <td>3299974</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>Canada</td>
      <td>CA</td>
      <td>Ottawa</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>5003</td>
      <td>0</td>
      <td>0</td>
      <td>fc2a0e29-025b-4fe3-806a-3894c0308635</td>
      <td>2017-04-13 23:45:29.741</td>
      <td>upImg</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH155104966</th>
      <td>Release</td>
      <td>3394224</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Garfield</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>5003</td>
      <td>0</td>
      <td>27998</td>
      <td>2fd6fc9b-0ebc-427c-9237-93634626f7b9</td>
      <td>2017-05-29 23:51:30.961</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH155104968</th>
      <td>Release</td>
      <td>3757648</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Fort Lee</td>
      <td>h3</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>b744a61e-4e5c-40c7-a0ed-d965a2fef49a</td>
      <td>2017-04-17 23:49:38.545</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH155104993</th>
      <td>Release</td>
      <td>3608066</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Graham</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1df80422-c1d6-4e04-8d12-eead8eaff023</td>
      <td>2017-04-05 00:00:44.206</td>
      <td>lBuf</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH155104998</th>
      <td>Release</td>
      <td>2326568</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>South El Monte</td>
      <td>h3</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2fdb5a52-5b46-4a3b-b403-ddd31958eabc</td>
      <td>2017-05-10 23:53:38.854</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH155105045</th>
      <td>Release</td>
      <td>5509964</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Leonia</td>
      <td>h3</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>a9baa107-f5ec-4fdf-af09-9b48ee73d4f7</td>
      <td>2017-05-21 23:48:10.241</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600252</th>
      <td>Release</td>
      <td>2428944</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Glendale</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>88e43535-5606-4960-b775-4d1c95db31bf</td>
      <td>1970-01-24 17:42:53.296</td>
      <td>lBuf</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600259</th>
      <td>Release</td>
      <td>3782450</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Sunnyvale</td>
      <td>h3</td>
      <td>...</td>
      <td>5003</td>
      <td>0</td>
      <td>3967</td>
      <td>3d974278-ca54-41da-9593-3d78b9d32c96</td>
      <td>2017-05-29 23:49:59.363</td>
      <td>upImg</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600279</th>
      <td>Release</td>
      <td>3333644</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>West Hollywood</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>cc0e54fc-b7b5-449d-8b6f-a1ceb596492b</td>
      <td>2017-05-25 23:51:45.768</td>
      <td>iBuf</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600356</th>
      <td>Release</td>
      <td>289003</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Fullerton</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1bed7115-10f9-4b0e-9765-57938c29eb72</td>
      <td>2017-05-09 23:55:53.973</td>
      <td>lBuf</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600383</th>
      <td>Release</td>
      <td>3510175</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Colorado Springs</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>38e22118-fffb-48be-93da-cd2f4ae0ec67</td>
      <td>2017-05-29 23:51:29.677</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600389</th>
      <td>Release</td>
      <td>3477364</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Manorville</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5fc4a8c6-8464-4545-8c7c-af36e7344cb7</td>
      <td>2017-04-01 23:54:42.100</td>
      <td>upImg</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600396</th>
      <td>Release</td>
      <td>3486695</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Cumming</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1d01db3d-74ee-421a-9f77-f125f0f72afa</td>
      <td>2017-05-28 23:49:13.636</td>
      <td>lBuf</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600399</th>
      <td>Release</td>
      <td>3530160</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Long Island City</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9837d262-eb59-4226-af03-6d820d280727</td>
      <td>2017-05-26 23:54:13.369</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600402</th>
      <td>Release</td>
      <td>1466473</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Puyallup</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>31d3997e-8daa-494f-b43c-425349f5d6d8</td>
      <td>2017-05-04 23:56:24.698</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600404</th>
      <td>Release</td>
      <td>3288087</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Burlingame</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>b7296f21-d3b0-4bc9-ae8f-fbe88536a8a7</td>
      <td>2017-05-07 23:51:13.661</td>
      <td>lBuf</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600413</th>
      <td>Release</td>
      <td>3447785</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Huntington Beach</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>140079e7-b1b2-4ca5-9dda-bb5599b640ec</td>
      <td>2017-04-16 23:44:33.635</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600431</th>
      <td>Release</td>
      <td>3640133</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Santa Paula</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>c782800c-5c90-4fad-9fe8-eb042b04d12a</td>
      <td>2017-05-27 23:52:02.418</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600432</th>
      <td>Release</td>
      <td>2358154</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Los Angeles</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>55f5ca83-e278-438d-b2eb-88f1d41291c9</td>
      <td>2017-05-19 23:51:39.852</td>
      <td>lBuf</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600447</th>
      <td>Release</td>
      <td>5547225</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Gilroy</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>5003</td>
      <td>0</td>
      <td>4014</td>
      <td>dfb1c32d-61d5-430f-a090-c4e88a342f1d</td>
      <td>2017-05-26 23:54:46.915</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600451</th>
      <td>Release</td>
      <td>3606264</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Columbia</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>5004</td>
      <td>0</td>
      <td>59959</td>
      <td>45566212-df8e-4f6d-90a7-d5868638c579</td>
      <td>2017-05-06 23:50:40.419</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600453</th>
      <td>Release</td>
      <td>3690636</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Staten Island</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>05519930-e2d5-41a3-b89b-e505f57ffcd1</td>
      <td>2017-05-23 23:50:39.021</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600456</th>
      <td>Release</td>
      <td>3749167</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Baltimore</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>5003</td>
      <td>0</td>
      <td>59869</td>
      <td>c738fe4f-6ef2-4922-b1e6-0b6219baf7bb</td>
      <td>2017-05-23 23:49:21.875</td>
      <td>upImg</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600459</th>
      <td>Release</td>
      <td>3307579</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Forest</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5b2ee38b-fc22-44c8-a44e-7fc9a9faea90</td>
      <td>2017-04-30 23:46:54.276</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600465</th>
      <td>Release</td>
      <td>965475</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Bethesda</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4459aa51-1195-43d9-9977-01abe30bcbc4</td>
      <td>2017-04-22 23:39:32.133</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600473</th>
      <td>Release</td>
      <td>3520839</td>
      <td>KOOLi_Player</td>
      <td>2.0.7</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>New Park</td>
      <td>h3</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4a52eda8-4009-44e1-9c34-c62d83719fc8</td>
      <td>2017-04-30 23:46:14.569</td>
      <td>upImg</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600475</th>
      <td>Release</td>
      <td>2285424</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Rowland Heights</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>5003</td>
      <td>0</td>
      <td>0</td>
      <td>81fe1f50-6d09-4017-b494-374f46460fb6</td>
      <td>2017-04-27 23:47:50.064</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600486</th>
      <td>Release</td>
      <td>1351600</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Ypsilanti</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0b94a0b1-9118-411c-93d2-deb281950b59</td>
      <td>2017-04-07 23:48:17.575</td>
      <td>vh</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>WUCH161600496</th>
      <td>Release</td>
      <td>3572680</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Granada Hills</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>852aa16b-c314-4982-9775-11294c0ab370</td>
      <td>2017-05-18 23:50:43.239</td>
      <td>mplyevent</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
<p>708 rows × 53 columns</p>
</div>




    print 'Ratio of churn users/unique users: ',\
        float(churn_usr_df.shape[0])/dfs_last.shape[0]

    Ratio of churn users/unique users:  0.168691922802



    # churn user list
    churn_usr_lst = list(churn_usr_df.index)
    print len(churn_usr_lst)

    708



    # churn user list looks like..
    churn_usr_lst[:10]




    [u'14110962300003',
     u'14110962300023',
     u'14110962300029',
     u'14110962300038',
     u'14110962300042',
     u'14110962300051',
     u'14110962300069',
     u'14110962300073',
     u'14110962300074',
     u'14110962300077']



### mark churn users in original DataFrame dfs 


    dfs['uid'].isin(churn_usr_lst)




    0         False
    1         False
    2          True
    3         False
    4         False
    5         False
    6         False
    7         False
    8         False
    9          True
    10        False
    11        False
    12        False
    13         True
    14        False
    15        False
    16        False
    17        False
    18        False
    19        False
    20         True
    21        False
    22         True
    23        False
    24        False
    25        False
    26        False
    27        False
    28        False
    29        False
              ...  
    181970    False
    181971    False
    181972    False
    181973    False
    181974    False
    181975    False
    181976    False
    181977    False
    181978    False
    181979    False
    181980    False
    181981    False
    181982    False
    181983    False
    181984    False
    181985    False
    181986    False
    181987    False
    181988    False
    181989    False
    181990    False
    181991    False
    181992    False
    181993    False
    181994    False
    181995    False
    181996    False
    181997    False
    181998    False
    181999    False
    Name: uid, dtype: bool




    print dfs.ix[2,:]['uid']
    print dfs.ix[2,:]['uid'] in churn_usr_lst

    WUCH155102826
    True



    churn_usr_lst[470:480]




    [u'WUCH155102778',
     u'WUCH155102780',
     u'WUCH155102804',
     u'WUCH155102812',
     u'WUCH155102816',
     u'WUCH155102818',
     u'WUCH155102819',
     u'WUCH155102822',
     u'WUCH155102826',
     u'WUCH155102838']




    # Using boolen mask
    # Add one more column 'churn'
    dfs['churn'] = dfs['uid'].isin(churn_usr_lst) 
    print dfs.shape
    # (182000, 53) => (182000, 54)

    (182000, 54)



    dfs.head()




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>abtm</th>
      <th>br</th>
      <th>brn</th>
      <th>brv</th>
      <th>chn</th>
      <th>ckey</th>
      <th>co</th>
      <th>coiso</th>
      <th>ct</th>
      <th>devm</th>
      <th>...</th>
      <th>tPld</th>
      <th>tVH</th>
      <th>tid</th>
      <th>ts2</th>
      <th>type</th>
      <th>uid</th>
      <th>utype</th>
      <th>v</th>
      <th>yob</th>
      <th>churn</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Release</td>
      <td>3614101</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>Canada</td>
      <td>CA</td>
      <td>Coquitlam</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>49377</td>
      <td>59880</td>
      <td>4e7475b2-0b88-461f-9387-0a9b77251df8</td>
      <td>2017-03-31 23:56:07.535</td>
      <td>vh</td>
      <td>WUCH155103440</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Release</td>
      <td>3328416</td>
      <td>KOOLi_Player</td>
      <td>2.0.6</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Los Angeles</td>
      <td>h3</td>
      <td>...</td>
      <td>72154</td>
      <td>36047</td>
      <td>7e588404-453f-4a45-a8aa-05b6b0ae5be4</td>
      <td>2017-03-31 23:57:12.602</td>
      <td>lBuf</td>
      <td>14110963601665</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Release</td>
      <td>3587620</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Laguna Woods</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>69839</td>
      <td>12022</td>
      <td>f19a8414-64cd-418a-985e-61ae073d8915</td>
      <td>2017-03-31 23:56:57.448</td>
      <td>lBuf</td>
      <td>WUCH155102826</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Release</td>
      <td>1373174</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>West Springfield</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>73567</td>
      <td>39988</td>
      <td>7efccc8b-436d-40bf-8bd5-fe45d08039ca</td>
      <td>2017-03-31 23:55:47.792</td>
      <td>mplyevent</td>
      <td>WUCH161600388</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Release</td>
      <td>1322244</td>
      <td>KOOLi_Player</td>
      <td>1.0.10</td>
      <td></td>
      <td>17943e6c6eec49cdb6</td>
      <td>United States</td>
      <td>US</td>
      <td>Medfield</td>
      <td>WooriKooli W</td>
      <td>...</td>
      <td>70656</td>
      <td>16127</td>
      <td>14bd5375-4a03-460c-b0aa-d73fe16628b7</td>
      <td>2017-03-31 23:54:27.751</td>
      <td>vh</td>
      <td>WUCH155101681</td>
      <td>user</td>
      <td>0.9.1</td>
      <td>Unset</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 54 columns</p>
</div>




    pickle.dump(dfs, open("dfs_churn_marked.p","wb"))
