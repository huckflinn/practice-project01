import pandas as pd
import unittest
from unittest.mock import patch

from src.process_data import extract_data


class TestExtraction(unittest.TestCase):

    @patch("pandas.read_parquet")
    def test_extract_data(self, mock_read_parquet):
        mock_df = pd.DataFrame({
            "id": [1, 2, 3],
            "trip": ['a', 'b', 'c'],
            "date": ["1970-01-01", "2000-01-01", "2012-12-12"]
        })

        mock_read_parquet.return_value = mock_df

        res = extract_data("dummy_file.parquet")

        self.assertIs(res, mock_df)
        mock_read_parquet.assert_called_once_with("dummy_file.parquet")

    
    def test_file_not_found(self):
        fake_file = "not_real.parquet"

        with self.assertRaises(FileNotFoundError):
            extract_data(fake_file)