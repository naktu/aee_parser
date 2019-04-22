import unittest
from aee_parser import get_url


class TestGetUrl(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_timeout(self):
        result = get_url("http://example.com:8000")
        self.assertDictEqual(result, {"status": 1, "data": "ConnectionError"})

    def test_status_code(self):
        result = get_url("http://ya.ru/33")
        self.assertDictEqual(result, {"status": 1, "data": 'Http error: 404'})


if __name__ == '__main__':
    unittest.main()
