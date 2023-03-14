"""
Unit tests for calories management module
"""
import sys
import os
import unittest
from unittest.mock import patch
import pandas as pd

sys.path.insert(
    0, (os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../")))

import analysis

class TestProcessDailyCaloriesData(unittest.TestCase):
    """
    Test suite for calories data processing
    """

    def setUp(self):
        self.df = pd.DataFrame({
            'Id': [1503960366, 1503960366, 1927972279, 1927972279],
            'Calories': [1500, 2000, 1800, 1900]
        })

    def test_process_daily_calories_data_smoke(self):
        """
        Processes daily calories data
        """
        output = analysis.calories_analysis.process_daily_calories_data(
            self.df, '1503960366')
        self.assertIsInstance(output, pd.DataFrame)
        self.assertEqual(len(output), 2)
        self.assertSetEqual(set(output['Id']), {1503960366})
        self.assertSetEqual(set(output['Calories']), {1500, 2000})

    def test_filter_df_user_id_called(self):
        """
        Filters by user id
        """
        with patch('analysis.calories_analysis.analysis_utils.filter_df_user_id') as mock_filter:
            analysis.calories_analysis.process_daily_calories_data(self.df)
            mock_filter.assert_called_once_with(self.df, '1503960366')


if __name__ == "__main__":
    unittest.main()
