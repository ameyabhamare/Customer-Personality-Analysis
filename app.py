import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import matplotlib
import tkinter
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from activity_and_weight_analysis.activity_and_weight_analysis import *
from heart_rate_analysis.heart_rate_analysis import *

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
def model_pipeline(df, x, y):
    X = df.loc[:, x].values.reshape(-1, 1)  # values converts it into a numpy array
    Y = df.loc[:, 'Calories'].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(X, Y)  # perform linear regression
    #Y_pred = linear_regressor.predict(X)  # make predictions
    return linear_regressor

#Processing multiple files in the user selection dropdown
for file_ in files:
    file_name = file_.name
    file_path = f'data/{file_name}'
    df = pd.read_csv(file_path)
    df = transform_dataframe(df)
        
# Heart rate analysis
if selected_dropdown == 'Heart Rate':             
    daily_values = create_final_df()
    plot_daily_heart_rate(daily_values, user_id = None)
    plot_weekly_heart_rate(daily_values, user_id = None)
    plot_bpm_density(daily_values, user_id = None)
    plot_sleep_vs_bpm(daily_values, user_id = None)
        
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
    dropdown_c_options = ['VeryActiveMinutes', 'LightlyActiveMinutes', 'SedentaryMinutes']
    selected_c_dropdown = st.selectbox("Select Variable", options = dropdown_c_options)
    slider_val = st.slider(selected_c_dropdown, min(df[selected_c_dropdown]), max(df[selected_c_dropdown]), 1)
    # st.slider('Feature 2', 0, 10, 1)
    # st.slider('Feature 3', 0, 10, 1)
    # st.slider('Feature 4', 0, 10, 1)
    fig = plt.figure(figsize=(15, 8))
    sns.regplot(data = df, x= selected_c_dropdown, y = 'Calories')
    st.pyplot(fig)
    lr = model_pipeline(df, selected_c_dropdown, 'Calories')
    st.write(f"Model Daily Caloric: {round(lr.predict([[slider_val]])[0][0], 2)}")