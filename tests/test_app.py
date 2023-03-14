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

class TestProcessDailyActivityData(unittest.TestCase):