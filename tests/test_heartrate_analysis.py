import sys
import os
import unittest
import pandas as pd
import datetime

from unittest.mock import patch

sys.path.insert(0, (os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../")))

import analysis

class TestProcessHeartrateData(unittest.TestCase):
    def setUp(self):
        self.df_heartrate = pd.DataFrame({
            'Time': ['04/01/2022 08:30:00 AM', '04/02/2022 10:30:00 AM', '04/03/2022 12:30:00 PM', '04/02/2022 08:30:00 AM', '04/02/2022 10:30:00 AM', '04/02/2022 12:30:00 PM'],
            'Value': [70, 80, 90, 72, 82, 92],
            'Id': [2026352035, 2026352035, 2026352035, 1111111111, 1111111111, 1111111111]
        })

        self.df_daily_sleep = pd.DataFrame({
            'SleepDay': ['04/01/2022 08:30:00 AM', '04/02/2022 10:30:00 AM', '04/03/2022 12:30:00 PM'],
            'TotalMinutesAsleep': [400, 480, 560],
            'Id': [2026352035, 2026352035, 2026352035]
        })

    @patch('analysis.heartrate_analysis.analysis_utils.filter_df_user_id')
    def test_process_heartrate_data_filter_user_id(self, mock_filter_df_user_id):
        # Set up mock return value
        mock_filter_df_user_id.side_effect = [self.df_heartrate, self.df_daily_sleep]

        # Call the function with the mock data
        analysis.heartrate_analysis.process_heartrate_data(self.df_heartrate, self.df_daily_sleep, '1503960366')
        
        self.assertEqual(len(mock_filter_df_user_id.mock_calls), 2)

    def test_process_heartrate_data(self):
        expected_output = pd.DataFrame({
            'date_time': [datetime.datetime(2022, 4, 1), datetime.datetime(2022, 4, 2), datetime.datetime(2022, 4, 3)],
            'Value': [70.0, 80.0, 90.0],
            'day_of_week': ['Friday', 'Saturday', 'Sunday'],
            'TotalMinutesAsleep': [400, 480, 560],
            'Sleep Duration': ['Okay', 'Enough', 'Healthy']
        })

        # Verify expected output
        output = analysis.heartrate_analysis.process_heartrate_data(self.df_heartrate, self.df_daily_sleep, user_id='2026352035')
        self.assertTrue(len(output) == 3)
        self.assertTrue(all(i == j for i,j in zip(output['date_time'].to_numpy(), expected_output['date_time'].to_numpy())))
        self.assertTrue(all(i == j for i,j in zip(output['Value'].to_numpy(), expected_output['Value'].to_numpy())))
        self.assertTrue(all(i == j for i,j in zip(output['day_of_week'].to_numpy(), expected_output['day_of_week'].to_numpy())))
        self.assertTrue(all(i == j for i,j in zip(output['TotalMinutesAsleep'].to_numpy(), expected_output['TotalMinutesAsleep'].to_numpy())))
        self.assertTrue(all(i == j for i,j in zip(output['Sleep Duration'].to_numpy(), expected_output['Sleep Duration'].to_numpy())))        

if __name__ == "__main__":
    unittest.main()
