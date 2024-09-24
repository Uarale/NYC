#import the necessary package
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

#Read in the CSV file containing the data
schools = pd.read_csv("/Users/usamasuleiman/Downloads/datalab_export_2024-08-28 11_50_39.csv")

#Check out the Data
print(schools.head())

#Find if there are missing values and then remove them.
schools_missing_values = schools.isna().sum()
print(schools_missing_values)

schools_cleaned= schools.dropna()
print(schools_cleaned)

#Verifying if missing values are still present
schools_missing_values_after= schools_cleaned.isna().sum()
print(schools_missing_values_after)

#Its clean and tidy!

#In order to keep our data tidy, we will also round up all our numeric values to two decimal places

schools_cleaned = schools_cleaned.round(2)

#Which NYC school have the best math results?

#Start with calculating the threshold, which is 80%
800 * 0.8 == 640


best_math_schools = schools[schools["average_math"] >= 640][["school_name", "average_math"]].sort_values("average_math", ascending = False)

print(best_math_schools)

#The school with the best math results on average is "New Explorations into Science, Technology and Math High School"!

#What are top 10 best performing schools based on the combined SAT scores?
#Start by combining each individual SAT score in a list and save it as "total_SAT"

schools_cleaned.loc[:, "total_SAT"] = (schools_cleaned["average_math"] +
    schools_cleaned["average_writing"] +
    schools_cleaned["average_reading"])

top_10_schools = schools_cleaned.sort_values(by="total_SAT", ascending = False).head(10)

#Aligning the index with the sorted data
top_10_schools =top_10_schools.reset_index(drop=True)

#Starting from 1
top_10_schools.index = top_10_schools.index + 1

#Selecting the relevant columns to display
top_10_schools = top_10_schools[["school_name", "average_math", "average_writing", "average_reading", "total_SAT"]]

#Selecting only the "school_name" and "total_SAT" columns
top_10_schools = top_10_schools[["school_name", "total_SAT"]]

print(top_10_schools)

#We can see that the high school for dual language and asian studies is at the very top!

#Which single borough has the largest standard deviation in the combined SAT score?
largest_std_dev =schools_cleaned.groupby("borough")["total_SAT"].std()

#Convert the result to a DataFrame
largest_std_dev = pd.DataFrame(largest_std_dev)

#Finding the borough with the largest standard deviation

largest_std_dev_by_borough = largest_std_dev.loc[largest_std_dev["total_SAT"].idxmax()]

print(largest_std_dev_by_borough)

#We can see that the borough with the largest standard deviation is Manhattan


#What is the number of schools in the borough
num_schools = schools_cleaned.groupby("school_name")["borough"].value_counts()

print(num_schools)
# We can see that there are a total of 4 schools in the borough Manhattan.

#What is the average of Total_SAT?

average_SAT = schools_cleaned["total_SAT"].mean()

print(average_SAT)
#The average of total_SAT is 1 295 points.