<h1 style="text-align: center; border-bottom: 1px dashed">G-Limited. (Employee Attrition)</h1>

## About Dataset
The data was obtained from a friend, so I honestly don't know the genesis of this data. Still, upon research, I saw a very similar dataset on Kaggle<a href="https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset"> IBM HR Analytics Employee Attrition & Performance</a> so I would reference that. It is a fictional dataset designed by IBM data scientists for the sole purpose of learning.

## Introduction.
G-Limited is a fictional company that wants to understand the factors that lead to employee attrition in their company, employing the expertise of an analyst G-Limited wants to explore important questions that could potentially help to derive insight from the data to help them make the best decision to retain employees.

## PROCESS
### Data Extraction.
As a firm believer in the gospel of Python, I was given a database file (.db) and was told to extract the data from it using Python. The data extraction was fairly straightforward because the database was created using SQLite an inbuilt Python database. After importing SQLite3, I then performed the data extraction.

<img src=images/attr_extraction.png style="width: 50%; height:60%"><br>

### Data cleaning
After extracting the data, I cleaned it using a Jupyter Notebook, which is more suited to this purpose.

I employed the following rules;
1. <b>Data Exploration:</b> This is where I look through the distribution and see the data types of the columns in the dataset, check for missing values, and ensure everything is okay.

2. <b>Data Cleaning:</b> This is where I perform cleaning by going through each of the columns of the data set

3. <b>Data Validation:</b> This is where I look at the previous dataset (pre-cleaning) and the new dataset (post-cleaning) and appreciate <b>Guido Van Rossum</b> for creating a sweet language.

4. <b>Extract the clean data:</b> and after all that, save the cleaned data.

### Data Analysis
After cleaning with Python and extracting the data, I took the data to PowerBi where I did a proper Analysis of the data, designed a simple report, and came out with insights that answered our guiding questions.

<a href="https://www.novypro.com/project/employee-attrition-dashboard-4"><img src=images/attr.png style="width: 70%; height:60%"></a><br>
<a href="https://www.novypro.com/project/employee-attrition-dashboard-4">Click to visit the dashboard.</a>


## Guiding questions
<ol>
    <li>Does monthly income play a part in employee attrition?
    <li>Which department lost the most staff and why??
    <li>What age bracket do most of our staff come from?
    <li>What is the most likely reason that staff leave the company?
</ol>

## Answer to guiding questions.

1. Yes, monthly income does play a heavy part in the rate of attrition, based on the trend in the job's section of the visual we can see that the lower the monthly income the higher the rate of attrition, with sales representative having a 40% attrition rate with a total monthly income of $217,958
while research directors have the lowest rate of attrition at 3% with a total monthly income of $1,282,684, so we can see that the higher the rate of income the lower the rate of attrition.

2. By default it won't be surprising that it is Research and Development that lost the most staff (133 staff) because their numbers are more than another department, but taking a closer look into that department we see that 62 of those staff left are Laboratory Technicians which is the second most populous after Research scientists, taking a closer look again shows that out of those 62 that left, 56 of them are level 1 staffs and their pay are the smallest compared to other levels, but comparing them to other Level 1 workers their pay is the smallest, they are the most underpaid staffs in the company, that is most likely what contributed to their exit from the company.

3. Most of our staff come from the 30-39 age bracket with a total of 622 staff. 533 of them are still active while 89 of them have left the company.

4. There are multiple reasons people would have left the company, ranging from personal preference to organizational issues. so based on the data I can give 3 reasons that staff most likely left G-Limited;

- 127 of the staff that left were working overtime, that's over 53% of staff that was working overtime also looking at the total monthly income across all levels, the overtime workers were earning less than the non-overtime workers.

- Monthly Income is also an issue, the rate of attrition increases where monthly income reduces, and this increase in the rate of attrition affected mostly 3 Job roles; - Laboratory Technicians, Human resources, and Sales representatives these 3 groups were earning the least compared to other departments.

- Stock Option level is also a possible reason, approximately 65% of staff that left had no stock option level, we would have said that lower level staff members had no stock option level but there are level one staff with a stock option level of 3. So it is safe to say the stock options level also contributed to the departure of staff.

## General takeaway:

- With a total of 1,470 employees, in terms of attrition we have 16% of employees who have left and 1,233 (84%) who are still active.

- Based on this distribution the data is  skewed, also having more males (822 60%) than females (588 40%), this skewness already shows a possibility of more attrition in men than in women.

- G-Limited has more married staff about 46% of the staff are currently married, 32% are single and the other 22% represent staff that are divorced

- Most of the active and inactive staff are in the 30-39 age group (533 and 89 respectively) while the least age group is 60+ with only 5 staff (2 female and 3 male staff).

- We have 3 departments in G-Limited: Sales, Research and Development, and Human Resources having (446, 961, and 63 staff respectively)

## Technology used.
<ul>
    <li>Python
        <ul>
            <li> Numpy
            <li>Pandas
            <li> Sklearn
            <li> SQLite
        </ul>
    <li>PowerBi
    <li>Navypro (dashboard hosting)
</ul>
<hr>
<div style="text-align: center;">
<a href="https://oluwaseun-ogundeko.netlify.app/">Learn more about me!</a>
</div>
