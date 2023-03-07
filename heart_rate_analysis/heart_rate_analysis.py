'''This module reads in the daily_values.csv files and displays relvant visualizations'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
daily_values = pd.read_csv('C:/AMEYA/UW/Academics/DATA 515/Project/FitMe/\
                           heart_rate_analysis/data/daily_values.csv')
'''







sns.boxplot(x = 'Sleep Duration', y = 'Value', data = daily_values, color = 'blue')
plt.xticks(rotation = 45, ha = 'right')
plt.show()


def plot_daily_heart_rate(daily_values, user_id = None):
    if user_id is None:
        user_id = '2026352035'
    daily_values = daily_values.query(f"Id == {user_id}")
    _, ax1 = plt.subplots(figsize = (12,6))
    ax1 = sns.lineplot(x = 'date_time', y = 'Value', data = daily_values, palette = 'bright')
    ax1.set(xlabel = 'Date')
    ax1.set(ylabel = 'bpm')
    ax1.set_xticklabels(labels = daily_values['date_time'], size = 6, rotation = 30)
    ax1.plot()
    plt.show()
    
def plot_weekly_heart_rate(df, user_id = None):
    if user_id is None:
        user_id = '2026352035'
    daily_values = daily_values.query(f"Id == {user_id}")
    _, ax1 = plt.subplots(figsize = (12, 6))
    ax1 = sns.lineplot(x = 'day_of_week', y = 'Value', data = daily_values, palette = 'bright')
    ax1.set(xlabel = 'Day of the week')
    ax1.plot()
    plt.show()

def plot_bpm_density(df, user_id = None):
    if user_id is None:
        user_id = '2026352035'
    daily_values = daily_values.query(f"Id == {user_id}")
    _, ax1 = plt.subplots(figsize = (12, 6))
    ax1 = sns.kdeplot(daily_values['Value'], shade = True, legend = False)
    ax1.set(xlabel = 'BPM')
    ax1.set(ylabel = 'Distribution')
    ax1.plot()
    plt.show()
    

def plot_sleep_vs_bpm(df, user_id = None):


    
def create_final_df(heartrate_seconds, daily_sleep):
    heartrate_seconds['date_time'] = pd.to_datetime(heartrate_seconds['Time'], format = "%m/%d/%Y %I:%M:%S %p")
    heartrate_daily = heartrate_seconds.groupby('Id').resample('1D', on = 'date_time', origin = '2016-04-12 07:21:00').Value.mean().reset_index()
    heartrate_daily['date_time'] = pd.to_datetime(heartrate_daily['date_time'], format = "%m/%d/%Y %I:%M:%S %p")
    heartrate_daily['date_time'] = heartrate_daily['date_time'].dt.date
    heartrate_daily['date_time'] = pd.to_datetime(heartrate_daily['date_time'], format = "%Y/%m/%d")
    
    daily_sleep['date_time'] = pd.to_datetime(daily_sleep['SleepDay'], format = '%m/%d/%Y %I:%M:%S %p')
    daily_values = heartrate_daily.merge(daily_sleep, how = 'left', on = ['Id', 'date_time'])
    
    return daily_values
    
if __name__ == '__main__':
    heartrate_seconds = pd.read_csv("../database/heartrate_seconds_merged.csv")
    daily_sleep = pd.read_csv("../database/sleepDay_merged.csv")
    df_final_proc = create_final_df(heartrate_seconds, daily_sleep)
    
    
    
    
    