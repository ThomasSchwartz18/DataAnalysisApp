# tests/test_data_import_export.py

import unittest
import pandas as pd
from src.data_import_export import *

class TestDataImportExport(unittest.TestCase):

    def test_import_csv(self):
        df = import_csv('tests/data/test.csv')
        self.assertIsInstance(df, pd.DataFrame)

    def test_export_csv(self):
        df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        export_csv(df, 'tests/data/export_test.csv')
        df_exported = pd.read_csv('tests/data/export_test.csv')
        pd.testing.assert_frame_equal(df, df_exported)

    # Additional tests for other functions...

if __name__ == '__main__':
    unittest.main()
