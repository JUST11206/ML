#input csv file and convert to dataframe
#openpyxl library is used to read excel file
import pandas as pd
import openpyxl
#read_excel() function is used to read excel file and convert to dataframe
df_csv = pd.read_excel("challenge.xlsx")
df_csv = df_csv.copy()
print(df_csv)
print("\nThis is clean DataFrame\n")
df_csv = df_csv.dropna()
print(df_csv)