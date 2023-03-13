import pandas as pd
from sklearn.linear_model import LinearRegression
from utils import analysis_utils

def process_daily_calories_data(df_daily_calories, user_id='1503960366'):
    df_daily_calories = analysis_utils.filter_df_user_id(df_daily_calories, user_id)
    day_mapping = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun' }

    df_daily_calories['ActivityDate'] = pd.to_datetime(df_daily_calories['ActivityDate'])
    df_daily_calories['year'] = df_daily_calories['ActivityDate'].dt.year
    df_daily_calories['month'] = df_daily_calories['ActivityDate'].dt.month
    df_daily_calories['dayofweek'] = df_daily_calories['ActivityDate'].map(lambda v: day_mapping[v.dt.dayofweek])

    return df_daily_calories