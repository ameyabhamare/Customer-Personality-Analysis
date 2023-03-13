import pandas as pd
from utils import analysis_utils

def process_heartrate_data(df_heartrate, df_daily_sleep, user_id = '2026352035'):
    """
    A method to process and merge the heart rate and sleep datasets
    Arguments:
        None
    Returns:
        A merged dataset containing heart rate data on a seconds level 
        and sleep information on a daily level
    """
    df_heartrate = analysis_utils.filter_df_user_id(df_heartrate, user_id)
    df_daily_sleep = analysis_utils.filter_df_user_id(df_daily_sleep, user_id)

    df_heartrate['date_time'] = pd.to_datetime(df_heartrate['Time'], format = "%m/%d/%Y %I:%M:%S %p")

    # arrange heartrate daily
    heartrate_daily = df_heartrate.resample('1D', on = 'date_time', origin = '2016-04-12 07:21:00').Value.mean().reset_index()

    heartrate_daily['date_time'] = pd.to_datetime(heartrate_daily['date_time'], format = "%m/%d/%Y %I:%M:%S %p")
    heartrate_daily['date_time'] = heartrate_daily['date_time'].dt.date
    heartrate_daily['date_time'] = pd.to_datetime(heartrate_daily['date_time'], format = "%Y/%m/%d")
    heartrate_daily['day_of_week'] = heartrate_daily['date_time'].dt.day_name()

    # # arrange daily sleep
    df_daily_sleep['date_time'] = pd.to_datetime(df_daily_sleep['SleepDay'], format = '%m/%d/%Y %I:%M:%S %p')

    # merge datasets
    daily_values = heartrate_daily.merge(df_daily_sleep, how = 'left', on = ['date_time'])
    daily_values['Sleep Duration'] = pd.cut(x = daily_values['TotalMinutesAsleep'], bins = [0, 393, 442, 503, 775], labels = ['Less', 'Okay', 'Enough', 'Healthy'])

    return daily_values
    