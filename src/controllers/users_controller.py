import datetime

from models.active_record_users import ActiveRecordUsers
from models.active_record_admins import ActiveRecordAdmins
from models.active_record_bans import ActiveRecordBans
from models.active_record_reports import ActiveRecordReports
from models.active_record_ratings import ActiveRecordRatings


class UsersController:

    def __init__(self, admin_view, admin_controller):
        self.ar_users = ActiveRecordUsers()
        self.ar_admins = ActiveRecordAdmins()
        self.ar_bans = ActiveRecordBans()
        self.ar_reports = ActiveRecordReports()
        self.ar_rating = ActiveRecordRatings()

        self.admin_view = admin_view
        self.admin_controller = admin_controller
        self.commands = [("Ban user", self.ban_user),
                         ("View reports", self.view_reports),
                         ("Statistics for certain user", self.user_stats),
                         ("Return to main menu", self.return_to_main_menu)
                         ]

    def user_management(self):
        user_input = None
        while user_input not in range(len(self.commands) + 1):
            num = 0
            self.admin_view.print_barrier()
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
            try:
                res = self.commands[user_input - 1][1]()
                if res is False:
                    return False
            except:
                self.admin_view.print_msg("Invalid action, please try again")

    def ban_user(self):
        banning = True
        while banning:
            try:
                users = self.ar_users.find_all_not_banned()
                self.admin_view.print_users(users)
                self.admin_view.get_input("Please select a user to ban")
                user = users[int(self.admin_view.current_input) - 1]
                self.admin_view.get_input("Please insert a reason for ban")
                reason = self.admin_view.current_input
                self.admin_view.pretty_print_ban_reason(user.username, user.email, reason)
                try:
                    confirmation = self.admin_view.confirmation()
                    if confirmation == "1":
                        self.ar_admins.username = str(self.admin_controller.username)
                        admin_id = self.ar_admins.find_id_by_username()
                        self.ar_bans.user_id = user.id
                        self.ar_bans.admin_id = admin_id
                        current_date = datetime.datetime.now()
                        formatted_date = current_date.strftime("%Y-%m-%d")
                        self.ar_bans.release_date = formatted_date
                        self.ar_bans.reason = reason
                        self.ar_bans.save()
                        self.admin_view.print_msg("User has been successfully banned")
                        banning = False
                    elif confirmation == "2":
                        pass
                    else:
                        banning = False
                except:
                    self.admin_view.print_msg("There was an error banning user")
            except:
                self.admin_view.print_msg("Error choosing user")

    def view_reports(self):
        reporting = True
        while reporting:
            try:
                reports = self.ar_reports.find_not_confirmed()
                self.admin_view.pretty_print_reports(reports)
                self.admin_view.get_input("Please select a report to check")
                report = reports[int(self.admin_view.current_input) - 1]
                self.admin_view.pretty_print_report(report.Reporter, report.Reported, report.reason)
                self.admin_view.print_msg("Do you really want to check this report?")
                try:
                    confirmation = self.admin_view.confirmation()
                    if confirmation == "1":
                        self.ar_reports.confirm_report(report.id)
                        self.admin_view.print_msg("Report was successfully approved")
                        reporting = False
                    elif confirmation == "2":
                        pass
                    else:
                        reporting = False
                except:
                    self.admin_view.print_msg("There was a error with checking the report")
            except:
                self.admin_view.print_msg("Error choosing report")

    def user_stats(self):
        users = self.ar_users.find_all_not_banned()
        self.admin_view.print_users(users)
        self.admin_view.get_input("Please select a user to check reviews of")
        user = users[int(self.admin_view.current_input) - 1]
        reviews = self.ar_rating.find_by_user_id(user.id)
        self.admin_view.print_game_reviews_for_user(user.username, reviews)

    def return_to_main_menu(self):
        self.admin_view.print_msg("Returning to main menu...")
        return False
