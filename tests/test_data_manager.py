import os
import unittest

from data_manager import SimpleDataManager

test_user_names = ['Quiton', 'Rodger', 'Stan', 'Tom', 'Ursula', 'Vince', 'Won', 'Xavier', 'Yoon', 'Zed']
db_filename = os.path.join('../', 'res', 'test_user_db.db')
csv_users_filename = os.path.join('../', 'res', 'full_user_data.csv')

class MyTestCase(unittest.TestCase):

    def test_something(self):
        data = SimpleDataManager()
        data.create_tables(db_filename)
        data.load_users_from_db(csv_users_filename, db_filename)
        users = data.get_user_list(db_filename)
        for name in users:
            if name not in test_user_names:
                self.fail(f'fail: {name}')
        self.assertEqual(10, len(users))


if __name__ == '__main__':
    unittest.main()
