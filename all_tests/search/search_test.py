import unittest
from search_stock import search as s

class SearchTest(unittest.TestCase):
    def test_url(self):
        url = "https://finance.yahoo.com/quote/"
        a = s.Search('sndl')
        self.assertEqual(a.get_url(), url)


if __name__ == '__main__':
    unittest.main()
