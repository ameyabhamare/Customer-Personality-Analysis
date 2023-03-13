import pandas as pd
from sklearn.linear_model import LinearRegression
from utils import analysis_utils

def process_daily_calories_data(df_daily_calories, user_id='1503960366'):
    """
    Filter daily calories data by user id and return the filtered dataframe.
    
    Args:
        df_daily_calories (pandas.DataFrame): Dataframe containing daily calories data.
        user_id (str): User id to filter the dataframe by.
    
    Returns:
        pandas.DataFrame: Filtered dataframe.
    """
    df_daily_calories = analysis_utils.filter_df_user_id(df_daily_calories, user_id)
    return df_daily_calories