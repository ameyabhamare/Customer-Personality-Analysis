"""
This module analyzes the activity and weight data to generate insights about
the user's health.
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def plot_sleep_time_vs_time_in_bed(df_sleep_data, user_id=None):
    """
    A method to generate a graph between sleep time v/s time in bed.
    Args:
    df_sleep_data - Dataframe containing the time in bed and total sleep time columns.
    user_id (None: optional) - The user-id of the user.

    Return:
    df_sleep_data - The processed sleep dataframe.
    """
    if user_id is None:
        user_id = '1503960366'
    df_sleep_data = df_sleep_data.query(f"Id == {user_id}")
    df_sleep_data['SleepDate'] = df_sleep_data.apply(lambda x: x['SleepDay'].split(" ")[0], axis=1)
    df_sleep_data = df_sleep_data.drop(['SleepDay', 'TotalSleepRecords'], axis=1)
    _, ax_1 = plt.subplots(figsize=(12,6))
    ax_1 = sns.barplot(x=df_sleep_data["SleepDate"],
                        y=df_sleep_data["TotalTimeInBed"], color='r' )
    ax_1 = sns.barplot(x=df_sleep_data["SleepDate"],
                        y=df_sleep_data["TotalMinutesAsleep"], color='b')
    ax_1.set(xlabel="Date", ylabel="Minutes")
    plt.xticks(rotation=90)
    plt.show()
    return df_sleep_data

def plot_daily_step_pattern(df_daily_steps, user_id=None):
    """
    A method to generate a graph for daily step pattern.
    Args:
    df_daily_steps - Dataframe containing the number of steps taken by the user everyday.
    user_id (None: optional) - The user-id of the user.

    Return:
    df_sleep_data - The processed steps dataframe.
    """
    if user_id is None:
        user_id = '1503960366'
    df_daily_steps = df_daily_steps.query(f"Id == {user_id}")
    _, ax1 = plt.subplots(figsize=(12,6))
    sns.barplot(df_daily_steps, x='ActivityDay', y='StepTotal', color='g', ax=ax1)
    plt.xticks(rotation=90)
    plt.show()
    return df_daily_steps

def plot_daily_sleep_vs_step_count(df_sleep_and_steps):
    """
    A method to generate a graph between sleep time v/s step count.
    Args:
    df_sleep_data - Dataframe containing the sleep data merged with number of steps everyday.
    user_id (None: optional) - The user-id of the user.

    Return:
    None
    """
    _, ax1 = plt.subplots(figsize=(12,6))
    sns.lineplot(data = df_sleep_and_steps['StepTotal'], marker='o', ax=ax1, color='g')
    plt.xticks(rotation=90)
    ax2 = ax1.twinx()
    sns.barplot(data = df_sleep_and_steps, x='SleepDate', y='TotalMinutesAsleep',
                    alpha=0.4, ax=ax2, color='r')
    ax1.set(xlabel="Date")
    plt.show()

def plot_daily_calories_pattern(df_daily_calories, user_id=None):
    """
    A method to generate a graph for daily calories.
    Args:
    df_sleep_data - Dataframe containing the number of calories burnt everyday.
    user_id (None: optional) - The user-id of the user.

    Return:
    df_sleep_data - The processed calories dataframe.
    """
    if user_id is None:
        user_id = '1503960366'
    df_daily_calories = df_daily_calories.query(f"Id == {user_id}")
    _, ax1 = plt.subplots(figsize=(12,6))
    sns.lineplot(data = df_daily_calories, x='ActivityDay', y='Calories', marker='o',
                    ax=ax1, color='g')
    plt.xticks(rotation=90)
    plt.show()
    return df_daily_calories

if __name__ == "__main__":

    df_sleep_data_unproc = pd.read_csv("../data/sleepDay_merged.csv")
    df_sleep_data_proc = plot_sleep_time_vs_time_in_bed(df_sleep_data_unproc, '1503960366')
    df_daily_steps_unproc = pd.read_csv("../data/dailySteps_merged.csv")
    df_daily_steps_proc = plot_daily_step_pattern(df_daily_steps_unproc, user_id=None)
    df_sleep_and_steps_merged = pd.merge(df_daily_steps_proc, df_sleep_data_proc, how='inner',
                                    left_on='ActivityDay', right_on='SleepDate')
    plot_daily_sleep_vs_step_count(df_sleep_and_steps_merged)
    df_daily_calories_unproc = pd.read_csv("../data/dailyCalories_merged.csv")
    df_daily_calories_proc = plot_daily_calories_pattern(df_daily_calories_unproc, user_id=None)
