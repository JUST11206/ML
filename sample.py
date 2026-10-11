#use pandas library for analysis data
import pandas as pd
from sklearn.preprocessing import LabelEncoder

#random data for dataframe
#none is empty value in data
data = {
    "Name": ["malik", "sadie", "ahmed","saad","zain"],
    "Gender": ["male", "female", "male", None, "male"],
    "Age": [20, 21, 22, None, 24],
    "Salary": [1000, 2000, 3000, 4000, 5000]
 }

#create dataframe using DataFrame()
df = pd.DataFrame(data)
# print(df)

#drop empty value columns 
drop_df = df.dropna()
print(drop_df)

#fill empty values with 0
fill_df = df.fillna(0)
print(fill_df)

#sum of all column empty values
#We can find the column to clean data
print(df.isnull().sum())

#LabelEncoder is a object  used to convert categorical data into numerical data
le = LabelEncoder()
#here we are encoding the Gender column into numerical values
df['Gender_Encoded'] = le.fit_transform(df['Gender'])

print("\nThis is clean DataFrame\n")
print(df)
print("\n")
print(df[['Gender', 'Gender_Encoded', 'Age', 'Salary']])