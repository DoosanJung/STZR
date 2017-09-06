Include your answers to this morning's exercises in `answers.py` or `answers.ipynb`

## Part 1: Access to the data

S3 is the storage system on AWS. Here, you will interact with it to take this test. You can use the information below to download the data. Please note that downloading the data will take few minutes; about two to three minutes.

```Python
bucket_name = 'stlz-dataengineer'
key_name = 'interview-data/interview_data1'
```

Use any library/package to read the file from S3. I recommend using the library `boto` if you plan to do it with `Python`.

**YOU DO NOT NEED `AWS_ACCESS_KEY` AND `AWS_SECRET_ACCESS_KEY` FOR THIS SHORT TEST**

**NOTE: IF YOU CANNOT CONNECT TO OR DOWNLOAD THE DATA FROM AWS S3 BUCKET,
USE THIS DATA** ['interview _data1'](https://drive.google.com/open?id=0B5rOf6SBB06BdFlCczhtaDA1Mk0) **INSTEAD**

<br>

## Part 2: Understand the data

Our company lets on-line video service providers measures viewers' experiences in real-time with their assets across various devices and environments. Our company allows them to have new insight and tune their performance of their streaming service. The message front is the distributed message processing components of our company.

Here's a brief description of the variables including:

|       Information      | Key name |                    Description                    |
|:----------------------:|:--------:|:-------------------------------------------------:|
| customer key           | ckey     | The unique customer key by Streamlyzer            |
| user ID                | uid      | The unique user name in the service               |
| ticket ID              | tid      | The ticket of a viewing media                     |
| Viewing Time           | tVH      | The time how long the user is watching            |
| Player Loading Time    | tPld     | The time what the player is loaded                |
| Initial Buffering Time | tIBuf    | Initial Buffering time                            |
| Re-buffering Time      | tBuf     | Re-buffering time                                 |
| Long Buffering Time    | tLBuf    | Buffering time over 7 minutes                     |
| Log Type               | type     | log type('Buf':Buffering time,..)                 |
| Player Event           | mplyevnt | player event type('brchg':bitrate is changed, ..) |


<br>

1. Load the data

    - The data ranges from *2017-06-29 11:56 pm  ~  2017-06-30 01:20 am*

    - I recommend using the library `Pandas` if you plan to do it with `Python`

2. Clean the data

    - From now on, we'll focus on a customer `'17943e6c6eec49cdb6'`. Remove all other customers for following analysis. (__Hint :__ 'ckey')

    - Drop the rows with `'tid'` equals to `Unset`

    - You'll only need `['uid','tid','tBuf','tIBuf','tLBuf','tPld','tVH','type','mplyevnt']` columns from now on. Please note that columns related to *time* are continuous variables, while others are categorical variables

3. Now we start analyzing this data

    - How many unique users are there ? 

4. Draw a table such as follows.

    - For the *time* variables, such as tVH, you'll need to **sum** them to get the total time. For example, for uid X and tid 1, there can be more than one `viewing time` log (during watching a video) for this uid X and tid 1. In this case, summing up time variables within same uid and tid will give you the total time, which is presented in table below. For example, how long were the viewing time for uid X and tid 1 can be calculated
    <br>(__Hint :__ `Pandas.DataFrame.groupby` to the rescue)

    - For the *categorical* variables, you'll need to **count** how many times each category appeared in the logs. For example, how many times bitrate change occurred can be calculated

    - Result would looks like this. (column order does not matter here)


      | uid   | tid   | Viewing time('tVH') | ... | Bitrate change('brchg') | ... |
      |-------|-------|---------------------|-----|-------------------------|-----|
      | uid X | tid 1 | 120000              | ... | 4                       | ... |
      | uid X | tid 2 | 0                   | ... | 0                       | ... |
      | uid X | tid 3 | 50000               | ... | 0                       | ... |
      | uid Y | tid 4 | 2532300             | ... | 1200                    | ... |
      | uid Y | tid 5 | 5000                | ... | 0                       | ... |
      | ...   | ...   | ...                 | ... | ...                     | ... |

<br>

## Part 3: Descriptive statistics

Often times, we are interested in the summary statistics of our data.

1. From the table above (Part2.4), calculate the average `Viewing Time`
    - We want you to describe the meaning of what you've calculated. For example, what does the mean value of 'viewing time' represents?

2. Plot histogram for `Viewing Time`.
