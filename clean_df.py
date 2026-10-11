
from sklearn.preprocessing import StandardScaler, MinMaxScaler 

from sklearn.model_selection import train_test_split
import pandas as pd

data = {
    "hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "score": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

#obkect creation for StandardScaler
standard_scaler = StandardScaler()
minmax_scaler = MinMaxScaler()
#convert the data into standard scaled data
standard_scaled = standard_scaler.fit_transform(df)
minmax_scaled = minmax_scaler.fit_transform(df)


print("\nThis is scaled DataFrame\n")
print(pd.DataFrame(standard_scaled, columns=["hours", "score"]))
print(pd.DataFrame(minmax_scaled, columns = ["hours", "score"]))

#divide data into training and testing data
#42 is a default random state value used to split the data into training and testing data
#.2 means 20% of data is used for testing and 80% of data is used for training
#so basically we are splitting (divide) the data

x = df[["hours"]]
y = df[["score"]]

#train_test_split() function is do split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("Training Data:")
print(x_train)
print(y_train)

print("Testing Data:")
print(x_test)
print(y_test)


# from sklearn.linear_model import LinearRegression

# model = LinearRegression()

# model.fit(x_train, y_train)

# predictions = model.predict(x_test)

# print("Actual score:", y_test.values)
# print("Predicted score:", predictions)