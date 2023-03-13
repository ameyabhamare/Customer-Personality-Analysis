"""
This module reads in datasets, merges them and displays relevant visualizations
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def plot_daily_heart_rate(daily_values, user_id = None):
    '''
    A method to generate a graph that displays how heart rate varies day-over-day
    Arguments:
        daily_values - The merged dataset containing
                       heart rate and sleep information on a daily level
        user_id (None: optional) - The user id
    Returns:
        None
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
    A method to generate a graph that displays how heart rate varies across days of the week
    Arguments:
        daily_values - The merged dataset containing heart rate and
                       sleep information on a daily level
        user_id (None: optional) - The user id
    Returns:
        None
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
    """
    A method to generate a graph that displays the density of bpm
    across the time duration that the dataset spans
    Arguments:
        daily_values - The merged dataset containing heart rate and
                       sleep information on a daily level
        user_id (None: optional) - The user id
    Returns:
        None
    """
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
    """
    A method to generate a graph that displays
    how the heart-rate relates to the duration of sleep
    Arguments:
        daily_values - The merged dataset containing heart rate
                       and sleep information on a daily level
        user_id (None: optional) - The user id
    Returns:
        None
    """
    if user_id is None:
        user_id = '2026352035'
    daily_values = daily_values.query(f"Id == {user_id}")
    _, ax1 = plt.subplots(figsize = (12, 6))
    ax1 = sns.boxplot(x = 'Sleep Duration', y = 'Value', data = daily_values, color = 'blue')
    ax1.set(xlabel = 'Sleep duration in minutes')
    ax1.set(ylabel = 'BPM')
    plt.show()
    
def create_final_df():
    """
    A method to process and merge the heart rate and sleep datasets
    Arguments:
        None
    Returns:
        A merged dataset containing heart rate data on a seconds level 
        and sleep information on a daily level
    """
    heartrate_seconds = pd.read_csv('heart_rate_analysis/tests/mock_data/heartrate_seconds_merged.csv')
    daily_sleep = pd.read_csv('heart_rate_analysis/tests/mock_data/sleepDay_merged.csv')
    heartrate_seconds['date_time'] = pd.to_datetime(heartrate_seconds['Time'],
                                                    format = "%m/%d/%Y %I:%M:%S %p")
    heartrate_daily = heartrate_seconds.groupby('Id').resample(
        '1D', on = 'date_time', origin = '2016-04-12 07:21:00').Value.mean().reset_index()
    heartrate_daily['date_time'] = pd.to_datetime(heartrate_daily['date_time'],
                                                  format = "%m/%d/%Y %I:%M:%S %p")
    heartrate_daily['date_time'] = heartrate_daily['date_time'].dt.date
    heartrate_daily['date_time'] = pd.to_datetime(heartrate_daily['date_time'],
                                                  format = "%Y/%m/%d")
    heartrate_daily['day_of_week'] = heartrate_daily['date_time'].dt.day_name()
    daily_sleep['date_time'] = pd.to_datetime(daily_sleep['SleepDay'],
                                              format = '%m/%d/%Y %I:%M:%S %p')
    daily_values = heartrate_daily.merge(daily_sleep, how = 'left', on = ['Id', 'date_time'])
    daily_values['Sleep Duration'] = pd.cut(x = daily_values['TotalMinutesAsleep'],
                                            bins = [0, 393, 442, 503, 775],
                                            labels = ['Less', 'Okay', 'Enough', 'Healthy'])
    return daily_values
    