"""
Unit tests for the main app module
"""
import sys
import os
import unittest
from unittest.mock import patch
import pandas as pd

sys.path.insert(
    0, (os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../")))

import app

def mock_create_fig():
    return lambda: (None, None)

class TestApp(unittest.TestCase):
    """
    Test suite for main app entry point
    """

    def setUp(self):
        return super().setUp()

    @patch("app.st")
    def test_setup_streamlit_ui(self, st_mock):
        """
        Makes sure that streamlit ui is being setup properly and that global variables get
        populated
        """
        app.setup_streamlit_ui()

        st_mock.title.assert_called_with('FitMe')
        st_mock.markdown.assert_called()
        st_mock.sidebar.selectbox.assert_called()
        st_mock.sidebar.file_uploader.assert_called()
        self.assertTrue(app.user_id_dropdown is not None)
        self.assertTrue(app.selected_dropdown is not None)
        self.assertTrue(app.files is not None)

    @patch("app.render_heartrate_analysis")
    def test_render_analysis_heartrate(self, mock):
        app.render_analysis('Heart Rate')
        mock.assert_called()

    @patch("app.render_activity_weight_analysis")
    def test_render_analysis_activity_weight(self, mock):
        app.render_analysis('Activity & Weight')
        mock.assert_called()

    @patch("app.render_caloric_model")
    def test_render_analysis_caloric(self, mock):
        app.render_analysis('Caloric Model')
        mock.assert_called()

    @patch("app.render_default")
    def test_render_analysis_default(self, mock):
        app.render_analysis('bleh')
        mock.assert_called()

    @patch("app.st")
    def test_render_heartrate_analysis(self, st_mock):
        with patch("app.pd.read_csv") as read_csv_mock:
            with patch("app.graph_utils") as graph_utils_mock:
                with patch("app.heartrate_analysis") as heartrate_analysis_mock:
                    graph_utils_mock.create_fig.return_value = (None, None)
                    graph_utils_mock.create_barplot.return_value = None
                    heartrate_analysis_mock.process_heartrate_data.return_value = pd.DataFrame({
                        'Value': []
                    })

                    app.render_heartrate_analysis()

                    self.assertEqual(read_csv_mock.call_count, 2)
                    heartrate_analysis_mock.process_heartrate_data.assert_called()
                    self.assertEqual(graph_utils_mock.create_fig.call_count, 4)
                    self.assertEqual(graph_utils_mock.create_lineplot.call_count, 2)
                    self.assertEqual(graph_utils_mock.create_kdeplot.call_count, 1)
                    self.assertEqual(graph_utils_mock.create_boxplot.call_count, 1)
                    self.assertEqual(st_mock.pyplot.call_count, 4)


if __name__ == "__main__":
    unittest.main()
