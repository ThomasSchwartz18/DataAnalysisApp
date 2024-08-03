# tests/test_data_management.py

import unittest
import pandas as pd
from src.data_management import *

class TestDataManagement(unittest.TestCase):

    def test_impute_missing_values(self):
        df = pd.DataFrame({'col1': [1, 2, None, 4]})
        df_imputed = impute_missing_values(df, strategy='mean')
        self.assertFalse(df_imputed.isnull().values.any())

    def test_remove_duplicates(self):
        df = pd.DataFrame({'col1': [1, 1, 2, 2], 'col2': [3, 3, 4, 4]})
        df_cleaned = remove_duplicates(df)
        self.assertEqual(len(df_cleaned), 2)

    def test_filter_data(self):
        df = pd.DataFrame({'col1': [1, 2, 3, 4]})
        df_filtered = filter_data(df, 'col1 > 2')
        self.assertEqual(len(df_filtered), 2)

    # Additional tests for other functions...

if __name__ == '__main__':
    unittest.main()
