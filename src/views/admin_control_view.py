class AdminView:
    def __init__(self, menu_barrier):
        self.barrier = menu_barrier

        self.username = None
        self.email = None
        self.password = None
        self.current_input = None

    def print_barrier(self, barrier_char: str = "-"):
        """Metoda pro výpis UI oddělovače

            :param barrier_char: Znak použitý k oddělování
        """
        print(barrier_char * self.barrier)

    def print_msg(self, msg: str):
        """Metoda pro výpis zprávy s oddělovačem"""
        self.print_barrier()
        print(msg)
        self.print_barrier()

    def get_username(self):
        self.print_msg("Enter username:")
        self.username = input()

    def get_email(self):
        self.print_msg("Enter email:")
        self.email = input()

    def get_password(self):
        self.print_msg("Enter password:")
        self.password = input()

    def get_input(self, msg):
        self.current_input = input(msg)

    def game_inputs(self, change_publisher=False, change_title=True, change_release_date=False):
        publisher, title, release_date = "", "", ""
        if change_publisher:
            self.print_msg("Enter publisher name")
            publisher = input()
        if change_title:
            self.print_msg("Enter title")
            title = input()
        if change_release_date:
            self.print_msg("Enter release date")
            release_date = input()

        return publisher, title, release_date

    def pretty_print_game(self, publisher, title, release_date):
        self.print_msg("Game information:")
        print("Publisher:", publisher)
        print("Title:", title)
        print("Release date:", release_date)

    def confirmation(self):
        self.print_msg("Continue = 1 Cancel = 2 Exit = 3")
        return input()

    def print_games_options(self, games):
        self.print_barrier()
        print("No.   Title" + " " * 28 + "Release Date")
        print("-" * 50)
        for i, row in enumerate(games):
            title = f"{i + 1}. {row.title}".ljust(40)
            date = row.release_date.strftime("%Y-%m-%d")
            print(f"{title}{date}")
        self.print_barrier()

    def print_game_reviews(self, reviews):
        self.print_barrier()
        print("Username" + " " * 15 + "Rating" + " " * 5 + "Review")
        print("-" * 50)
        for row in reviews:
            username = row.username.ljust(20)
            rating = str(row.rating).ljust(10)
            review = row.review
            print(f"{username}{rating}{review}")
        self.print_barrier()

    def print_users(self, users):
        self.print_msg("  #  | Username" + " " * 10 + "| Email")
        print("-" * 50)
        for i, row in enumerate(users):
            username = row.username.ljust(20)
            email = row.email
            print(f"{i + 1:3}  | {username}{email}")

    def pretty_print_ban_reason(self, username, email, reason):
        self.print_msg("User ban reason:")
        print("Username:", username)
        print("Email:", email)
        print("Reason:", reason)

    def pretty_print_reports(self, reports):
        self.print_msg("Reports:")
        print("  #  | Reporter" + " " * 10 + "| Reported" + " " * 9 + "| Reason")
        print("-" * 50)
        for i, row in enumerate(reports):
            reporter = row.Reporter.ljust(20)
            reported = row.Reported.ljust(20)
            reason = row.reason
            print(f"{i + 1:3}  | {reporter}{reported}{reason}")
        self.print_barrier()

    def pretty_print_report(self, reporter, reported, reason):
        self.print_msg("Report information:")
        print("Reporter:", reporter)
        print("Reported:", reported)
        print("Reason:", reason)

    def print_game_reviews_for_user(self, user, reviews):
        self.print_barrier()
        print(user + " " * 15 + "Rating" + " " * 5 + "Review")
        print("-" * 50)
        for row in reviews:
            rating = str(row.rating).ljust(10)
            review = row.review
            print(f"{rating}{review}")
        self.print_barrier()

    def print_server_statistics(self, users_total, bans_total, reviews_total, games_total):
        self.print_msg("Server statistics:")
        print("Users registered:", users_total)
        print("Users banned:", bans_total)
        print("Total game reviews:", reviews_total)
        print("Games total in database:", games_total)
        self.print_barrier()
