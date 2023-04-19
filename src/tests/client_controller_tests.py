import unittest
from unittest.mock import Mock, patch
from controllers.client_controller import ClientController


class TestClientController(unittest.TestCase):

    def setUp(self):
        self.client_controller = ClientController()

    def test_login_success(self):
        self.client_controller.users.find = Mock(
            return_value=Mock(password='$2b$12$N6yX9hmE2ULVvD1fB/8VZubD6U3F6ofD.iJiW8m9a1lghd7hqAbCK'))
        result = self.client_controller.login("test_user", "test@test.com", "Test1234@")
        self.assertTrue(not result)

    def test_login_failure(self):
        self.client_controller.users.find = Mock(side_effect=AttributeError)
        result = self.client_controller.login("test_user", "test@test.com", "Test1234@")
        self.assertFalse(result)

    def test_register_success(self):
        self.client_controller.users.save = Mock()
        result = self.client_controller.register("test_user", "test@test.com", "Test1234@", "Test1234@")
        self.assertTrue(result)
        self.client_controller.users.save.assert_called_once()

    def test_register_failure(self):
        result = self.client_controller.register("", "", "", "")
        self.assertEqual(result, "All fields are required")
        result = self.client_controller.register("a", "test@test.com", "Test1234@", "Test1234@")
        self.assertEqual(result,
                         "Username must be 4-20 characters long and contain only alphanumeric characters and underscores")
        result = self.client_controller.register("test_user", "invalid_email", "Test1234@", "Test1234@")
        self.assertEqual(result, "Invalid email address")
        result = self.client_controller.register("test_user", "test@test.com", "password", "password")
        self.assertEqual(result,
                         "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character")
        result = self.client_controller.register("test_user", "test@test.com", "Test1234@", "DifferentPassword1234@")
        self.assertEqual(result, "Passwords do not match")
