from views.user_menu_view import UserMenuView
from views.registration_view import RegistrationView
from views.password_change_view import PasswordChangeView
from views.user_profile_view import UserProfileView
from views.search_view import SearchView
from views.game_review_view import GameReviewView
from views.game_list_view import GameListView
from views.game_list_user_view import GameUserListView

from models.active_record_ratings import ActiveRecordRatings
from models.active_record_reports import ActiveRecordReports
from models.active_record_games import ActiveRecordGames
from models.active_record_users import ActiveRecordUsers

from tkinter import messagebox
from controllers.client_controller import ClientController


def alert_window(msg):
    messagebox.showwarning("Alert", msg)


class GuiController:

    def __init__(self):
        self.user_controller = ClientController()
        self.ar_ratings = ActiveRecordRatings()
        self.ar_reports = ActiveRecordReports()
        self.ar_games = ActiveRecordGames()
        self.ar_users = ActiveRecordUsers()

    def move_to_user_menu(self, user_login, username, email, password):
        if self.user_controller.login(username, email, password):
            user_login.destroy()
            rating_count = self.ar_ratings.find_by_user_username(username).Count
            mean_score = self.ar_ratings.get_mean_score(username).Count
            reports_given = self.ar_reports.reports_by_username(username).Count
            user_menu = UserMenuView(self, username, email, password, rating_count, mean_score, reports_given)
            return True
        alert_window("Login failed, please try again")
        return False

    def move_to_password_change(self, current_window, username, email, password):
        current_window.destroy()
        app = PasswordChangeView(self, username, email, password)

    def open_registration(self, user_login):
        user_login.destroy()
        reg_view = RegistrationView(user_login.gui)

    def return_to_login(self, current_window, option=False):
        from views.login_view import LoginView
        if option:
            alert_window("Password change was successful.\nPlease login again!")
        current_window.destroy()
        app = LoginView()

    def open_user_profile(self, current_window, searched_user, username, email, password):

        rating_count = self.ar_ratings.find_by_user_username(searched_user).Count
        if rating_count == 0:
            alert_window("User not found")
            return False
        mean_score = self.ar_ratings.get_mean_score(searched_user).Count
        reports_given = self.ar_reports.reports_by_username(searched_user).Count
        current_window.destroy()
        app = UserProfileView(self, searched_user, rating_count, mean_score, reports_given, username, email, password)

    def register_user(self, current_window, username, email, password, password_check):
        result = self.user_controller.register(username, email, password, password_check)
        if result != True:
            alert_window(result)
            return False
        alert_window("Registration successful")
        self.return_to_login(current_window)
        return True

    def change_password(self, current_window, username, email, current_password, pass1, pass2):
        if self.user_controller.password_change(username, email, current_password, pass1, pass2):
            self.return_to_login(current_window, True)
            return True
        alert_window("Password change was not successful, please try again!")

    def open_search_window(self, current_window, username, email, password, option):
        current_window.destroy()
        SearchView(self, username, email, password, option)

    def open_game_review_form(self, current_window, username, email, password):
        current_window.destroy()
        GameReviewView(self, username, email, password)

    def open_game_list(self):
        data = self.ar_games.get_game_ratings()
        GameListView(data)

    def open_user_game_list(self, username):
        data = self.ar_ratings.get_game_ratings_for_user(username)
        GameUserListView(data)

    def send_review(self,username, email, game_to_review, rating, review):
        print(game_to_review)
        print(rating)
        print(review)
        try:
            rating = float(rating)
            if rating < 1 or rating > 10:
                raise ValueError
        except ValueError:
            alert_window("Error: rating must be a number between 1 and 10")
            return False
        else:
            if not game_to_review:
                alert_window("Error: game title cannot be empty")
                return False
            elif not review:
                alert_window("Warning: review is empty")
                return False
        try:
            user_id = self.ar_users.find(username,email).id
            game_id = self.ar_games.find_by_title(game_to_review).id
            self.ar_ratings.users_id = int(user_id)
            self.ar_ratings.game_id = int(game_id)
            self.ar_ratings.rating = int(rating)
            self.ar_ratings.review = review
            self.ar_ratings.save()
            alert_window("Review was successfully added")
            return True
        except:
            alert_window("This game does not exist")
            return False





