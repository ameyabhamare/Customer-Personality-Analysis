import numpy as np
import pandas as pd
import unittest
import sys
import os
from unittest.mock import patch

sys.path.insert(0, (os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../")))

import activity_and_weight_analysis as testmodule

# set up mock data
mock_df_sleep_data = pd.read_csv(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/./mock_data/mock_sleepDay_merged.csv"))
mock_df_daily_steps = pd.read_csv(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/./mock_data/mock_dailySteps_merged.csv"))

class ActivityWeightAnalysisTests(unittest.TestCase):
    """
    This is the test suite for the activity_and_weight_analysis module
    """

    """
    plot_sleep_time_vs_time_in_bed
    """
    def smoke_test_plot_sleep_time_vs_time_in_bed(self):
        """
        Smoke test for plot_sleep_time_vs_time_in_bed
        """
        with patch("activity_and_weight_analysis.plt") as mock_plt:
            try:
                testmodule.plot_sleep_time_vs_time_in_bed(mock_df_sleep_data)
                mock_plt.show.assert_called_once()
            except:
                self.fail("exception thrown in smoke test")

    def test_plot_sleep_time_vs_time_in_bed_default_args(self):
        """
        User id should default to '1503960366' in case no user_id is passed in
        """
        with patch("activity_and_weight_analysis.plt") as mock_plt:
            try:
                df, _ = testmodule.plot_sleep_time_vs_time_in_bed(mock_df_sleep_data)
                self.assertEqual(len(df['Id'].unique()), 1)
                self.assertEqual((df['Id'].unique())[0], 1503960366)
                mock_plt.show.assert_called_once()
            except:
                self.fail("exception thrown")
    
    def test_plot_sleep_time_vs_time_in_bed_args(self):
        """
        User id can be passed in
        """
        with patch("activity_and_weight_analysis.plt") as mock_plt:
            try:
                df, _ = testmodule.plot_sleep_time_vs_time_in_bed(mock_df_sleep_data, user_id="1982938473")
                self.assertEqual(len(df['Id'].unique()), 1)
                self.assertEqual((df['Id'].unique())[0], 1982938473)
                mock_plt.show.assert_called_once()
            except:
                self.fail("exception thrown")

    def test_plot_sleep_time_vs_time_in_bed_plot(self):
        """
        Makes sure that the graph produced contains the right axes as well as 
        the right amount of data
        """
        with patch("activity_and_weight_analysis.plt") as mock_plt:
            try:
                df, fig = testmodule.plot_sleep_time_vs_time_in_bed(mock_df_sleep_data, user_id="1982938473")
                self.assertEqual(fig.get_xaxis().get_label().get_text(), "Date")
                self.assertEqual(fig.get_yaxis().get_label().get_text(), "Minutes")
                self.assertEqual(len(fig.lines), 102)
                mock_plt.show.assert_called_once()
            except:
                self.fail("exception thrown")

    """
    plot_daily_step_pattern
    """
    def smoke_test_plot_daily_step_pattern(self):
        """
        Smoke test for plot_daily_step_pattern
        """
        with patch("activity_and_weight_analysis.plt") as mock_plt:
            try:
                testmodule.plot_daily_step_pattern(mock_df_daily_steps)
                mock_plt.show.assert_called_once()
            except:
                self.fail("exception thrown in smoke test")

    def test_plot_daily_step_pattern_default_args(self):
        """
        User id should default to '1503960366' in case no user_id is passed in
        """
        with patch("activity_and_weight_analysis.plt") as mock_plt:
            try:
                df, _ = testmodule.plot_daily_step_pattern(mock_df_daily_steps)
                self.assertEqual(len(df['Id'].unique()), 1)
                self.assertEqual((df['Id'].unique())[0], 1503960366)
                mock_plt.show.assert_called_once()
            except:
                self.fail("exception thrown")
    
    def test_plot_daily_step_pattern_args(self):
        """
        User id can be passed in
        """
        with patch("activity_and_weight_analysis.plt") as mock_plt:
            try:
                df, _ = testmodule.plot_daily_step_pattern(mock_df_daily_steps, user_id="1624580081")
                self.assertEqual(len(df['Id'].unique()), 1)
                self.assertEqual((df['Id'].unique())[0], 1624580081)
                mock_plt.show.assert_called_once()
            except:
                self.fail("exception thrown")

    def test_plot_daily_step_pattern_plot(self):
        """
        Makes sure that the graph produced contains the right axes as well as 
        the right amount of data
        """
        with patch("activity_and_weight_analysis.plt.show") as mock_plt:
            try:
                df, fig = testmodule.plot_daily_step_pattern(mock_df_daily_steps, user_id="1624580081")
                self.assertEqual(fig.get_xaxis().get_label().get_text(), "ActivityDay")
                self.assertEqual(fig.get_yaxis().get_label().get_text(), "StepTotal")
                self.assertEqual(len(fig.lines), 102)
            except:
                self.fail("exception thrown")

if __name__ == "__main__":
    unittest.main()