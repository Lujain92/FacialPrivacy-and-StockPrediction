import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from datetime import datetime
from sklearn.linear_model import LinearRegression

# load the dataset
df = pd.read_csv('price_model\prices.csv')
# print(df)

# create a dates array
dates=df['Date'].values

# create a prices numpy array
y = df['Price'].values
print(y)


# for the data of dates that I have in csv file, it consist of multiple dates format so I need to covert 
# them to one format

# Define the desired output format 
output_format = '%m-%d-%Y'

# Create an empty list to store the formatted dates
formatted_dates = []

# Loop through each date in the array
for date_str in dates:
    try:
        # Try to convert the date string to datetime object using the first format
        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
    except ValueError:
        try:
            # If the first format doesn't work, try the second format
            date_obj = datetime.strptime(date_str, '%m-%d-%y')
        except ValueError:
            try:
                # If the second format doesn't work, try the third format
                date_obj = datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                # If none of the formats work, print an error message and skip to the next date
                print(f'Error: {date_str} is not a recognized date format')
                continue
    
    # Format the datetime object to the desired output format and append to the list
    formatted_dates.append(datetime.strftime(date_obj, output_format))

# Print the formatted dates
print(formatted_dates)

# convert the formatted dates into numpy array
np_array = np.array(formatted_dates)




# Define an array of date strings in the format '%m-%d-%Y'
date_str_array = np.array(np_array)

# Convert the date strings to datetime objects
date_obj_array = np.array([datetime.strptime(date_str, '%m-%d-%Y') for date_str in date_str_array])

# Convert the datetime objects to Unix timestamps
unix_timestamp_array = np.array([date_obj.timestamp() for date_obj in date_obj_array])

# Convert the Unix timestamps to floats using NumPy's float64 data type
float_array = unix_timestamp_array.astype(np.float64)

print(float_array) 



# # to train the model

x = float_array.reshape((-1,1))



# split the dataset into training and testing sets
x_train, x_test, y_train, y_test  = train_test_split(x,y,train_size=.8, test_size=.2, random_state=100 )

# create the linear regression model and train it on the training set
lr=LinearRegression()
lr.fit(x_train,y_train)
# make predictions on the test set

y_predict=lr.predict(x_test)

print(y_predict)

# evaluate the performance of the model

the_score=lr.score(x_test,y_test) *100 # 71.9 
print(the_score)



