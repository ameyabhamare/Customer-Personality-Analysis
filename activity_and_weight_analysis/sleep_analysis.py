from utils import analysis_utils

def process_sleep_analysis_data(df_sleep_data, user_id='1503960366'):
    """
    A method to generate a graph between sleep time v/s time in bed.
    Args:
    df_sleep_data - Dataframe containing the time in bed and total sleep time columns.
    user_id (None: optional) - The user-id of the user.

    Return:
    df_sleep_data - The processed sleep dataframe.
    """ 
    df_sleep_data = analysis_utils.filter_df_user_id(df_sleep_data, user_id)

    # extract SleepDate from sleep day
    df_sleep_data['SleepDate'] = df_sleep_data['SleepDay'].map(lambda v: v.split(" ")[0])
    # drop unused cols
    df_sleep_data = df_sleep_data.drop(['SleepDay', 'TotalSleepRecords'], axis=1)
    
    return df_sleep_data