import unittest
from search_stock import search as s

class SearchTest(unittest.TestCase):
    def test_get_url(self):
        url = "https://finance.yahoo.com/quote/"
        self.assertEqual(s.Search('sndl').get_url(), url)


if __name__ == '__main__':
    unittest.main()
