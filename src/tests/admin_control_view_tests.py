import unittest
from unittest.mock import patch
from io import StringIO
from datetime import datetime
from views.admin_control_view import AdminView


class TestAdminView(unittest.TestCase):

    def setUp(self):
        self.admin_view = AdminView(menu_barrier=40)

    def test_print_barrier(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.admin_view.print_barrier(barrier_char='*')
            expected_output = '*' * 40 + '\n'
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_print_msg(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.admin_view.print_msg(msg='This is a message')
            expected_output = '-' * 40 + '\nThis is a message\n' + '-' * 40 + '\n'
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_get_username(self):
        with patch('builtins.input', return_value='test_user'):
            self.admin_view.get_username()
            self.assertEqual(self.admin_view.username, 'test_user')

    def test_get_email(self):
        with patch('builtins.input', return_value='test_email'):
            self.admin_view.get_email()
            self.assertEqual(self.admin_view.email, 'test_email')

    def test_get_password(self):
        with patch('builtins.input', return_value='test_password'):
            self.admin_view.get_password()
            self.assertEqual(self.admin_view.password, 'test_password')

    def test_get_input(self):
        with patch('builtins.input', return_value='test_input'):
            self.admin_view.get_input(msg='Enter input:')
            self.assertEqual(self.admin_view.current_input, 'test_input')

    def test_game_inputs(self):
        with patch('builtins.input', side_effect=['test_publisher', 'test_title', 'test_release_date']):
            result = self.admin_view.game_inputs(change_publisher=True, change_title=True, change_release_date=True)
            expected_output = ('test_publisher', 'test_title', 'test_release_date')
            self.assertEqual(result, expected_output)

    def test_confirmation(self):
        with patch('builtins.input', return_value='1'):
            self.assertEqual(self.admin_view.confirmation(), '1')
