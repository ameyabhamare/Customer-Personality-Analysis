import sys
import os
import unittest
import pandas as pd

from unittest.mock import patch

sys.path.insert(0, (os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../")))

import analysis

class TestProcessDailyStepsData(unittest.TestCase):

    def setUp(self):
        self.mock_df_daily_steps = pd.DataFrame({
            'Id': [1503960366, 1503960366, 1503960366, 1503960366],
            'ActivityDay': ['4/12/2016', '4/13/2016', '4/15/2016', '4/16/2016'],
            'StepTotal': [13162, 10735, 9762, 12669]
        })
        self.mock_df_daily_sleep = pd.DataFrame({
            'Id': [1503960366, 1503960366, 1503960366, 1503960366],
            'SleepDay': ['4/12/2016 12:00:00 AM', '4/13/2016 12:00:00 AM', '4/15/2016 12:00:00 AM', '4/16/2016 12:00:00 AM'],
            'TotalSleepRecords': [1, 2, 1, 2],
            'TotalMinutesAsleep': [327, 384, 412, 340],
            'TotalTimeInBed': [346, 407, 442, 367]
        })
    
    @patch('analysis.steps_analysis.analysis_utils.filter_df_user_id')
    def test_process_daily_steps_data_filter_user_id(self, mock_filter_df_user_id):
        # Set up mock return value
        mock_filter_df_user_id.return_value = self.mock_df_daily_steps
        
        # Call function
        df_result = analysis.steps_analysis.process_daily_steps_data(self.mock_df_daily_steps, '1503960366')
        
        # Assert that filter_df_user_id was called with the correct arguments
        mock_filter_df_user_id.assert_called_once_with(self.mock_df_daily_steps, '1503960366')
        
        # Assert that the returned dataframe has the correct columns
        self.assertIsInstance(df_result, pd.DataFrame)

    def test_process_daily_steps_data(self):
        filtered_data = analysis.steps_analysis.process_daily_steps_data(self.mock_df_daily_steps, user_id='1503960366')
        expected_columns = ['Id', 'ActivityDay', 'StepTotal']
        self.assertListEqual(list(filtered_data.columns), expected_columns)
        
        expected_data = pd.DataFrame({
            'Id': [1503960366, 1503960366, 1503960366, 1503960366],
            'ActivityDay': ['4/12/2016', '4/13/2016', '4/15/2016', '4/16/2016'],
            'StepTotal': [13162, 10735, 9762, 12669]
        })
        pd.testing.assert_frame_equal(filtered_data[expected_columns], expected_data)

    def test_process_daily_sleep_steps_data(self):
        # Call the function with the mock data
        df_result = analysis.steps_analysis.process_daily_sleep_steps_data(self.mock_df_daily_steps, self.mock_df_daily_sleep, '1503960366')

        # Check the result
        self.assertIsInstance(df_result, pd.DataFrame)
        self.assertEqual(len(df_result), 4)
        self.assertTrue(set(['ActivityDay', 'StepTotal', 'TotalMinutesAsleep', 'TotalTimeInBed']).issubset(set(df_result.columns)))
        self.assertListEqual(df_result['ActivityDay'].unique().tolist(), ['4/12/2016', '4/13/2016', '4/15/2016', '4/16/2016'])
        self.assertListEqual(df_result['TotalMinutesAsleep'].unique().tolist(), [327, 384, 412, 340])
        self.assertListEqual(df_result['TotalTimeInBed'].unique().tolist(), [346, 407, 442, 367])


if __name__ == "__main__":
    unittest.main()
