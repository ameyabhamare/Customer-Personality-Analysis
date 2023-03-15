"""
Example file to demonstrate how to process sleep data
"""
import pandas as pd
# import sleep analysis from analysis package
from analysis import sleep_analysis

# read in dataframe from sleepDay dataset
sleep_df = pd.read_csv("data/sleepDay_merged.csv")

# sleep df overview
print(sleep_df.describe())

# process sleep data for user '1503960366'
sleep_df_proc = sleep_analysis.process_sleep_analysis_data(
    sleep_df, '1503960366')

print(sleep_df_proc.describe())
