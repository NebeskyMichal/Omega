from models.active_record_admins import ActiveRecordAdmins
from models.active_record_users import ActiveRecordUsers
from views.admin_control_view import AdminView
from models.active_record_admins import AdminNotFoundError
from controllers.games_controller import GamesController
from controllers.users_controller import UsersController

import bcrypt


class AdminController:

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

    def login(self, max_attempts=3):
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

    def menu_loop(self):
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

    def password_change(self):
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
            self.admin_view.print_msg("Password didnt match, please try again")
            return False

    def database_statistics(self):
        users_total = self.users_controller.ar_users.total().Count
        bans_total = self.users_controller.ar_bans.total().Count
        reviews_total = self.users_controller.ar_rating.total().Count
        games_total = self.game_controller.game_model.total().Count
        self.admin_view.print_server_statistics(users_total, bans_total, reviews_total, games_total)

    def end_program(self):
        self.admin_view.print_msg("Goodbye!")
        return True
