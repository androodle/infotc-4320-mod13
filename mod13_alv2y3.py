import unittest
from datetime import datetime
import StockDataAnalyzer

class TestStockDataAnalyzer(unittest.TestCase):

    def test_validate_stock_name(self):
        # Test that validate_stock_name function correctly validates stock names
        self.assertTrue(StockDataAnalyzer.validate_stock_name('AAPL'))
        self.assertFalse(StockDataAnalyzer.validate_stock_name('AAPL1'))
        self.assertFalse(StockDataAnalyzer.validate_stock_name(''))
        self.assertFalse(StockDataAnalyzer.validate_stock_name('APPLEINC'))

    def test_validate_chart_type(self):
        # Test that validate_chart_type function correctly validates chart types
        self.assertTrue(StockDataAnalyzer.validate_chart_type('1'))
        self.assertTrue(StockDataAnalyzer.validate_chart_type('2'))
        self.assertFalse(StockDataAnalyzer.validate_chart_type('3'))

    def test_validate_time_series(self):
        # Test that validate_time_series function correctly validates time series
        self.assertTrue(StockDataAnalyzer.validate_time_series('1'))
        self.assertTrue(StockDataAnalyzer.validate_time_series('2'))
        self.assertTrue(StockDataAnalyzer.validate_time_series('3'))
        self.assertTrue(StockDataAnalyzer.validate_time_series('4'))
        self.assertFalse(StockDataAnalyzer.validate_time_series('5'))

    def test_validate_date(self):
        # Test that validate_date function correctly validates dates
        self.assertTrue(StockDataAnalyzer.validate_date('2020-01-01'))
        self.assertFalse(StockDataAnalyzer.validate_date('2020-01-32'))
        self.assertFalse(StockDataAnalyzer.validate_date('2020-13-01'))
        self.assertFalse(StockDataAnalyzer.validate_date('2020-01-1'))
        self.assertFalse(StockDataAnalyzer.validate_date('2020-1-01'))

    def test_validate_date_range(self):
        # Test that validate_date_range function correctly validates date ranges
        self.assertTrue(StockDataAnalyzer.validate_date_range('2020-01-01', '2020-12-31'))
        self.assertFalse(StockDataAnalyzer.validate_date_range('2020-12-31', '2020-01-01'))

    def test_validate_yes_no(self):
        # Test that validate_yes_no function correctly validates yes/no responses
        self.assertTrue(StockDataAnalyzer.validate_yes_no('yes'))
        self.assertTrue(StockDataAnalyzer.validate_yes_no('no'))
        self.assertTrue(StockDataAnalyzer.validate_yes_no('y'))
        self.assertTrue(StockDataAnalyzer.validate_yes_no('n'))
        self.assertFalse(StockDataAnalyzer.validate_yes_no('yes '))
        self.assertFalse(StockDataAnalyzer.validate_yes_no(' no'))
        self.assertFalse(StockDataAnalyzer.validate_yes_no('Y'))
        self.assertFalse(StockDataAnalyzer.validate_yes_no('N'))

if __name__ == '__main__':
    unittest.main()
