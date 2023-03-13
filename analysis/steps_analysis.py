import pandas as pd
from utils import analysis_utils
from . import sleep_analysis

def process_daily_steps_data(df_daily_steps, user_id='1503960366'):
    """
    A method to generate a graph for daily step pattern.
    Args:
    df_daily_steps - Dataframe containing the number of steps taken by the user everyday.
    user_id (None: optional) - The user-id of the user.

    Return:
    df_daily_steps - The processed steps dataframe.
    """
    df_daily_steps = analysis_utils.filter_df_user_id(df_daily_steps, user_id)
    return df_daily_steps

def process_daily_sleep_steps_data(df_daily_steps, df_daily_sleep, user_id='1503960366'):
    """
    A method to generate a graph between sleep time v/s step count.
    Args:
    df_daily_steps - Dataframe containing the step data.
    df_daily_sleep - Dataframe containing the sleep data.
    user_id (None: optional) - The user-id of the user.

    Return:
    df_merged - A merged dataframe containing the step count and sleep duration data.
    """
    df_daily_steps = analysis_utils.filter_df_user_id(df_daily_steps, user_id)
    df_daily_sleep = analysis_utils.filter_df_user_id(df_daily_sleep, user_id)
    
    df_sleep_proc = sleep_analysis.process_sleep_analysis_data(df_daily_sleep, user_id=user_id)

    # merge both data set (inner join) with sleep data
    df_merged = pd.merge(df_daily_steps, df_sleep_proc, how='inner', left_on='ActivityDay', right_on='SleepDate')
    df_merged = df_merged.drop(columns=['SleepDate'])
    return df_merged
