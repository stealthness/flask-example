import os

class SimpleDataManager:

    def __init__(self):
        self.users = []

    def load_users(self, filename):
        with open(filename) as csv_file:
            for name in csv_file:
                self.users.append(name.strip())