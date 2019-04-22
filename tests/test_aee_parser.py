import unittest
from aee_parser import get_url, find_articles


class TestGetUrl(unittest.TestCase):
    SITE = "https://www.allearsenglish.com/episodes/"
    TIMEOUT = "http://example.com:8000"
    STATUS_CODE = "http://ya.ru/33"

    def test_timeout(self):
        result = get_url(self.TIMEOUT)
        self.assertIsNone(result)

    def test_status_code(self):
        result = get_url(self.STATUS_CODE)
        self.assertIsNone(result)

    def test_page_is_valid(self):
        result = get_url(self.SITE)
        self.assertIsInstance(result, str)


class TestFindArticles(unittest.TestCase):
    with open("tests/pages/page-2.html") as f:
        page = f.read()

    def test_valid_data(self):
        articles = find_articles(self.page)
        self.assertIsInstance(articles, list)
        self.assertGreater(len(articles), 3)

    def test_not_valid_page_result(self):
        articles = find_articles(None)
        self.assertIs(articles, None)


if __name__ == '__main__':
    unittest.main()
