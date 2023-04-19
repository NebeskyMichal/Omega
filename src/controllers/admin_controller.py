from models.active_record_admins import ActiveRecordAdmins
from models.active_record_users import ActiveRecordUsers
from views.admin_control_view import AdminView
from models.active_record_admins import AdminNotFoundError
from controllers.games_controller import GamesController
from controllers.users_controller import UsersController

import bcrypt


class AdminController:
    """Controller class for interaction with admin interface"""
    def __init__(self):
        self.admins = ActiveRecordAdmins()
        self.admin_view = AdminView(50)
        self.game_controller = GamesController(self.admin_view)
        self.users_controller = UsersController(self.admin_view, self)
        self.commands = [("Manage games", self.game_controller.game_menu),
                         ("Manage users", self.users_controller.user_management),
                         ("Change password", self.password_change),
                         ("Check statistics", self.database_statistics),
                         ("End program", self.end_program)
                         ]
        self.username = None
        self.email = None
        self.menu_loop()

    def login(self, max_attempts: int = 3) -> bool:
        """This method asks for credentials and gives 3 attempts to login for admin

            :param max_attempts: number of attempts
            :return: True or False based on if login was successful or not
        """
        for attempt in reversed(range(1, max_attempts + 1)):
            self.admin_view.print_msg(f"Please login, you have {attempt} attempts")
            self.admin_view.get_username()
            self.admin_view.get_email()
            self.admin_view.get_password()
            try:
                db_hashed_password = self.admins.find(self.admin_view.username, self.admin_view.email).password
                provided_password = self.admin_view.password.encode("UTF-8")
                if bcrypt.checkpw(provided_password, db_hashed_password.encode("UTF-8")):
                    self.admin_view.print_msg("Successfully logged in")
                    self.username = self.admin_view.username
                    self.email = self.admin_view.email
                    self.users_controller = UsersController(self.admin_view, self.username)
                    return True
                else:
                    self.admin_view.print_msg("Incorrect password")
            except AdminNotFoundError:
                self.admin_view.print_msg("Admin not found")
            except Exception as e:
                self.admin_view.print_msg(f"Error: {str(e)}")
        self.admin_view.print_msg("Failed to login")
        return False

    def menu_loop(self) -> bool:
        """This method loops through menu and is waiting for input from admin,
            based on choice it sends admin to another method using Command Pattern

            :return: True or False based on if the choice in menu is Exit or not
        """
        if not self.login():
            return False
        self.admin_view.print_barrier()
        user_input = None
        while user_input not in range(len(self.commands) + 1):
            num = 0
            for header, method in self.commands:
                num += 1
                print(str(num) + ". " + header)
            self.admin_view.print_barrier()
            try:
                self.admin_view.get_input("Choose which action you want to run")
                user_input = int(self.admin_view.current_input)
                if (user_input < 0) or (user_input > len(self.commands)):
                    raise Exception()
            except:
                print("Invalid action, please try again")
                user_input = None

            res = self.commands[user_input - 1][1]()
            if res:
                return False
            user_input = None

    def password_change(self) -> bool:
        """This method asks admin for old password and two times new password
            checks for correctness of inputs and if the new passwords are same

            :return: True or False if the password was change or not
        """
        self.admin_view.get_input("Please enter your password again")
        pswd = self.admin_view.current_input
        db_hashed_password = self.admins.find(self.username, self.email).password
        provided_password = pswd.encode("UTF-8")
        if bcrypt.checkpw(provided_password, db_hashed_password.encode("UTF-8")):
            self.admin_view.get_input("Please enter your new password")
            pass1 = self.admin_view.current_input
            self.admin_view.get_input("Please enter your new password again")
            pass2 = self.admin_view.current_input
            if pass1 == pass2:
                self.admins.username = self.admin_view.username
                pswd = str(bcrypt.hashpw(pass1.encode("UTF-8"), bcrypt.gensalt(rounds=12)))
                self.admins.password = pswd[2:len(pswd) - 1]
                self.admins.update_password()
                return
            self.admin_view.print_msg("Password didn't match, please try again")
            return False

    def database_statistics(self):
        """This method asks Models for data and returns them to view to print them"""
        users_total = self.users_controller.ar_users.total().Count
        bans_total = self.users_controller.ar_bans.total().Count
        reviews_total = self.users_controller.ar_rating.total().Count
        games_total = self.game_controller.game_model.total().Count
        self.admin_view.print_server_statistics(users_total, bans_total, reviews_total, games_total)

    def end_program(self) -> bool:
        """This method gives farewell to user and ends program

            :return: True for ending the program
        """
        self.admin_view.print_msg("Goodbye!")
        return True
