import pandas as pd
from sklearn.linear_model import LinearRegression
from utils import analysis_utils

def process_daily_activity_data(df_daily_activity, user_id='1503960366'):
    df_daily_activity = analysis_utils.filter_df_user_id(df_daily_activity, user_id)

    df_daily_activity['ActivityDate'] = pd.to_datetime(df_daily_activity['ActivityDate'])
    df_daily_activity['year'] = df_daily_activity['ActivityDate'].dt.year
    df_daily_activity['month'] = df_daily_activity['ActivityDate'].dt.month
    df_daily_activity['dayofweek'] = df_daily_activity['ActivityDate'].dt.dayofweek

    return df_daily_activity


def daily_activity_calories_linreg_model(df, x):
    '''
    This is a model functions and it returns the linear regression object
    '''
    i = df.loc[:, x].values.reshape(-1, 1)  # values converts it into a numpy_ array_
    j = df.loc[:, 'Calories'].values.reshape(-1, 1)  # -1: calc dimensn of rows, but have 1 column
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(i, j)  # perform linear regression
    #Y_pred = linear_regressor.predict(X_)  # make predictions
    return linear_regressor
