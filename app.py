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

from activity_and_weight_analysis import sleep_analysis
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
    from heart_rate_analysis.heart_rate_analysis import create_final_df,\
    plot_daily_heart_rate, plot_weekly_heart_rate, plot_bpm_density, plot_sleep_vs_bpm
    daily_values = create_final_df()
    plot_daily_heart_rate(daily_values, user_id = None)
    plot_weekly_heart_rate(daily_values, user_id = None)
    plot_bpm_density(daily_values, user_id = None)
    plot_sleep_vs_bpm(daily_values, user_id = None)
    
# Activity and weight analysis
if selected_dropdown == 'Activity & Weight':
    # load data
    df_sleep_data_unproc = pd.read_csv("data/sleepDay_merged.csv")
    df_daily_steps_unproc = pd.read_csv("data/dailySteps_merged.csv")
    df_daily_calories_unproc = pd.read_csv("data/dailyCalories_merged.csv")

    # process data
    sleep_proc = sleep_analysis.process_sleep_analysis_data(df_sleep_data_unproc)

    # build graph viz
    graph_utils.create_barplot(x_axis=sleep_proc['SleepDate'], y_axis=sleep_proc['TotalTimeInBed'], color='r', xlabel='Date', ylabel='Minutes')
    graph_utils.create_barplot(x_axis=sleep_proc['SleepDate'], y_axis=sleep_proc['TotalMinutesAsleep'], color='r', xlabel='Date', ylabel='Minutes')

    # display viz
    graph_utils.plt_show()
    
    # df_sleep_data_proc = plot_sleep_time_vs_time_in_bed(df_sleep_data_unproc, '1503960366')
    # df_daily_steps_proc = plot_daily_step_pattern(df_daily_steps_unproc, user_id=None)
    # df_sleep_and_steps_merged = pd.merge(df_daily_steps_proc, df_sleep_data_proc, how='inner',
    #                                 left_on='ActivityDay', right_on='SleepDate')
    # plot_daily_sleep_vs_step_count(df_sleep_and_steps_merged)
    # df_daily_calories_proc = plot_daily_calories_pattern(df_daily_calories_unproc, user_id=None)

if selected_dropdown == 'Caloric Model':
    from caloric_model.model import model_pipeline
    dropdown_c_options = ['VeryActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes', 'ModeratelyActiveDistance', 'VeryActiveDistance', 'SedentaryActiveDistance']
    selected_c_dropdown = st.selectbox("Select Variable", options = dropdown_c_options)
    slider_val = st.slider(selected_c_dropdown, min(df[selected_c_dropdown]), max(df[selected_c_dropdown]), 1)
    fig = plt.figure(figsize=(15, 8))
    sns.regplot(data = df, x= selected_c_dropdown, y = 'Calories')
    st.pyplot(fig)
    lr = model_pipeline(df, selected_c_dropdown)
    st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(f'<p class="big-font">Model Daily Caloric: {round(lr.predict([[slider_val]])[0][0], 2)}</p>', unsafe_allow_html=True)
