from models.active_record_users import ActiveRecordUsers
import bcrypt
import re


class ClientController:

    def __init__(self):
        self.users = ActiveRecordUsers()

    def login(self, username, email, password):
        try:
            hashed_passwd = self.users.find(username, email).password
        except AttributeError:
            return False
        if bcrypt.checkpw(password.encode("UTF-8"), hashed_passwd.encode("UTF-8")):
            return True
        else:
            return False

    def password_change(self, username, email, current_password, pass1, pass2):
        db_hashed_password = self.users.find(username, email).password
        provided_password = current_password.encode("UTF-8")
        if bcrypt.checkpw(provided_password, db_hashed_password.encode("UTF-8")):
            if pass1 == pass2:
                self.users.username = username
                self.users.email = email
                if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^\w\d\s:])([^\s]){8,}$', pass1):
                    return False
                pswd = str(bcrypt.hashpw(pass1.encode("UTF-8"), bcrypt.gensalt(rounds=12)))
                self.users.password = pswd[2:len(pswd) - 1]
                self.users.update_password()
                return True
        return False

    def register(self, username, email, password, password_check):
        if not username or not email or not password or not password_check:
            return "All fields are required"
        if not re.match(r'^\w{4,20}$', username):
            return "Username must be 4-20 characters long and contain only alphanumeric characters and underscores"
        if not re.match(r'^[\w\.-]+@[\w\.-]+(\.[\w]+)+$', email):
            return "Invalid email address"

        if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^\w\d\s:])([^\s]){8,}$', password):
            return "Password must be at least 8 characters long and contain at least one uppercase letter, " \
                   "one lowercase letter, one digit, and one special character"

        if password != password_check:
            return "Passwords do not match"

        self.users.username = username
        self.users.email = email
        pswd = str(bcrypt.hashpw(password.encode("UTF-8"), bcrypt.gensalt(rounds=12)))
        self.users.password = pswd[2:len(pswd) - 1]
        self.users.save()

        return True
