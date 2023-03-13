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

def process_daily_calories_data(df_daily_calories, user_id='1503960366'):
    df_daily_calories = analysis_utils.filter_df_user_id(df_daily_calories, user_id)
    return df_daily_calories