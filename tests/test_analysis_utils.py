"""
Unit tests for utils/analysis module
"""
import sys
import os
import unittest
from unittest.mock import patch
import pandas as pd


sys.path.insert(
    0, (os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../")))

import utils

class TestAnalysisUtils(unittest.TestCase):
    """
    Test suite for analysis utils
    """

    def test_filter_df_user_id_valid_id(self):
        """
        Filters by user id
        """
        # Arrange
        df = pd.DataFrame(
            {'Id': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
        user_id = 2

        # Act
        filtered_df = utils.analysis_utils.filter_df_user_id(df, user_id)

        # Assert
        self.assertEqual(len(filtered_df), 1)
        self.assertEqual(filtered_df.iloc[0]['Name'], 'Bob')

    def test_filter_df_user_id_invalid_id(self):
        """
        Throws upon invalid id
        """
        # Arrange
        df = pd.DataFrame(
            {'Id': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
        user_id = 4

        # Act/Assert
        with self.assertRaises(TypeError):
            utils.analysis_utils.filter_df_user_id(df, user_id)

    def test_populate_dropdowns(self):
        """
        Unit test for populate_dropdowns
        """
        with patch("utils.analysis_utils.pd") as pd_mock:
            with patch("utils.analysis_utils.glob") as glob_mock:
                pd_mock.read_csv.return_value = pd.DataFrame({
                    'Id': [1, 2, 3]
                })
                glob_mock.glob.return_value = ["path1", "path2"]

                store_ids = utils.analysis_utils.populate_dropdowns()

                pd_mock.read_csv.assert_called()
                glob_mock.glob.assert_called()
                self.assertEqual(store_ids, set([1, 2, 3]))
    
    def test_populate_dropdowns_no_user_id(self):
        """
        Unit test for populate_dropdowns
        """
        with patch("utils.analysis_utils.pd") as pd_mock:
            with patch("utils.analysis_utils.glob") as glob_mock:
                pd_mock.read_csv.return_value = pd.DataFrame({
                    'Id': []
                })
                glob_mock.glob.return_value = ["path1", "path2"]

                with self.assertRaises(TypeError):
                    utils.analysis_utils.populate_dropdowns()


if __name__ == "__main__":
    unittest.main()
