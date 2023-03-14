import pandas as pd
from sklearn.linear_model import LinearRegression
from utils import analysis_utils


def process_daily_activity_data(df_daily_activity: pd.DataFrame, user_id: str = '1503960366') -> pd.DataFrame:
    '''
    Filter daily activity data by user_id and add columns for year, month, and day of week.

    Args:
    - df_daily_activity (pd.DataFrame): DataFrame containing daily activity data
    - user_id (str, optional): User ID to filter the data by (default: '1503960366')

    Returns:
    - df_daily_activity (pd.DataFrame): Filtered DataFrame with additional columns for year, month, and day of week
    '''
    df_daily_activity = analysis_utils.filter_df_user_id(df_daily_activity, user_id)
    
    df_daily_activity['ActivityDate'] = pd.to_datetime(df_daily_activity['ActivityDate'])
    df_daily_activity['year'] = df_daily_activity['ActivityDate'].dt.year
    df_daily_activity['month'] = df_daily_activity['ActivityDate'].dt.month
    df_daily_activity['dayofweek'] = df_daily_activity['ActivityDate'].dt.dayofweek

    return df_daily_activity


def daily_activity_calories_linreg_model(df: pd.DataFrame, x: str) -> LinearRegression:
    '''
    Create a linear regression model to predict calories burned based on a given feature.

    Args:
    - df (pd.DataFrame): DataFrame containing daily activity data
    - x (str): Feature to use as input to the model

    Returns:
    - linear_regressor (LinearRegression): Trained linear regression object
    '''
    i = df.loc[:, x].values.reshape(-1, 1)  # values converts it into a numpy array
    j = df.loc[:, 'Calories'].values.reshape(-1, 1)  # -1: calc dimensn of rows, but have 1 column
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(i, j)  # perform linear regression
    #Y_pred = linear_regressor.predict(X_)  # make predictions
    return linear_regressor