"""
This module spins up FitMe on localhost using the streamlit library
"""
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib
import tkinter
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from caloric_model.model import transform_dataframe

from analysis import sleep_analysis, calories_analysis, steps_analysis, heartrate_analysis
from utils import graph_utils

# if selected_dropdown == 'Heart Rate':
#     from heart_rate_analysis.heart_rate_analysis import create_final_df,\
#     plot_daily_heart_rate, plot_weekly_heart_rate, plot_bpm_density, plot_sleep_vs_bpm
#     daily_values = create_final_df()
#     plot_daily_heart_rate(daily_values, user_id = None)
#     plot_weekly_heart_rate(daily_values, user_id = None)
#     plot_bpm_density(daily_values, user_id = None)
#     plot_sleep_vs_bpm(daily_values, user_id = None)

# load data
df_heartrate_unproc = pd.read_csv('data/heartrate_seconds_merged.csv')
df_sleep_data_unproc = pd.read_csv("data/sleepDay_merged.csv")

# process data
heartrate_proc = heartrate_analysis.process_heartrate_data(df_heartrate_unproc, df_sleep_data_unproc)

# build graph viz
#graph_utils.create_lineplot(xlabel='Date', ylabel='Daily BPM', data=heartrate_proc, x='date_time', y='Value', title="Average daily BPM")
#graph_utils.plt_show()

#graph_utils.create_lineplot(xlabel='Date', ylabel='Weekly BPM', data=heartrate_proc, x='day_of_week', y='Value', title="Average weekly BPM")
#graph_utils.plt_show()

#graph_utils.create_kdeplot(heartrate_proc['Value'], xlabel='BPM', ylabel='Distribution', shade=True, legend=False, title="BPM Distribution")
#graph_utils.plt_show()

graph_utils.create_boxplot(data=heartrate_proc, x='Sleep Duration', y='Value', xlabel='Sleep duration in minutes', ylabel='BPM', title="Sleep quality analysis")
graph_utils.plt_show()

# def plot_sleep_vs_bpm(daily_values, user_id = None):
#     """
#     A method to generate a graph that displays
#     how the heart-rate relates to the duration of sleep
#     Arguments:
#         daily_values - The merged dataset containing heart rate
#                        and sleep information on a daily level
#         user_id (None: optional) - The user id
#     Returns:
#         None
#     """
#     if user_id is None:
#         user_id = '2026352035'
#     daily_values = daily_values.query(f"Id == {user_id}")
#     _, ax1 = plt.subplots(figsize = (12, 6))
#     ax1 = sns.boxplot(x = 'Sleep Duration', y = 'Value', data = daily_values, color = 'blue')
#     ax1.set(xlabel = 'Sleep duration in minutes')
#     ax1.set(ylabel = 'BPM')
#     plt.show()



# # load data
# df_sleep_data_unproc = pd.read_csv("data/sleepDay_merged.csv")
# df_daily_steps_unproc = pd.read_csv("data/dailySteps_merged.csv")
# df_daily_calories_unproc = pd.read_csv("data/dailyCalories_merged.csv")

# # process data
# sleep_proc = sleep_analysis.process_sleep_analysis_data(df_sleep_data_unproc)
# daily_steps_proc = steps_analysis.process_daily_steps_data(df_daily_steps_unproc)
# daily_steps_sleep_proc = steps_analysis.process_daily_sleep_steps_data(df_daily_steps_unproc, df_sleep_data_unproc)
# daily_calories_proc = calories_analysis.process_daily_calories_data(df_daily_calories_unproc)

# # build graph viz
# # sleep analysis
# #graph_utils.create_barplot(x_axis=sleep_proc['SleepDate'], y_axis=sleep_proc['TotalTimeInBed'], color='r', xlabel='Date', ylabel='Minutes', title="Sleep activity analysis")
# #graph_utils.create_barplot(x_axis=sleep_proc['SleepDate'], y_axis=sleep_proc['TotalMinutesAsleep'], color='b', xlabel='Date', ylabel='Minutes', title="Sleep activity analysis")

# # daily steps analysis
# #graph_utils.create_barplot(x_axis=daily_steps_proc['ActivityDay'], y_axis=daily_steps_proc['StepTotal'], xlabel='Date', ylabel='Daily steps', title='Daily steps analysis')

# # daily sleep and steps analysis
# #sleep_ax = graph_utils.create_barplot(x_axis=daily_steps_sleep_proc['ActivityDay'], y_axis=daily_steps_sleep_proc['TotalMinutesAsleep'], xlabel='Date', ylabel='Minutes asleep', title='Daily steps sleep analysis')
# #graph_utils.create_lineplot(dat=daily_steps_sleep_proc['StepTotal'], ax=sleep_ax, marker='o', color='g')

# # daily calories analysis
# graph_utils.create_lineplot(data=daily_calories_proc, x='ActivityDay', y='Calories', marker='o', color='g')

# # display viz
# graph_utils.plt_show()