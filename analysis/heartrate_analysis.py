"""
Module to process and merge heart rate and sleep datasets.
"""
import pandas as pd
from utils import analysis_utils


def process_heartrate_data(df_heartrate, df_daily_sleep, user_id='2026352035'):
    """
    A method to process and merge the heart rate and sleep datasets
    :param df_heartrate: dataframe containing heart rate data
    :param df_daily_sleep: dataframe containing sleep information
    :param user_id: id of user to filter data for
    :return: merged dataset containing heart rate data on a seconds level and sleep information 
        on a daily level
    """

    # filter data by user_id
    df_heartrate = analysis_utils.filter_df_user_id(df_heartrate, user_id)
    df_daily_sleep = analysis_utils.filter_df_user_id(df_daily_sleep, user_id)

    # convert date_time column to datetime format
    df_heartrate['date_time'] = pd.to_datetime(
        df_heartrate['Time'], format="%m/%d/%Y %I:%M:%S %p")

    # arrange heart rate daily by taking mean of heart rate for each day
    heartrate_daily = df_heartrate.resample(
        '1D', on='date_time', origin='2016-04-12 00:00:00').Value.mean().reset_index()

    # convert date_time column to date format
    heartrate_daily['date_time'] = pd.to_datetime(
        heartrate_daily['date_time'], format="%Y/%m/%d")
    heartrate_daily['date'] = heartrate_daily['date_time'].dt.date
    heartrate_daily['day_of_week'] = heartrate_daily['date_time'].dt.day_name()

    # convert SleepDay column to datetime format
    df_daily_sleep['date_time'] = pd.to_datetime(
        df_daily_sleep['SleepDay'], format='%m/%d/%Y %I:%M:%S %p')
    df_daily_sleep['date'] = df_daily_sleep['date_time'].dt.date

    # merge datasets
    daily_values = heartrate_daily.merge(
        df_daily_sleep, how='left', on=['date'])
    daily_values = daily_values.rename(columns={"date_time_x": "date_time"})
    daily_values = daily_values.drop(columns=['date_time_y'])

    # categorize Sleep Duration column based on TotalMinutesAsleep
    daily_values['Sleep Duration'] = pd.cut(x=daily_values['TotalMinutesAsleep'], bins=[
                                            0, 393, 442, 503, 775], labels=['Less', 'Okay', 'Enough', 'Healthy'])

    return daily_values
