import sys
import os
import unittest
import pandas as pd
import matplotlib

from unittest.mock import patch, Mock

sys.path.insert(0, (os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../")))

import utils

class TestGraphUtils(unittest.TestCase):
    def test_create_fig(self):
        with patch('matplotlib.pyplot.subplots') as mock_subplots:
            mock_fig, mock_ax = Mock(), Mock()
            mock_subplots.return_value = (mock_fig, mock_ax)

            # Test calling function with default arguments
            fig, ax = utils.graph_utils.create_fig()
            self.assertEqual(fig, mock_fig)
            self.assertEqual(ax, mock_ax)
            mock_subplots.assert_called_once()

            # Test calling function with non-default arguments
            fig, ax = utils.graph_utils.create_fig(nrows=2, ncols=3)
            self.assertEqual(fig, mock_fig)
            self.assertEqual(ax, mock_ax)
            mock_subplots.assert_called_with(nrows=2, ncols=3)

    def test_create_barplot(self):
        with patch('seaborn.barplot') as mock_barplot:
            mock_ax = Mock()
            mock_barplot.return_value = mock_ax

            # Test calling function with default arguments
            ax = utils.graph_utils.create_barplot('x', 'y')
            self.assertEqual(ax, mock_ax)
            mock_barplot.assert_called_once_with(x='x', y='y', color='r', ax=None)
            mock_ax.set.assert_called_once_with()

            # Test calling function with non-default arguments
            ax = utils.graph_utils.create_barplot('x', 'y', color='g', ax=mock_ax, xlabel='X Label', ylabel='Y Label')
            self.assertEqual(ax, mock_ax)
            mock_barplot.assert_called_with(x='x', y='y', color='g', ax=mock_ax)
            mock_ax.set.assert_called_with(xlabel='X Label', ylabel='Y Label')

    def test_create_lineplot(self):
        df = pd.DataFrame({'x': ['a', 'b', 'c'], 'y': [1, 2, 3]})
        with patch('seaborn.lineplot') as mock_lineplot:
            mock_ax = Mock()
            mock_lineplot.return_value = mock_ax

            # Test calling function with default arguments
            ax = utils.graph_utils.create_lineplot(data=df)
            self.assertEqual(ax, mock_ax)
            mock_lineplot.assert_called_once_with(data=df)
            mock_ax.set.assert_called_once_with(xlabel='', ylabel='', title='')

            # Test calling function with non-default arguments
            ax = utils.graph_utils.create_lineplot(data=df, xlabel='X Label', ylabel='Y Label', title='Plot Title')
            self.assertEqual(ax, mock_ax)
            mock_lineplot.assert_called_with(data=df)
            mock_ax.set.assert_called_with(xlabel='X Label', ylabel='Y Label', title='Plot Title')

    def test_create_kdeplot(self):
        xlabel='X Label'
        ylabel='Y Label'
        title='KDE Plot'
        
        with patch('seaborn.kdeplot') as mock_kdeplot:
            mock_ax = Mock()
            mock_kdeplot.return_value = mock_ax
            
            ax = utils.graph_utils.create_kdeplot([1, 2, 3, 4, 5], xlabel=xlabel, ylabel=ylabel, title=title)
            
            # Assertions
            mock_kdeplot.assert_called_once_with([1, 2, 3, 4, 5])
            mock_ax.set.assert_called_once_with(xlabel=xlabel, ylabel=ylabel, title=title)
            mock_ax.tick_params.assert_called_once_with(labelrotation=90)
            self.assertEqual(ax, mock_ax)
        
    def test_create_boxplot(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        xlabel = 'X Label'
        ylabel = 'Y Label'
        title = 'Box Plot'
        # Mocking sns.boxplot
        with patch('seaborn.boxplot') as mock_boxplot:
            mock_ax = Mock()
            mock_boxplot.return_value = mock_ax
            
            ax = utils.graph_utils.create_boxplot(data, xlabel, ylabel, title)
            
            # Assertions
            mock_boxplot.assert_called_once_with(data=data)
            mock_ax.set.assert_called_once_with(xlabel=xlabel, ylabel=ylabel, title=title)
            mock_ax.tick_params.assert_called_once_with(labelrotation=90)
            self.assertEqual(ax, mock_ax)
            
    def test_create_regplot(self):
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        xlabel = 'X Label'
        ylabel = 'Y Label'
        title = 'Regression Plot'
        
        # Mocking sns.regplot
        with patch('seaborn.regplot') as mock_regplot:
            mock_ax = Mock()
            mock_regplot.return_value = mock_ax
            
            ax = utils.graph_utils.create_regplot(x=x, y=y, xlabel=xlabel, ylabel=ylabel, title=title)
            
            # Assertions
            mock_regplot.assert_called_once_with(x=x, y=y, xlabel=xlabel, ylabel=ylabel, title=title)
            self.assertEqual(ax, mock_ax)
    
    @patch('matplotlib.pyplot.xticks')
    @patch('matplotlib.pyplot.show')
    def test_plt_show(self, mock_show, mock_xticks):
        utils.graph_utils.plt_show()
        mock_xticks.assert_called_once_with(rotation=90)
        mock_show.assert_called_once()
        


if __name__ == "__main__":
    unittest.main()
