'''This module reads in the daily_values.csv files and displays relvant visualizations'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

daily_values = pd.read_csv('C:/AMEYA/UW/Academics/DATA 515/Project/FitMe/\
                           heart_rate_analysis/data/daily_values.csv')

ax = sns.lineplot(x = 'day_of_week', y = 'Value', data = daily_values, palette = 'bright')
ax.set(xlabel = 'Day of the week')
ax.plot()
plt.show()

ax = sns.lineplot(x = 'date_time', y = 'Value', data = daily_values, palette = 'bright')
ax.set(xlabel = 'Date')
ax.set(ylabel = 'bpm')
ax.set_xticklabels(labels = daily_values['date_time'], size = 6, rotation = 30)
ax.plot()
plt.show()

sns.kdeplot(daily_values['Value'], shade = True, legend = False)
plt.xlabel('BPM', fontsize = 16)
plt.ylabel('Distribution', fontsize = 10)
plt.show()

sns.boxplot(x = 'Sleep Duration', y = 'Value', data = daily_values, color = 'blue')
plt.xticks(rotation = 45, ha = 'right')
plt.show()
