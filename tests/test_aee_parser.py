import unittest
from aee_parser import get_url


class TestGetUrl(unittest.TestCase):
    SITE = "https://www.allearsenglish.com/episodes/"
    TIMEOUT = "http://example.com:8000"
    STATUS_CODE = "http://ya.ru/33"

    def setUp(self) -> None:
        pass

    def test_timeout(self):
        result = get_url(self.TIMEOUT)
        self.assertDictEqual(result, {"status": 1, "data": "ConnectionError"})

    def test_status_code(self):
        result = get_url(self.STATUS_CODE)
        self.assertDictEqual(result, {"status": 1, "data": 'Http error: 404'})

    def test_page_is_valid(self):
        result = get_url(self.SITE)
        self.assertEqual(0, result['status'])
        self.assertIsInstance(result['data'], str)


if __name__ == '__main__':
    unittest.main()
