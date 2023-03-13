import pandas as pd

def filter_df_user_id(df, user_id):
    """
    A function to filter a pandas DataFrame based on a user ID.
    
    Parameters:
    - df (pandas DataFrame): The DataFrame to filter
    - user_id (str or int): The user ID to filter by
    
    Returns:
    - A filtered pandas DataFrame
    """
    df = df.query(f"Id == {user_id}")
    if df.empty:
        raise TypeError("Invalid user id")
    
    return df
