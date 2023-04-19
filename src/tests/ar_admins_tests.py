import sys

sys.path.append("src/")

from models.database_connector import DatabaseConnectionSingleton as Connection
from models.active_record_admins import ActiveRecordAdmins, AdminNotFoundError
import unittest


class TestActiveRecordAdmins(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = Connection.get_instance()
        cls.active_record_admins = ActiveRecordAdmins()
        cls.active_record_admins.username = "test_admin"
        cls.active_record_admins.email = "test_admin@example.com"
        cls.active_record_admins.password = "test_password"
        cls.active_record_admins.save()

    def test_save(self):
        username = "admin1"
        email = "admin1@example.com"
        password = "password1"
        active_record_admins = ActiveRecordAdmins()
        active_record_admins.username = username
        active_record_admins.email = email
        active_record_admins.password = password
        active_record_admins.save()
        result = self.connection.query("select * from Admins where username ='{}' and email ='{}'"
                                       .format(username, email))
        self.assertEqual(result[0][1], username)
        self.assertEqual(result[0][2], email)
        self.assertEqual(result[0][3], password)
        self.connection.query("delete from Admins where username ='{}' and email ='{}'".format(username, email))

    def test_update(self):
        username = "test_admin2"
        email = "test_admin2@example.com"
        password = "test_password2"
        self.active_record_admins.update(username, email, password)
        result = self.connection.query("select * from Admins where username ='{}' and email ='{}' and password ='{}'"
                                       .format(username, email, password))
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][1], username)
        self.assertEqual(result[0][2], email)
        self.assertEqual(result[0][3], password)

    def test_update_password(self):
        password = "new_password"
        self.active_record_admins.password = password
        self.active_record_admins.update_password()
        result = self.connection.query("select * from Admins where username ='{}' and email ='{}' and password ='{}'"
                                       .format(self.active_record_admins.username,
                                               self.active_record_admins.email,
                                               password))
        self.assertEqual(result[0][3], password)

    def test_find(self):
        result = self.active_record_admins.find(self.active_record_admins.username, self.active_record_admins.email)
        self.assertEqual(result[1], self.active_record_admins.username)
        self.assertEqual(result[2], self.active_record_admins.email)
        self.assertEqual(result[3], self.active_record_admins.password)

    def test_find_id_by_username(self):
        result = self.active_record_admins.find_id_by_username()
        self.assertIsNotNone(result)

    def test_delete(self):
        username = "admin2"
        email = "admin2@example.com"
        password = "password2"
        active_record_admins = ActiveRecordAdmins()
        active_record_admins.username = username
        active_record_admins.email = email
        active_record_admins.password = password
        active_record_admins.save()
        active_record_admins.delete(username, email)
        result = self.connection.query("select * from Admins where username ='{}' and email ='{}'"
                                       .format(username, email))
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
