from analysis import *
import pandas as pd

df_sleep_data_unproc = pd.read_csv("../data/sleepDay_merged.csv")
df_sleep_data_proc = plot_sleep_time_vs_time_in_bed(df_sleep_data_unproc, '1503960366')
df_daily_steps_unproc = pd.read_csv("../data/dailySteps_merged.csv")
df_daily_steps_proc = plot_daily_step_pattern(df_daily_steps_unproc, user_id=None)
df_sleep_and_steps_merged = pd.merge(df_daily_steps_proc, df_sleep_data_proc, how='inner',
                                left_on='ActivityDay', right_on='SleepDate')
plot_daily_sleep_vs_step_count(df_sleep_and_steps_merged)
df_daily_calories_unproc = pd.read_csv("../data/dailyCalories_merged.csv")
df_daily_calories_proc = plot_daily_calories_pattern(df_daily_calories_unproc, user_id=None)
