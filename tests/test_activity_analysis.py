"""
Unit tests for the activity analysis module
"""
import sys
import os
import unittest
from unittest.mock import patch
import pandas as pd

sys.path.insert(
    0, (os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../")))

import analysis

class TestProcessDailyActivityData(unittest.TestCase):
    """
    Test suite for daily activity data processing
    """
    def setUp(self):
        # set up mock data frame
        self.df = pd.DataFrame({
            'Id': [1, 1, 1, 1, 1, 2],
            'ActivityDate': ['01/01/2022', '01/01/2022', '01/01/2022', '01/01/2022', '01/01/2022', '03/11/2022'],
            'TotalSteps': [10000.0, 5000.0, 7000.0, 8000.0, 6000.0, 200.0],
        })

    def test_smoke(self):
        '''
        Smoke test to ensure the function runs without errors.
        '''
        processed_df = analysis.activity_analysis.process_daily_activity_data(
            self.df, '1')
        self.assertIsInstance(processed_df, pd.DataFrame)

    @patch('analysis.activity_analysis.analysis_utils.filter_df_user_id')
    def test_process_daily_activity_data(self, mock_filter_df_user_id):
        """
        making sure we filter by user id
        """
        # Set up mock return value
        mock_filter_df_user_id.return_value = self.df

        # Call function
        df_result = analysis.activity_analysis.process_daily_activity_data(
            self.df, '1')

        # Assert that filter_df_user_id was called with the correct arguments
        mock_filter_df_user_id.assert_called_once_with(self.df, '1')

        # Assert that the returned dataframe has the correct columns
        self.assertTrue(all(col in df_result.columns for col in [
                        'year', 'month', 'dayofweek']))

    def test_year(self):
        """
        Test that year gets extracted properly
        """
        expected_output = pd.DataFrame({
            'Id': [2],
            'ActivityDate': ['03/11/2022'],
            'Calories': [200],
            'year': [2022],
            'month': [3],
            'dayofweek': [4]
        })
        user_id = '2'
        output = analysis.activity_analysis.process_daily_activity_data(
            self.df, user_id)
        self.assertTrue('year' in output.columns,
                        "Year column not found in output DataFrame.")
        self.assertTrue(output['year'].to_numpy(
        ) == expected_output['year'].to_numpy(), "Year column is not correct.")

    def test_month(self):
        """
        Month gets extracted properly
        """
        expected_output = pd.DataFrame({
            'Id': [2],
            'ActivityDate': ['03/11/2022'],
            'Calories': [200],
            'year': [2022],
            'month': [3],
            'dayofweek': [4]
        })
        user_id = '2'
        output = analysis.activity_analysis.process_daily_activity_data(
            self.df, user_id)
        self.assertTrue('month' in output.columns,
                        "Month column not found in output DataFrame.")
        self.assertTrue(output['month'].to_numpy(
        ) == expected_output['month'].to_numpy(), "Month column is not correct.")

    def test_dayofweek(self):
        """
        Day of week gets extracted properly
        """
        expected_output = pd.DataFrame({
            'Id': [2],
            'ActivityDate': ['03/11/2022'],
            'Calories': [200],
            'year': [2022],
            'month': [3],
            'dayofweek': [4]
        })
        user_id = '2'
        output = analysis.activity_analysis.process_daily_activity_data(
            self.df, user_id)
        self.assertTrue('dayofweek' in output.columns,
                        "Day of week column not found in output DataFrame.")
        self.assertTrue(output['dayofweek'].to_numpy(
        ) == expected_output['dayofweek'].to_numpy(), "Month column is not correct.")


if __name__ == "__main__":
    unittest.main()
