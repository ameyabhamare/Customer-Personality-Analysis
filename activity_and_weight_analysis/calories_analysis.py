import pandas as pd
from sklearn.linear_model import LinearRegression
from utils import analysis_utils

# def plot_daily_calories_pattern(df_daily_calories, user_id=None):
#     """
#     A method to generate a graph for daily calories.
#     Args:
#     df_sleep_data - Dataframe containing the number of calories burnt everyday.
#     user_id (None: optional) - The user-id of the user.

#     Return:
#     df_sleep_data - The processed calories dataframe.
#     """
#     if user_id is None:
#         user_id = '1503960366'
#     df_daily_calories = df_daily_calories.query(f"Id == {user_id}")
#     _, ax1 = plt.subplots(figsize=(12,6))
#     sns.lineplot(data = df_daily_calories, x='ActivityDay', y='Calories', marker='o',
#                     ax=ax1, color='g')
#     plt.xticks(rotation=90)
#     plt.show()
#     return df_daily_calories

# def transform_dataframe(df_):
#     '''
#     This function adds new features/columns to the dataframe
#     '''
#     df_['ActivityDate'] = pd.to_datetime(df_['ActivityDate'])
#     df_['year'] = df_['ActivityDate'].dt.year
#     df_['month'] = df_['ActivityDate'].dt.month
#     df_['dayofweek'] = df_['ActivityDate'].dt.dayofweek
#     
#     df_['dayofweek'] = df_['dayofweek'].map(day_mapping)
#     return df_

def process_daily_calories_data(df_daily_calories, user_id='1503960366'):
    df_daily_calories = analysis_utils.filter_df_user_id(df_daily_calories, user_id)
    day_mapping = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun' }

    df_daily_calories['ActivityDate'] = pd.to_datetime(df_daily_calories['ActivityDate'])
    df_daily_calories['year'] = df_daily_calories['ActivityDate'].dt.year
    df_daily_calories['month'] = df_daily_calories['ActivityDate'].dt.month
    df_daily_calories['dayofweek'] = df_daily_calories['ActivityDate'].map(lambda v: day_mapping[v.dt.dayofweek])

    return df_daily_calories

def calories_linreg_model(df, x):
    '''
    This is a model functions and it returns the linear regression object
    '''
    i = df.loc[:, x].values.reshape(-1, 1)  # values converts it into a numpy_ array_
    j = df.loc[:, 'Calories'].values.reshape(-1, 1)  # -1: calc dimensn of rows, but have 1 column
    linear_regressor = LinearRegression()  # create object for the class
    linear_regressor.fit(i, j)  # perform linear regression
    #Y_pred = linear_regressor.predict(X_)  # make predictions
    return linear_regressor
