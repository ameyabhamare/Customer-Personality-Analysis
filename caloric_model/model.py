'''
This file handles the caloric model module
'''
from sklearn.linear_model import LinearRegression
import pandas as pd

def transform_dataframe(df_):
    '''
    This function adds new features/columns to the dataframe
    '''
    df_['ActivityDate'] = pd.to_datetime(df_['ActivityDate'])
    df_['year'] = df_['ActivityDate'].dt.year
    df_['month'] = df_['ActivityDate'].dt.month
    df_['dayofweek'] = df_['ActivityDate'].dt.dayofweek
    day_mapping = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun' }
    df_['dayofweek'] = df_['dayofweek'].map(day_mapping)
    return df_

def model_pipeline(df_, x):
    '''
    This is a model functions and it returns the linear regression object
    '''
    i = df_.loc[:, x].values.reshape(-1, 1)  # values converts it into a numpy_ array_
    j = df_.loc[:, 'Calories'].values.reshape(-1, 1)  # -1: calc dimensn of rows, but have 1 column
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(i, j)  # perform linear regression
    #Y_pred = linear_regressor.predict(X_)  # make predictions
    return linear_regressor
