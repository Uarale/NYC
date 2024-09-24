# NYC_Public_Schools

# NYC Public Schools SAT Performance Analysis

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technology Used](#technology-used)
3. [Process](#process)
4. [The Data](#the-data)
6. [Insigts](#insights)
7. [Credits](#credits)

## Project Overview
Every year, American high school students take the SATs, standardized tests that assess literacy, numeracy, and writing skills. With three sections—reading, math, and writing—each scored out of 800 points, these tests are crucial for students and colleges during the admissions process.

In this project, I analyzed SAT performance across New York City public schools using a dataset called `schools.csv`. The aim was to answer three key questions regarding the schools’ performance, which is valuable for various stakeholders, including educators, policymakers, and parents.

## Technology Used
- **Python**
- **Pandas**: Utilized for data manipulation and analysis, allowing me to efficiently handle the dataset and perform the calculations.
  
## Process
1. **Data Collection**: I started by reading in the `schools.csv` dataset, which contains information about NYC public schools and their SAT scores.
2. **Data Exploration**: Explored the dataset to understand its structure and identify any missing values.
3. **Data Cleaning**: Cleaned the data by removing any rows with missing values and rounding numeric values to two decimal places for consistency.
4. **Analysis**: Answered specific questions about school performance, including:
   - Identifying the best math-performing schools.
   - Determining the top 10 schools based on combined SAT scores.
   - Finding the borough with the largest standard deviation in combined SAT scores.
5. **Results Presentation**: Printed out the results of each analysis step, highlighting key insights.

## The Data: `schools.csv`

| Column             | Description                                            |
|--------------------|--------------------------------------------------------|
| `school_name`      | Name of the school                                     |
| `borough`          | Borough where the school is located                   |
| `average_math`     | Average math SAT score                                |
| `average_reading`  | Average reading SAT score                             |
| `average_writing`  | Average writing SAT score                             |
| `total_SAT`        | Combined SAT score (math + reading + writing)        |


### Insights Gained from NYC School Performance Analysis

1. **Data Cleaning and Preparation**:
   - Before diving into the analysis, I ensured the data was clean by checking for and removing any missing values. This step was crucial in maintaining the integrity of my analysis. Additionally, I rounded all numeric values to two decimal places, which not only made the dataset more visually appealing but also easier to interpret.

2. **Top Math Performers**:
   - My analysis revealed that the school with the best average math results is **"New Explorations into Science, Technology and Math High School"**, which exceeded the threshold of 640 points (80% of the maximum score). This insight highlights the school’s strong emphasis on mathematics, which may be beneficial for students looking to excel in STEM fields.

3. **Overall SAT Performance**:
   - I identified the top 10 schools based on their combined SAT scores. Notably, the **High School for Dual Language and Asian Studies** topped the list with the highest total SAT score. This information is essential for parents and students aiming for schools with strong overall academic performance.

4. **Variability Across Boroughs**:
   - Unfortunately, all the schools in this dataset were located in Manhattan, which limited the diversity of boroughs for comparison. This lack of variation made it challenging to explore the variability across different boroughs. However, I found that Manhattan had the largest standard deviation in combined SAT scores, indicating a wider disparity in performance among its schools. This suggests that while some schools perform exceptionally well, others may struggle significantly, and further investigation may be warranted to understand the reasons behind this variability.

5. **School Distribution**:
   - The analysis of school counts revealed that there are a total of 4 schools in Manhattan, showcasing the borough's limited but potentially high-quality educational options. This insight may prompt further investigation into the reasons behind the limited number of schools and the implications for student enrollment.

6. **Average SAT Score**:
   - The average combined SAT score across the dataset was found to be **1,295 points**. This figure provides a benchmark for evaluating individual school performances and can help stakeholders gauge the overall academic climate of NYC schools.

## Credits

I would like to thank DataCamp for providing the dataset which helped me successfully complete this small project. Their resources have been invaluable in my journey to obtain my Data Analyst certificate.
