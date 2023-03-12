import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

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