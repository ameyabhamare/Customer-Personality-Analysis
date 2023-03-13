import pandas as pd
from . import sleep_analysis
from utils import analysis_utils

def process_daily_steps_data(df_daily_steps, user_id='1503960366'):
    """
    A method to generate a graph for daily step pattern.
    Args:
    df_daily_steps - Dataframe containing the number of steps taken by the user everyday.
    user_id (None: optional) - The user-id of the user.

    Return:
    df_sleep_data - The processed steps dataframe.
    """
    df_daily_steps = analysis_utils.filter_df_user_id(df_daily_steps, user_id)
    return df_daily_steps

def process_daily_sleep_steps_data(df_daily_steps, df_daily_sleep, user_id='1503960366'):
    # df_sleep_and_steps_merged = pd.merge(df_daily_steps_proc, df_sleep_data_proc, how='inner',
    #                                 left_on='ActivityDay', right_on='SleepDate')
    """
    A method to generate a graph between sleep time v/s step count.
    Args:
    df_sleep_data - Dataframe containing the sleep data merged with number of steps everyday.
    user_id (None: optional) - The user-id of the user.

    Return:
    None
    """
    df_daily_steps = analysis_utils.filter_df_user_id(df_daily_steps, user_id)
    df_daily_sleep = analysis_utils.filter_df_user_id(df_daily_sleep, user_id)
    
    df_sleep_proc = sleep_analysis.process_sleep_analysis_data(df_daily_sleep, user_id=user_id)

    # merge both data set (inner join) with sleep data
    df_merged = pd.merge(df_daily_steps, df_sleep_proc, how='inner', left_on='ActivityDay', right_on='SleepDate')
    df_merged = df_merged.drop(columns=['SleepDate'])
    return df_merged