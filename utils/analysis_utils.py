import pandas as pd

def filter_df_user_id(df, user_id):
    df = df.query(f"Id == {user_id}")
    if df.empty:
        raise TypeError("Invalid user id")
    
    return df