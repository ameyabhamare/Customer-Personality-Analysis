import sys
import os
import unittest
import pandas as pd

from unittest.mock import patch

sys.path.insert(0, (os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../")))

import analysis

class TestProcessDailyCaloriesData(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'Id': [1503960366, 1503960366, 1927972279, 1927972279],
            'Calories': [1500, 2000, 1800, 1900]
        })

    def test_process_daily_calories_data_smoke(self):
        output = analysis.calories_analysis.process_daily_calories_data(self.df, '1503960366')
        assert isinstance(output, pd.DataFrame)
        assert len(output) == 2
        assert set(output['Id']) == {1503960366}
        assert set(output['Calories']) == {1500, 2000}

    def test_filter_df_user_id_called(self):
        with patch('analysis.calories_analysis.analysis_utils.filter_df_user_id') as mock_filter:
            analysis.calories_analysis.process_daily_calories_data(self.df)
            mock_filter.assert_called_once_with(self.df, '1503960366')

if __name__ == "__main__":
    unittest.main()