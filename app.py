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

from activity_and_weight_analysis import sleep_analysis, calories_analysis, steps_analysis, heartrate_analysis
from utils import graph_utils

st.title("FitMe")
st.markdown("Fitness Explorer. This app performs health analysis based on fitness tracking data")
dropdown_options = ['Heart Rate', 'Activity & Weight', 'Caloric Model']
selected_dropdown = st.sidebar.selectbox("Select Analysis", options = dropdown_options)
files = st.sidebar.file_uploader("Please choose a csv file", accept_multiple_files = True)

#Processing multiple files in the user selection dropdown
for file_ in files:
    file_name = file_.name
    file_path = f'data/{file_name}'
    df = pd.read_csv(file_path)
    df = transform_dataframe(df)
    
# Heart rate analysis
if selected_dropdown == 'Heart Rate':
    # load data
    df_heartrate_unproc = pd.read_csv('data/heartrate_seconds_merged.csv')
    df_sleep_data_unproc = pd.read_csv("data/sleepDay_merged.csv")

    # process data
    heartrate_proc = heartrate_analysis.process_heartrate_data(df_heartrate_unproc, df_sleep_data_unproc)

    # build graph viz
    # daily bpm
    graph_utils.create_lineplot(xlabel='Date', ylabel='Daily BPM', data=heartrate_proc, x='date_time', y='Value', title="Average daily BPM")
    graph_utils.plt_show()

    # weekly bpm
    graph_utils.create_lineplot(xlabel='Date', ylabel='Weekly BPM', data=heartrate_proc, x='day_of_week', y='Value', title="Average weekly BPM")
    graph_utils.plt_show()

    # bpm density
    graph_utils.create_kdeplot(heartrate_proc['Value'], xlabel='BPM', ylabel='Distribution', shade=True, legend=False, title="BPM Distribution")
    graph_utils.plt_show()

    # box plot bpm
    graph_utils.create_boxplot(data=heartrate_proc, x='Sleep Duration', y='Value', xlabel='Sleep duration in minutes', ylabel='BPM', title="Sleep quality analysis")
    graph_utils.plt_show()
    
# Activity and weight analysis
if selected_dropdown == 'Activity & Weight':
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
    graph_utils.create_barplot(x_axis=sleep_proc['SleepDate'], y_axis=sleep_proc['TotalTimeInBed'], color='r', xlabel='Date', ylabel='Minutes', title="Sleep activity analysis")
    graph_utils.create_barplot(x_axis=sleep_proc['SleepDate'], y_axis=sleep_proc['TotalMinutesAsleep'], color='b', xlabel='Date', ylabel='Minutes', title="Sleep activity analysis")
    graph_utils.plt_show() # display

    # daily steps analysis
    graph_utils.create_barplot(x_axis=daily_steps_proc['ActivityDay'], y_axis=daily_steps_proc['StepTotal'], xlabel='Date', ylabel='Daily steps', title='Daily steps analysis')
    graph_utils.plt_show() # display

    # daily sleep and steps analysis
    sleep_ax = graph_utils.create_barplot(x_axis=daily_steps_sleep_proc['ActivityDay'], y_axis=daily_steps_sleep_proc['TotalMinutesAsleep'], xlabel='Date', ylabel='Minutes asleep', title='Daily steps sleep analysis')
    graph_utils.create_lineplot(dat=daily_steps_sleep_proc['StepTotal'], ax=sleep_ax, marker='o', color='g')
    graph_utils.plt_show() # display

    # daily calories analysis
    graph_utils.create_lineplot(data=daily_calories_proc, x='ActivityDay', y='Calories', marker='o', color='g')
    graph_utils.plt_show() # display

if selected_dropdown == 'Caloric Model':
    dropdown_c_options = ['VeryActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes', 'ModeratelyActiveDistance', 'VeryActiveDistance', 'SedentaryActiveDistance']
    selected_c_dropdown = st.selectbox("Select Variable", options = dropdown_c_options)
    slider_val = st.slider(selected_c_dropdown, min(df[selected_c_dropdown]), max(df[selected_c_dropdown]), 1)

    # load data
    df_daily_calories_unproc = pd.read_csv("data/dailyCalories_merged.csv")

    # process data
    daily_calories_proc = calories_analysis.process_daily_calories_data(df_daily_calories_unproc)

    sns.regplot(data = daily_calories_proc, x = selected_c_dropdown, y = 'Calories')
    st.pyplot(fig)
    lr = calories_analysis.calories_linreg_model(df, selected_c_dropdown)
    st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(f'<p class="big-font">Model Daily Caloric: {round(lr.predict([[slider_val]])[0][0], 2)}</p>', unsafe_allow_html=True)
