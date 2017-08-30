Include your answers to this morning's exercises in `answers.py` or `answers.ipynb`

## Part 1: Understand the data

The streamlyzer lets on-line video service providers measures viewers' experiences in real-time with their assets across various devices and environments. The Streamlyzer allows them to have new insight and tune their performance of their streaming service. The message front is the
distributed message processing components of Streamlyzer.

Here's a brief description of the variables including:

   ![image](images/resid_plot.png)
<br>

1. Load the data

  From now on, we'll focus on a customer '17943e6c6eec49cdb6'. Remove all other customers for following analysis. (__Hint :__ ckey)

  **Q1:**
  - How many logs are there with this customer?
  - How many log types are there? (__Hint :__ type) and what are they?

  <br>

2. Drop 'tid's which do not have a specified user (__Hint :__'uid') from the data.

  **Q2:**
  - How many users are there?
  - How many users viewed only one video (__Hint :__'tid') ?
  - How many users viewed more than one videos (__Hint :__'tid') ?

  <br>

3. Draw a table such as follows.
  - You'll only need 'uid','tid','tBuf','tIBuf','tLBuf','tPld','tVH','type','mplyevnt' columns from now on. Columns related to *time* are continuous variables, while others are categorical variables

  - For the *time* variables, such as tVH, you'll need to **sum** them to get the total time. For example, for uid X and tid 1, there can be more than one viewing time log for this uid X and tid 1. In this case, summing up time variables within same uid and tid will give you the total time, which is presented in table below. For example, how long were the viewing time for uid X for tid 1 can be calculated
  <br>(__Hint :__ groupby to the rescue)

  - For the *categorical* variables, you'll need to **count** how many times each category appeared in the logs. For example, how many times bitrate change occurred can be calculated

  - Result would looks like this


      | uid   | tid   | ViewHour('tVH') | ... | ... | Bitrate change('brchg') | ... |
      |-------|-------|-----------------|-----|-----|-------------------------|-----|
      | uid X | tid 1 | 120000          | ... | ... | 4                       | ... |
      | uid X | tid 2 | 0               | ... | ... | 0                       | ... |
      | uid X | tid 3 | 50000           | ... | ... | 0                       | ... |
      | uid Y | tid 4 | 2532300         | ... | ... | 1200                    | ... |
      | uid Y | tid 5 | 5000            | ... | ... | 0                       | ... |
      | ...   | ...   | ...             | ... | ... | ...                     | ... |


<br>

## Part 2: Descriptive statistics

Often times, we are interested in the summary statistics of our data.

1. From the table above (Part1.3), find mean value, standard deviation, minimum value, maximum value for each column
    - Describe the meaning of what you've calculated. For example, what does the mean value of 'some number' for viewing time represent?

2. Plot histogram for each column

3. Draw one more table such as follows
    - You'll use 'uid','tid','tBuf','tIBuf','tLBuf','tPld','tVH','type','mplyevnt' columns again. Columns related to *time* are continuous variables, while others are categorical variables

    - This time, We want to know each user's summery statistics. Find mean value, standard deviation, minimum value, maximum value for each column.

    - Describe the meaning of what you've calculated. For example, what does the mean value of 'some number' for viewing time represent?

    - Result would looks like this


        | uid   | ViewHour('tVH') | ... | ... | Bitrate change('brchg') | ... |
        |-------|-----------------|-----|-----|-------------------------|-----|
        | uid X | 34560000        | ... | ... | 40                      | ... |
        | uid Y | 937400          | ... | ... | 100                     | ... |
        | uid Z | 17470000        | ... | ... | 20340                   | ... |
        | uid M | 34985000        | ... | ... | 120000                  | ... |
        | uid N | 5000            | ... | ... | 0                       | ... |
        | ...   | ...             | ... | ... | ...                     | ... |

*4. Plot histogram for each column
