######

# Creating a Dataframe for the famous climbs, Normalization #


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

with open('famous_segments.json') as f:

    data = json.load(f)

df = pd.json_normalize(data)

# test

""" 
print(df.head())
print(df.describe())
print(df.info())
print(df.tail())
print(df.shape) """


# columns to keep: elapsed_time over moving_time 

columns_to_keep = ['distance', 'average_grade', 'maximum_grade', 'elevation_high', 'elevation_low', 'climb_category']

df_famous_climbs = df.loc[:, columns_to_keep]

# dummy aus column segment.climb_category

dummy_vars = pd.get_dummies(df_famous_climbs['climb_category'], prefix='climb_cat', drop_first=True)

# Add the dummy variables to the original DataFrame

df_famous_climbs = pd.concat([df_famous_climbs, dummy_vars], axis=1)

# Drop the original 'segment.climb_category' column

df_famous_climbs = df_famous_climbs.drop('climb_category', axis=1)


# test

""" print(df_famous_climbs.head())
print(df_famous_climbs.describe())
print(df_famous_climbs.info())
print(df_famous_climbs.tail())
print(df_famous_climbs.shape)
print(df_famous_climbs.isnull) """


