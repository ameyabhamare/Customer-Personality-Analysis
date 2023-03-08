import streamlit as st
import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt

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

#Modular work
if selected_dropdown == 'Heart Rate':
    if files is not None:
        fig = plt.figure(figsize=(15, 8))
        try:
            sns.lineplot(data = df , y = 'Calories', x = 'dayofweek')
        except NameError as e:
            st.write("Heart Rate file not uploaded correctly")
        st.pyplot(fig)

if selected_dropdown == 'Activity & Weight':
    st.write("Activity & Weight")

if selected_dropdown == 'Caloric Model':
    st.slider('Feature 1', 0, 10, 1)
    st.slider('Feature 2', 0, 10, 1)
    st.slider('Feature 3', 0, 10, 1)
    st.slider('Feature 4', 0, 10, 1)
    st.write("Model Daily Caloric: ")