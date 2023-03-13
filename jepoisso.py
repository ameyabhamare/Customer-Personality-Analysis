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

from activity_and_weight_analysis import sleep_analysis, calories_analysis, steps_analysis
from utils import graph_utils


# load data
df_sleep_data_unproc = pd.read_csv("data/sleepDay_merged.csv")
df_daily_steps_unproc = pd.read_csv("data/dailySteps_merged.csv")
df_daily_calories_unproc = pd.read_csv("data/dailyCalories_merged.csv")

# process data
sleep_proc = sleep_analysis.process_sleep_analysis_data(df_sleep_data_unproc)
daily_steps_proc = steps_analysis.process_daily_steps_data(df_daily_steps_unproc)
daily_steps_sleep_proc = steps_analysis.process_daily_sleep_steps_data(df_daily_steps_unproc, df_sleep_data_unproc)
daily_calories_proc = calories_analysis.process_daily_calories_data(df_daily_calories_unproc)

# build graph viz
# sleep analysis
#graph_utils.create_barplot(x_axis=sleep_proc['SleepDate'], y_axis=sleep_proc['TotalTimeInBed'], color='r', xlabel='Date', ylabel='Minutes', title="Sleep activity analysis")
#graph_utils.create_barplot(x_axis=sleep_proc['SleepDate'], y_axis=sleep_proc['TotalMinutesAsleep'], color='b', xlabel='Date', ylabel='Minutes', title="Sleep activity analysis")

# daily steps analysis
#graph_utils.create_barplot(x_axis=daily_steps_proc['ActivityDay'], y_axis=daily_steps_proc['StepTotal'], xlabel='Date', ylabel='Daily steps', title='Daily steps analysis')

# daily sleep and steps analysis
#sleep_ax = graph_utils.create_barplot(x_axis=daily_steps_sleep_proc['ActivityDay'], y_axis=daily_steps_sleep_proc['TotalMinutesAsleep'], xlabel='Date', ylabel='Minutes asleep', title='Daily steps sleep analysis')
#graph_utils.create_lineplot(dat=daily_steps_sleep_proc['StepTotal'], ax=sleep_ax, marker='o', color='g')

# daily calories analysis
graph_utils.create_lineplot(data=daily_calories_proc, x='ActivityDay', y='Calories', marker='o', color='g')

# display viz
graph_utils.plt_show()