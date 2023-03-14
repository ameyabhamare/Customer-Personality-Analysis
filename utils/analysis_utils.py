"""
Utilities for analysis module
"""
import pandas as pd
import glob


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


def populate_dropdowns():
    """
    A function to get a unique list of user IDs for the for the drop down

    Parameters:
    - df (pandas DataFrame): The DataFrame to get unique IDs from

    Returns:
    - set of common IDS
    """

    store_ids = []
    for path in glob.glob("data/*"):
        df = pd.read_csv(path)
        store_ids.append(set(df['Id'].unique().tolist()))

    if len(store_ids) == 0:
        raise TypeError("Incorrect Data Import")

    return set.intersection(*store_ids)
