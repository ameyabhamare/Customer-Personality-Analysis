import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# Setting matplotlib backend to 'Agg'
matplotlib.use('Agg')

def create_fig(**kwargs):
    """
    Create a figure with subplots based on the given parameters

    Args:
    **kwargs: Keyword arguments passed to subplots()

    Returns:
    fig: Figure object
    ax: Axes object

    """
    # Create a figure with subplots based on the given parameters
    fig, ax = plt.subplots(**kwargs)
    return fig, ax

def create_barplot(x_axis, y_axis, color='r', ax=None, **kwargs):
    """
    Create a bar plot with the given parameters

    Args:
    x_axis: Variable to be plotted on the x-axis
    y_axis: Variable to be plotted on the y-axis
    color: Color of the bars in the plot, default is 'r' (red)
    ax: Axes object, default is None
    **kwargs: Additional keyword arguments passed to barplot()

    Returns:
    ax: Axes object

    """
    # Create a bar plot with the given parameters
    ax = sns.barplot(x=x_axis, y=y_axis, color=color, ax=ax)
    ax.set(**kwargs)
    ax.tick_params(labelrotation=90)
    return ax

def create_lineplot(xlabel='', ylabel='', title='', **kwargs):
    """
    Create a line plot with the given parameters

    Args:
    xlabel: Label for the x-axis, default is ''
    ylabel: Label for the y-axis, default is ''
    title: Title of the plot, default is ''
    **kwargs: Additional keyword arguments passed to lineplot()

    Returns:
    ax: Axes object

    """
    # Create a line plot with the given parameters
    ax = sns.lineplot(**kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.tick_params(labelrotation=90)
    return ax

def create_kdeplot(vals, xlabel='', ylabel='', title='', **kwargs):
    """
    Create a kernel density estimate (KDE) plot with the given parameters

    Args:
    vals: Values for which the KDE is estimated
    xlabel: Label for the x-axis, default is ''
    ylabel: Label for the y-axis, default is ''
    title: Title of the plot, default is ''
    **kwargs: Additional keyword arguments passed to kdeplot()

    Returns:
    ax: Axes object

    """
    # Create a KDE plot with the given parameters
    ax = sns.kdeplot(vals, **kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.tick_params(labelrotation=90)
    return ax


def create_boxplot(data, xlabel='', ylabel='', title='', **kwargs):
    """
    Create a box plot with the given parameters

    Args:
    data: Data to be plotted
    xlabel: Label for the x-axis, default is ''
    ylabel: Label for the y-axis, default is ''
    title: Title of the plot, default is ''
    **kwargs: Additional keyword arguments passed to boxplot()

    Returns:
    ax: Axes object

    """
    # Create a box plot with the given parameters
    ax = sns.boxplot(data=data, **kwargs)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.tick_params(labelrotation=90)
    return ax

def create_regplot(**kwargs):
    """
    Creates a regression plot using Seaborn's regplot function.

    Args:
        **kwargs: keyword arguments passed to Seaborn's regplot function.

    Returns:
        ax: Matplotlib axis object with the regression plot.
    """
    ax = sns.regplot(**kwargs)
    return ax


def plt_show():
    """
    Displays the current figure using Matplotlib's show function.
    The x-axis labels are rotated 90 degrees for readability.
    """
    plt.xticks(rotation=90)
    plt.show()
