######

# Creating a Dataframe from 3 json files, Normalization   #


########

#Pandas will be the backbone of our data manipulation.
import pandas as pd
#Matplotlib is a data visualization library. 
import matplotlib.pyplot as plt
#Numpy will help us handle some work with arrays.
import numpy as np
# import json
import json


# normalize nested json files

with open('all_efforts1.json') as f:

    data = json.load(f)

df1 = pd.json_normalize(data)

# test

""" print(df1.head())
print(df1.describe())
print(df1.info())
print(df1.tail())
print(df1.shape) """

# normalize nested json files

with open('all_efforts2.json') as f:

    data = json.load(f)

df2 = pd.json_normalize(data)

# test

""" print(df2.head())
print(df2.describe())
print(df2.info())
print(df2.tail())
print(df2.shape) """

# normalize nested json files

with open('all_efforts3.json') as f:

    data = json.load(f)

df3 = pd.json_normalize(data)

# test
""" 
print(df3.head())
print(df3.describe())
print(df3.info())
print(df3.tail())
print(df3.shape) """

# concat two data frames
print('After concat:')
df = pd.concat([df1, df2, df3], axis=0)


# columns to keep: elapsed_time over moving_time 

columns_to_keep = ['elapsed_time', 'average_cadence', 'average_heartrate', 'segment.distance', 'segment.average_grade', 'segment.maximum_grade', 'segment.elevation_high', 'segment.elevation_low', 'segment.climb_category']

df = df.loc[:, columns_to_keep]


# rename column names without prefix

df = df.rename(columns=lambda x: x.replace('segment.', ''))

# Calculate the mean of 'maximum_grade'
mean_maximum_grade = df['maximum_grade'].mean()

# Replace the outlier in 'maximum_grade' with the mean
df.loc[df['maximum_grade'].idxmax(), 'maximum_grade'] = mean_maximum_grade

# dummy aus column segment.climb_category

dummy_vars = pd.get_dummies(df['climb_category'], prefix='climb_cat', drop_first=True)

# Add the dummy variables to the original DataFrame

df = pd.concat([df, dummy_vars], axis=1)

# Drop the original 'segment.climb_category' column

df = df.drop('climb_category', axis=1)

# Calculate the mean of 'average_heartrate'

mean_average_heartrate = df['average_heartrate'].mean()

# Fill missing values in 'average_heartrate' with the mean

df['average_heartrate'] = df['average_heartrate'].fillna(mean_average_heartrate)

# Calculate the mean of 'average_cadence'

mean_average_cadence = df['average_cadence'].mean()

# Fill missing values in 'average_cadence' with the mean

df['average_cadence'] = df['average_cadence'].fillna(mean_average_cadence)

df = df.dropna()

# test

""" print(df.head())
print(df.describe())
print(df.info())
print(df.tail())
print(df.shape)
print(df.isnull) """


