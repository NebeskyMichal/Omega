from models.active_record_games import ActiveRecordGames
from models.active_record_publishers import ActiveRecordPublishers
from models.active_record_ratings import ActiveRecordRatings


class GamesController:

    def __init__(self, admin_view):
        self.admin_view = admin_view
        self.game_model = ActiveRecordGames()
        self.publisher_model = ActiveRecordPublishers()
        self.ratings_model = ActiveRecordRatings()
        self.commands = [("Add game", self.add_game),
                         ("Edit game title", self.edit_game_title),
                         ("Edit game release date", self.edit_game_date),
                         ("Delete game", self.delete_game),
                         ("Add publisher", self.add_publisher),
                         ("Statistics for certain game", self.stats_for_game),
                         ("Return to main menu", self.return_to_main_menu)
                         ]

    def game_menu(self):
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

    def add_game(self):
        adding = True
        while adding:
            publisher, title, release_date = self.admin_view.game_inputs(True, True, True)
            self.admin_view.pretty_print_game(publisher, title, release_date)
            try:
                confirmation = self.admin_view.confirmation()
                if confirmation == "1":
                    self.game_model.title = title
                    self.game_model.release_date = str(release_date)
                    self.game_model.insert_if_not_found(publisher)
                    self.admin_view.print_msg("Game added successfully")
                    adding = False
                elif confirmation == "2":
                    pass
                else:
                    adding = False
            except Exception:
                self.admin_view.print_msg("There was an error adding game")

    def edit_game_title(self):
        editing = True
        while editing:
            result = self.game_model.find_all()
            self.admin_view.print_games_options(result)
            try:
                self.admin_view.get_input("Select which game title you want to edit")
                selected_game = result[int(self.admin_view.current_input) - 1]
                publisher_name = self.publisher_model.find_by_id(int(selected_game.publisher_id)).name
                self.admin_view.pretty_print_game(publisher_name, selected_game.title, selected_game.release_date)
                self.admin_view.get_input("Please insert new title")
                new_title = self.admin_view.current_input
                self.admin_view.pretty_print_game(publisher_name, new_title, selected_game.release_date)
                try:
                    confirmation = self.admin_view.confirmation()
                    if confirmation == "1":
                        self.game_model.title = selected_game.title
                        self.game_model.release_date = str(selected_game.release_date)
                        self.game_model.update_title(new_title)
                        self.admin_view.print_msg("Title was successfully updated")
                        editing = False
                    elif confirmation == "2":
                        pass
                    else:
                        editing = False
                except:
                    self.admin_view.print_msg("There was an error editing game")
            except:
                self.admin_view.print_msg("Error while choosing game")

    def edit_game_date(self):
        editing = True
        while editing:
            result = self.game_model.find_all()
            self.admin_view.print_games_options(result)
            try:
                self.admin_view.get_input("Select which game release_date you want to edit")
                selected_game = result[int(self.admin_view.current_input) - 1]
                publisher_name = self.publisher_model.find_by_id(int(selected_game.publisher_id)).name
                self.admin_view.pretty_print_game(publisher_name, selected_game.title, selected_game.release_date)
                self.admin_view.get_input("Please insert new release date")
                new_release_date = self.admin_view.current_input
                self.admin_view.pretty_print_game(publisher_name, selected_game.title, new_release_date)
                try:
                    confirmation = self.admin_view.confirmation()
                    if confirmation == "1":
                        self.game_model.title = selected_game.title
                        self.game_model.release_date = str(selected_game.release_date)
                        self.game_model.update_release_date(new_release_date)
                        self.admin_view.print_msg("Release date was successfully updated")
                        editing = False
                    elif confirmation == "2":
                        pass
                    else:
                        editing = False
                except:
                    self.admin_view.print_msg("There was an error editing game")
            except:
                self.admin_view.print_msg("Error while choosing game")

    def delete_game(self):
        deleting = True
        while deleting:
            result = self.game_model.find_all()
            self.admin_view.print_games_options(result)
            try:
                self.admin_view.get_input("Select which game you want to delete")
                selected_game = result[int(self.admin_view.current_input) - 1]
                publisher_name = self.publisher_model.find_by_id(int(selected_game.publisher_id)).name
                self.admin_view.pretty_print_game(publisher_name, selected_game.title, selected_game.release_date)
                self.admin_view.print_msg("Do you really  want to delete this game?")
                try:
                    confirmation = self.admin_view.confirmation()
                    if confirmation == "1":
                        self.game_model.title = selected_game.title
                        self.game_model.release_date = str(selected_game.release_date)
                        self.game_model.publisher_id = selected_game.publisher_id
                        self.game_model.delete()
                        self.admin_view.print_msg("The game was successfully deleted")
                        deleting = False
                    elif confirmation == "2":
                        pass
                    else:
                        deleting = False
                except:
                    self.admin_view.print_msg("There was an error deleting game")
            except:
                self.admin_view.print_msg("Error while choosing game")

    def stats_for_game(self):
        stats = True
        while stats:
            result = self.game_model.find_all()
            self.admin_view.print_games_options(result)
            try:
                self.admin_view.get_input("Select which reviews you want to see")
                selected_game = result[int(self.admin_view.current_input) - 1]
                publisher_name = self.publisher_model.find_by_id(int(selected_game.publisher_id)).name
                self.admin_view.pretty_print_game(publisher_name, selected_game.title, selected_game.release_date)
                try:
                    confirmation = self.admin_view.confirmation()
                    if confirmation == "1":
                        result = self.ratings_model.find_by_game_title(selected_game.title)
                        self.admin_view.print_game_reviews(result)
                        stats = False
                    elif confirmation == "2":
                        pass
                    else:
                        stats = False
                except:
                    self.admin_view.print_msg("There was an error selecting statistics of chosen game")
            except:
                self.admin_view.print_msg("Error while choosing game")

    def add_publisher(self):
        adding = True
        while adding:
            publisher, title, release_date = self.admin_view.game_inputs(True, False, False)
            self.admin_view.print_msg("Do you want publisher with this name? " + publisher)
            try:
                confirmation = self.admin_view.confirmation()
                if confirmation == "1":
                    self.publisher_model.name = publisher
                    self.publisher_model.insert_if_not_found()
                    adding = False
                elif confirmation == "2":
                    pass
                else:
                    adding = False
            except Exception:
                self.admin_view.print_msg("There was an error adding publisher")

    def return_to_main_menu(self):
        self.admin_view.print_msg("Returning to main menu...")
        return False
