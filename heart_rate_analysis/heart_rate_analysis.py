'''
This module reads in the daily_values.csv files and displays relvant visualizations
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_daily_heart_rate(daily_values, user_id = None):
    '''
    A method to generate a graph between sleep time v/s time in bed.
    Args:
    df_sleep_data - Dataframe containing the time in bed and total sleep time columns.
    user_id (None: optional) - The user-id of the user.

    Return:
    df_sleep_data - The processed sleep dataframe.
    '''
    if user_id is None:
        user_id = '2026352035'
    daily_values = daily_values.query(f"Id == {user_id}")
    _, ax1 = plt.subplots(figsize = (12,6))
    ax1 = sns.lineplot(x = 'date_time', y = 'Value', data = daily_values, palette = 'bright')
    ax1.set(xlabel = 'Date')
    ax1.set(ylabel = 'bpm')
    ax1.plot()
    plt.show()
    
def plot_weekly_heart_rate(daily_values, user_id = None):
    '''
    A method to generate a graph between sleep time v/s time in bed.
    Args:
    df_sleep_data - Dataframe containing the time in bed and total sleep time columns.
    user_id (None: optional) - The user-id of the user.

    Return:
    df_sleep_data - The processed sleep dataframe.
    '''
    if user_id is None:
        user_id = '2026352035'
    daily_values = daily_values.query(f"Id == {user_id}")
    _, ax1 = plt.subplots(figsize = (12, 6))
    ax1 = sns.lineplot(x = 'day_of_week', y = 'Value', data = daily_values, palette = 'bright')
    ax1.set(xlabel = 'Day of the week')
    ax1.plot()
    plt.show()

def plot_bpm_density(daily_values, user_id = None):
    '''
    A method to generate a graph between sleep time v/s time in bed.
    Args:
    df_sleep_data - Dataframe containing the time in bed and total sleep time columns.
    user_id (None: optional) - The user-id of the user.

    Return:
    df_sleep_data - The processed sleep dataframe.
    '''
    if user_id is None:
        user_id = '2026352035'
    daily_values = daily_values.query(f"Id == {user_id}")
    _, ax1 = plt.subplots(figsize = (12, 6))
    ax1 = sns.kdeplot(daily_values['Value'], shade = True, legend = False)
    ax1.set(xlabel = 'BPM')
    ax1.set(ylabel = 'Distribution')
    ax1.plot()
    plt.show()
    
def plot_sleep_vs_bpm(daily_values, user_id = None):
    '''
    A method to generate a graph between sleep time v/s time in bed.
    Args:
    df_sleep_data - Dataframe containing the time in bed and total sleep time columns.
    user_id (None: optional) - The user-id of the user.

    Return:
    df_sleep_data - The processed sleep dataframe.
    '''
    if user_id is None:
        user_id = '2026352035'
    daily_values = daily_values.query(f"Id == {user_id}")
    _, ax1 = plt.subplots(figsize = (12, 6))
    ax1 = sns.boxplot(x = 'Sleep Duration', y = 'Value', data = daily_values, color = 'blue')
    ax1.set(xlabel = 'Sleep duration in minutes')
    ax1.set(ylabel = 'BPM')
    plt.show()
    
def create_final_df(df_heartrate_seconds, df_daily_sleep):
    '''
    A method to generate a graph between sleep time v/s time in bed.
    Args:
    df_sleep_data - Dataframe containing the time in bed and total sleep time columns.
    user_id (None: optional) - The user-id of the user.

    Return:
    df_sleep_data - The processed sleep dataframe.
    '''
    df_heartrate_seconds['date_time'] = pd.to_datetime(heartrate_seconds['Time'], 
                                                    format = "%m/%d/%Y %I:%M:%S %p")
    heartrate_daily = heartrate_seconds.groupby('Id').resample(
        '1D', on = 'date_time', origin = '2016-04-12 07:21:00').Value.mean().reset_index()
    heartrate_daily['date_time'] = pd.to_datetime(heartrate_daily['date_time'], 
                                                  format = "%m/%d/%Y %I:%M:%S %p")
    heartrate_daily['date_time'] = heartrate_daily['date_time'].dt.date
    heartrate_daily['date_time'] = pd.to_datetime(heartrate_daily['date_time'], 
                                                  format = "%Y/%m/%d")
    heartrate_daily['day_of_week'] = heartrate_daily['date_time'].dt.day_name()
    df_daily_sleep['date_time'] = pd.to_datetime(daily_sleep['SleepDay'], 
                                              format = '%m/%d/%Y %I:%M:%S %p')
    daily_values = heartrate_daily.merge(daily_sleep, how = 'left', on = ['Id', 'date_time'])
    daily_values['Sleep Duration'] = pd.cut(x = daily_values['TotalMinutesAsleep'],
                                            bins = [0, 393, 442, 503, 775],
                                            labels = ['Less', 'Okay', 'Enough', 'Healthy'])
    return daily_values

if __name__ == '__main__':
    heartrate_seconds = pd.read_csv("../database/heartrate_seconds_merged.csv")
    daily_sleep = pd.read_csv("../database/sleepDay_merged.csv")
    df_final_proc = create_final_df(heartrate_seconds, daily_sleep)   
    plot_daily_heart_rate(df_final_proc, user_id = None)
    plot_weekly_heart_rate(df_final_proc, user_id = None)
    plot_bpm_density(df_final_proc, user_id = None)
    plot_sleep_vs_bpm(df_final_proc, user_id = None)
    