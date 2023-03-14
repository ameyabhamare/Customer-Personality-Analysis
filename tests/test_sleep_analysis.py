import sys
import os
import unittest
import pandas as pd

from unittest.mock import patch

sys.path.insert(0, (os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../")))

import analysis

class TestProcessDailySleepData(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'Id': [1503960366, 1503960366, 1503960366, 1],
            'SleepDay': ['4/12/2016 12:00:00 AM', '4/13/2016 12:00:00 AM', '4/15/2016 12:00:00 AM',  '4/15/2016 12:00:00 AM'],
            'TotalSleepRecords': [1, 2, 1, 3],
            'TotalMinutesAsleep': [327, 384, 412, 404],
            'TotalTimeInBed': [346, 407, 442, 440]
        })

    def test_process_sleep_analysis_smoke(self):
        df_result = analysis.sleep_analysis.process_sleep_analysis_data(self.df, '1503960366')
        self.assertIsInstance(df_result, pd.DataFrame)
        self.assertTrue(len(df_result) == 3)

    
    @patch('analysis.sleep_analysis.analysis_utils.filter_df_user_id')
    def test_process_sleep_analysis_data_filter_user_id(self, mock_filter_df_user_id):
        # Set up mock return value
        mock_filter_df_user_id.return_value = self.df
        
        # Call function
        df_result = analysis.sleep_analysis.process_sleep_analysis_data(self.df, '1503960366')
        
        # Assert that filter_df_user_id was called with the correct arguments
        mock_filter_df_user_id.assert_called_once_with(self.df, '1503960366')
        
        # Assert that the returned dataframe has the correct columns
        self.assertIsInstance(df_result, pd.DataFrame)

    def test_process_sleep_analysis_data(self):
        filtered_data = analysis.sleep_analysis.process_sleep_analysis_data(self.df, user_id='1503960366')
        expected_columns = ['Id', 'TotalMinutesAsleep', 'TotalTimeInBed', 'SleepDate']
        self.assertListEqual(list(filtered_data.columns), expected_columns)
        
        expected_data = pd.DataFrame({
            'Id': [1503960366, 1503960366, 1503960366],
            'TotalMinutesAsleep': [327, 384, 412],
            'TotalTimeInBed': [346, 407, 442],
            'SleepDate': ['4/12/2016', '4/13/2016', '4/15/2016']
        })
        pd.testing.assert_frame_equal(filtered_data[expected_columns], expected_data)

if __name__ == "__main__":
    unittest.main()