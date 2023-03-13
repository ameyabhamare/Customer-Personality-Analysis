"""
This module spins up FitMe on localhost using the streamlit library
"""
import streamlit as st
import pandas as pd

from analysis import sleep_analysis, calories_analysis, steps_analysis, heartrate_analysis, activity_analysis
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
    # df = pd.read_csv(file_path)
    
# Heart rate analysis
if selected_dropdown == 'Heart Rate':
    # load data
    df_heartrate_unproc = pd.read_csv('data/heartrate_seconds_merged.csv')
    df_sleep_data_unproc = pd.read_csv("data/sleepDay_merged.csv")

    # process data
    heartrate_proc = heartrate_analysis.process_heartrate_data(df_heartrate_unproc, df_sleep_data_unproc)

    # daily bpm
    fig_daily_bpm, ax_daily_bpm = graph_utils.create_fig()
    graph_utils.create_lineplot(ax=ax_daily_bpm, xlabel='Date', ylabel='Daily BPM', data=heartrate_proc, x='date_time', y='Value', title="Average daily BPM")
    
    # weekly bpm
    fig_weekly_bpm, ax_weekly_bpm = graph_utils.create_fig()
    graph_utils.create_lineplot(ax=ax_weekly_bpm, xlabel='Date', ylabel='Weekly BPM', data=heartrate_proc, x='day_of_week', y='Value', title="Average weekly BPM")

    # bpm density
    fig_density_bpm, ax_density_bpm = graph_utils.create_fig()
    graph_utils.create_kdeplot(heartrate_proc['Value'], ax=ax_density_bpm, xlabel='BPM', ylabel='Distribution', shade=True, legend=False, title="BPM Distribution")

    # box plot bpm
    fig_box_plot_bpm, ax_box_plot_bpm = graph_utils.create_fig()
    graph_utils.create_boxplot(ax=ax_box_plot_bpm, data=heartrate_proc, x='Sleep Duration', y='Value', xlabel='Sleep duration in minutes', ylabel='BPM', title="Sleep quality analysis")

    st.pyplot(fig_daily_bpm)
    st.pyplot(fig_weekly_bpm)
    st.pyplot(fig_density_bpm)
    st.pyplot(fig_box_plot_bpm)
    
    
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

    # sleep analysis
    fig_sleep, ax_sleep = graph_utils.create_fig()
    graph_utils.create_barplot(ax=ax_sleep, x_axis=sleep_proc['SleepDate'], y_axis=sleep_proc['TotalTimeInBed'], color='r', xlabel='Date', ylabel='Minutes', title="Sleep activity analysis")
    graph_utils.create_barplot(ax=ax_sleep, x_axis=sleep_proc['SleepDate'], y_axis=sleep_proc['TotalMinutesAsleep'], color='b', xlabel='Date', ylabel='Minutes', title="Sleep activity analysis")

    # daily steps analysis
    fig_daily_steps, ax_daily_steps = graph_utils.create_fig()
    graph_utils.create_barplot(ax=ax_daily_steps, x_axis=daily_steps_proc['ActivityDay'], y_axis=daily_steps_proc['StepTotal'], xlabel='Date', ylabel='Daily steps', title='Daily steps analysis')

    # daily sleep and steps analysis
    fig_sleep_steps, ax_sleep_steps = graph_utils.create_fig()
    graph_utils.create_barplot(ax=ax_sleep_steps, x_axis=daily_steps_sleep_proc['ActivityDay'], y_axis=daily_steps_sleep_proc['TotalMinutesAsleep'], xlabel='Date', ylabel='Minutes asleep', title='Daily steps sleep analysis')
    graph_utils.create_lineplot(dat=daily_steps_sleep_proc['StepTotal'], ax=ax_sleep_steps, marker='o', color='g')

    # daily calories analysis
    fig_cals, ax_cals = graph_utils.create_fig()
    graph_utils.create_lineplot(ax=ax_cals, data=daily_calories_proc, x='ActivityDay', y='Calories', marker='o', color='g')

    st.pyplot(fig_sleep)
    st.pyplot(fig_daily_steps)
    st.pyplot(fig_sleep_steps)
    st.pyplot(fig_cals)

if selected_dropdown == 'Caloric Model':
    # load data
    df_daily_activity_unproc = pd.read_csv("data/dailyActivity_merged.csv")

    dropdown_c_options = ['VeryActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes', 'ModeratelyActiveDistance', 'VeryActiveDistance', 'SedentaryActiveDistance']
    selected_c_dropdown = st.selectbox("Select Variable", options = dropdown_c_options)
    slider_val = st.slider(selected_c_dropdown, min(df_daily_activity_unproc[selected_c_dropdown]), max(df_daily_activity_unproc[selected_c_dropdown]), 1)

    # process data
    df_daily_activity_proc = activity_analysis.process_daily_activity_data(df_daily_activity_unproc)

    sns.regplot(data = df_daily_activity_proc, x = selected_c_dropdown, y = 'Calories')
    st.pyplot(fig)
    lr = activity_analysis.daily_activity_calories_linreg_model(df_daily_activity_proc, selected_c_dropdown)
    st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(f'<p class="big-font">Model Daily Caloric: {round(lr.predict([[slider_val]])[0][0], 2)}</p>', unsafe_allow_html=True)
