import pandas as pd
from sklearn.linear_model import LinearRegression
from utils import analysis_utils

def process_daily_calories_data(df_daily_calories, user_id='1503960366'):
    df_daily_calories = analysis_utils.filter_df_user_id(df_daily_calories, user_id)
    return df_daily_calories