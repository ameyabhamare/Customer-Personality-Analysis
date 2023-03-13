import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def create_fig(**kwargs):
    fig, ax = plt.subplots(**kwargs)
    return fig, ax

def create_barplot(x_axis, y_axis, color='r', ax=None, **kwargs):
    ax = sns.barplot(x=x_axis, y=y_axis, color=color, ax=ax)
    ax.set(**kwargs)
    ax.tick_params(labelrotation=90)
    return ax

def create_lineplot(xlabel='', ylabel='', title='', **kwargs):
    ax = sns.lineplot(**kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.tick_params(labelrotation=90)
    return ax

def create_kdeplot(vals, xlabel='', ylabel='', title='', **kwargs):
    ax = sns.kdeplot(vals, **kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.tick_params(labelrotation=90)
    return ax


def create_boxplot(data, xlabel='', ylabel='', title='', **kwargs):
    ax = sns.boxplot(data = data, **kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.tick_params(labelrotation=90)
    return ax

def create_regplot(**kwargs):
    ax = sns.regplot(**kwargs)
    return ax

def plt_show():
    plt.xticks(rotation=90)
    plt.show()