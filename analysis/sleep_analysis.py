from utils import analysis_utils

def process_sleep_analysis_data(df_sleep_data, user_id='1503960366'):
    """
    Process sleep analysis data and extract relevant columns.
    
    Args:
        df_sleep_data (pandas.DataFrame): DataFrame containing sleep data.
        user_id (str, optional): User ID to filter data by.
        
    Returns:
        pandas.DataFrame: Processed DataFrame containing only relevant columns.
    """ 
    # filter data by user ID
    df_sleep_data = analysis_utils.filter_df_user_id(df_sleep_data, user_id)

    # extract SleepDate from SleepDay column
    df_sleep_data['SleepDate'] = df_sleep_data['SleepDay'].map(lambda v: v.split(" ")[0])
    
    # drop unused columns
    df_sleep_data = df_sleep_data.drop(['SleepDay', 'TotalSleepRecords'], axis=1)
    
    return df_sleep_data