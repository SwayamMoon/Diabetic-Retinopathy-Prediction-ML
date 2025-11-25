import os
import unittest

class TestCSVExists(unittest.TestCase):
    def test_csv_file_exists(self):
        self.assertTrue(os.path.isfile('path/to/your/file.csv'))

if __name__ == '__main__':
    unittest.main()