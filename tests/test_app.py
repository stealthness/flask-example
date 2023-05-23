import unittest

from main_app import app


class MyTestCase(unittest.TestCase):

    def test_something(self):

        web = app.test_client()
        rv = web.get('/')
        self.assertEqual(rv.status == '200 OK')


if __name__ == '__main__':
    unittest.main()
