Include your answers to this morning's exercises in `answers.py` or `answers.ipynb`

## Part 1: Access to the data

S3 is the storage system on AWS. Here, you will interact with it to take this test. You can use the information below to download the data. Please note that downloading the data will take few minutes; about two to three minutes.

```Python
bucket_name = 'stlz-dataengineer'
key_name = 'interview-data/interview_data1'
```

Use any library/package to read the file from S3. I recommend using the library `boto` if you plan to do it with `Python`.

**NOTE: IF YOU CANNOT CONNECT TO OR DOWNLOAD THE DATA FROM AWS S3 BUCKET,
USE THIS DATA** ['interview _data1'](https://drive.google.com/open?id=0B5rOf6SBB06BdFlCczhtaDA1Mk0) **INSTEAD**

<br>

## Part 2: Understand the data

Our company lets on-line video service providers measures viewers' experiences in real-time with their assets across various devices and environments. Our company allows them to have new insight and tune their performance of their streaming service. The message front is the distributed message processing components of our company.

Here's a brief description of the variables including:

   ![image](imgs/img1.png)
   ![image](imgs/img2.png)
   ![image](imgs/img3.png)   
   ![image](imgs/img4.png)
<br>

1. Load the data

    - From now on, we'll focus on a customer '17943e6c6eec49cdb6'. Remove all other customers for following analysis. (__Hint :__ 'ckey')

    - The data ranges from *2017-06-29 11:56 pm  ~  2017-06-30 01:20 am*

    - How many logs are there with this customer?

    - How many log types are there? (__Hint :__ 'type') and what are they?

2. Drop the rows with 'tid' which do not have a meaningful value. This tid looks very different from others. I bet you can tell once you find one

    - You'll only need ['uid','tid','tBuf','tIBuf','tLBuf','tPld','tVH','type','mplyevnt'] columns from now on. Please note that columns related to *time* are continuous variables, while others are categorical variables

    - __Hint :__ 'tid' looks like this: 08e784c7-ecc5-4012-8674-0847dfdef2d1. For some reason, there is a tid with very different value

    - __IMPORTANT :__ Same 'tid's should have same 'uid'. Find the 'tid' with different 'uid'. One way to do this is using `pandas.DataFrame.groupby`.

3. Now we start analyzing this data

    - How many unique users are there ? ...(1)

    - How many users have only one tid ? ...(2)

    - How many users have more than one tids ? ...(3)

    - For a sanity check, (1) == (2)+(3)?

4. Draw a table such as follows.

    - For the *time* variables, such as tVH, you'll need to **sum** them to get the total time. For example, for uid X and tid 1, there can be more than one viewing time log (during watching a video) for this uid X and tid 1. In this case, summing up time variables within same uid and tid will give you the total time, which is presented in table below. For example, how long were the viewing time for uid X and tid 1 can be calculated
    <br>(__Hint :__ groupby to the rescue)

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

1. From the table above (Part1.3), find mean value, standard deviation, minimum value, maximum value for each column
    - We want you to describe the meaning of what you've calculated. For example, what does the mean value of 'viewing time' represents?

2. Plot histogram for a column 'tVH'. Here, you can convert the time unit into 'minutes' if you want. 'tVH' is in milliseconds

3. Draw one more table such as follows
    - You'll use 'uid','tid','tBuf','tIBuf','tLBuf','tPld','tVH','type','mplyevnt' columns again. Again, columns related to *time* are continuous variables, while others are categorical variables. Please refer to the table below. Note that 'tid' has gone

    - Find mean value, standard deviation, minimum value, maximum value for each column.

    - We want you to describe the meaning of what you've calculated. For example, what does the mean value of 'viewing time' represents?

    - Result would looks like this (column order does not matter here)


        | uid   | Viewing time('tVH') | ... | ... | Bitrate change('brchg') | ... |
        |-------|---------------------|-----|-----|-------------------------|-----|
        | uid X | 34560000            | ... | ... | 40                      | ... |
        | uid Y | 937400              | ... | ... | 100                     | ... |
        | uid Z | 17470000            | ... | ... | 20340                   | ... |
        | uid M | 34985000            | ... | ... | 120000                  | ... |
        | uid N | 5000                | ... | ... | 0                       | ... |
        | ...   | ...                 | ... | ... | ...                     | ... |

_4. Find the user who has maximum viewing time (i.e. the length of the viewing time). How long did the user watched? 'tVH' is in milliseconds, how long the viewing time in minutes?

_5. Plot histogram for a column 'tVH'. Here, you can convert the time unit into 'minutes' if you want. 'tVH' is in milliseconds
