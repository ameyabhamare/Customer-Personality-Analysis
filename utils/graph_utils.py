import seaborn as sns
import matplotlib.pyplot as plt

"""
_, ax_1 = plt.subplots(figsize=(12,6))
    ax_1 = sns.barplot(x=df_sleep_data["SleepDate"],
                        y=df_sleep_data["TotalTimeInBed"], color='r' )
    ax_1 = sns.barplot(x=df_sleep_data["SleepDate"],
                        y=df_sleep_data["TotalMinutesAsleep"], color='b')
    
    ax_1.set(xlabel="Date", ylabel="Minutes")
    ax_1.set_title("Time asleep and time in bed")
"""

def create_barplot(x_axis, y_axis, color='r', **kwargs):
    ax = sns.barplot(x=x_axis, y=y_axis, color=color)
    ax.set(**kwargs)
    return ax

# sns.lineplot(data = df_sleep_and_steps['StepTotal'], marker='o', ax=ax1, color='g')
def create_lineplot(**kwargs):
    ax = sns.lineplot(**kwargs)
    return ax

def plt_show():
    plt.xticks(rotation=90)
    plt.show()