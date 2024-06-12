###########

### Model  #####

### regression:

# model = A random forest regressor.

### version 2


# imports
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# import dataframes
from dataframe import df
from dataframe_famous_climbs import df_famous_climbs

# cadence und heartrate droppen

df = df.drop(['average_cadence', 'average_heartrate'], axis=1)


# steo1: training data


# Assume you have a Pandas DataFrame `df` with features `X` and target `y`

X = df.drop('elapsed_time', axis=1)  # features

y = df['elapsed_time']  # target variable

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model
model = RandomForestRegressor()

model.fit(X_train, y_train)

# step 2: testing 

# testing

y_pred = model.predict(X_test)

# evaluate the model
# RMSE

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

# MSE

print(f'MSE: {mse:.2f}')

# Calculate mean absolute error

mae = mean_absolute_error(y_test, y_pred)

print(f'MAE: {mae:.2f}')

# Calculate R-squared score

r2 = r2_score(y_test, y_pred)

print(f'R-squared: {r2:.2f}')


# add missing columns with 0 values:

missing_columns = list(set(X.columns) - set(df_famous_climbs.columns))
for col in missing_columns:
    df_famous_climbs[col] = 0

# same order 
df_famous_climbs_features = df_famous_climbs[X.columns]


# step 3: prediction on new data

predictions = model.predict(df_famous_climbs_features)


# step 5: use the predictions:

# store predictions in new variable and use in streamlit

# -> predictions

print(predictions)

divided_list = [round(x / 60, 2) for x in predictions]

print(divided_list)

# 1."Stelvio" : 18663867
# 2. "Galibier": 18328881
# 3. "Mont Ventoux": 7711822
# 4. "Alp d' Huez": 13907878
# 5. "Col du Tourmalet": 34128342
# 6. "Alto de letras": 12648314
# 7. "Teid"e: 707733
# 8. "Monte Grappa": 611629
# 9. "Hawk Hill": 12667647
# 10. "Brocken": 18051783


# Create a new column in the original dataframe with the predicted elapsed times in minutes
df_famous_climbs['predicted_elapsed_time_minutes'] = divided_list

# add another column with the column names

climb_names = ["Stelvio", "Galibier", "Mont Ventoux", "Alp d' Huez", "Col du Tourmalet", "Alto de letras", "Teide", "Monte Grappa", "Hawk Hill", "Brocken"]
df_famous_climbs['climb_name'] = climb_names

#test

print(df_famous_climbs[['climb_name', 'predicted_elapsed_time_minutes']])

""" 

df_famous_climbs_RT3 = df_famous_climbs 

print(df_famous_climbs_RT3[['climb_name', 'predicted_elapsed_time_minutes']]) """