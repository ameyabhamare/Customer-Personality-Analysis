import streamlit as st
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

from heart_rate_analysis.viz import create_final_df, plot_daily_heart_rate, plot_weekly_heart_rate, plot_bpm_density, plot_sleep_vs_bpm
from activity_and_weight_analysis.activity_and_weight_analysis import plot_sleep_time_vs_time_in_bed, plot_daily_step_pattern, plot_daily_sleep_vs_step_count, plot_daily_calories_pattern
import sys
sys.path.insert(0, 'heart_rate_analysis')
sys.path.insert(1, 'activity_and_weight_analysis')

st.title("FitMe")
st.markdown("Fitness Explorer. This app performs health analysis based on fitness tracking data")
files = st.sidebar.file_uploader("Please choose a csv file", accept_multiple_files = True)
dropdown_options = ['Heart Rate', 'Activity & Weight', 'Caloric Model']
selected_dropdown = st.sidebar.selectbox("Select Analysis", options = dropdown_options)

#Add new features/columns to the dataframs
def transform_dataframe(df):
    df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])
    df['year'] = df['ActivityDate'].dt.year
    df['month'] = df['ActivityDate'].dt.month
    df['dayofweek'] = df['ActivityDate'].dt.dayofweek
    df['dayofweek'] = df['dayofweek'].map({0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun' })
    return df

#This function is for the caloric model module
def model_pipline():
    pass

#This function is for the caloric model module
def daily_caloric_model():
    pass

#Processing multiple files in the user selection dropdown
for file_ in files:
        file_name = file_.name
        file_path = f'../data/{file_name}'
        df = pd.read_csv(file_path)
        df = transform_dataframe(df)

# Heart rate analysis
if selected_dropdown == 'Heart Rate':
    '''
    if files is not None:
        fig = plt.figure(figsize=(15, 8))
        try:
            sns.lineplot(data = df , y = 'Calories', x = 'dayofweek')
        except NameError as e:
            st.write("Heart Rate file not uploaded correctly")
        st.pyplot(fig)
    '''
    heartrate_seconds = pd.read_csv("database/heartrate_seconds_merged.csv")
    daily_sleep = pd.read_csv("database/sleepDay_merged.csv")
    df_final_proc = create_final_df(heartrate_seconds, daily_sleep)
    plot_daily_heart_rate(df_final_proc, user_id = None)
    plot_weekly_heart_rate(df_final_proc, user_id = None)
    plot_bpm_density(df_final_proc, user_id = None)
    plot_sleep_vs_bpm(df_final_proc, user_id = None)
    

if selected_dropdown == 'Activity & Weight':
    df_sleep_data_unproc = pd.read_csv("database/sleepDay_merged.csv")
    df_daily_steps_unproc = pd.read_csv("database/dailySteps_merged.csv")
    df_daily_calories_unproc = pd.read_csv("database/dailyCalories_merged.csv")
    df_sleep_data_proc = plot_sleep_time_vs_time_in_bed(df_sleep_data_unproc, '1503960366')
    df_daily_steps_proc = plot_daily_step_pattern(df_daily_steps_unproc, user_id=None)
    df_sleep_and_steps_merged = pd.merge(df_daily_steps_proc, df_sleep_data_proc, how='inner',
                                    left_on='ActivityDay', right_on='SleepDate')
    plot_daily_sleep_vs_step_count(df_sleep_and_steps_merged)
    df_daily_calories_proc = plot_daily_calories_pattern(df_daily_calories_unproc, user_id=None)

if selected_dropdown == 'Caloric Model':
    st.slider('Feature 1', 0, 10, 1)
    st.slider('Feature 2', 0, 10, 1)
    st.slider('Feature 3', 0, 10, 1)
    st.slider('Feature 4', 0, 10, 1)
    st.write("Model Daily Caloric: ")