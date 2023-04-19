from models.database_connector import DatabaseConnectionSingleton as Connection


class AdminNotFoundError(Exception):
    pass


class ActiveRecordAdmins:

    def __init__(self):
        self.connection = Connection.get_instance()
        self._username = None
        self._email = None
        self._password = None

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def save(self):
        sql = "insert into Admins (username,email,password) values ('{}','{}','{}')" \
            .format(self.username, self.email, self.password)
        self.connection.query(sql)

    def update(self, username, email, password):
        sql = "update Admins set username = '{}', email = '{}', password = '{}' " \
              "where username = '{}' and email = '{}' and password = '{}'" \
            .format(username, email, password, self.username, self.email, self.password)
        self.username = username
        self.email = email
        self.password = password
        self.connection.query(sql)

    def update_password(self):
        sql = "update Admins set password = '{}' where username = '{}' and email = '{}' " \
            .format(self.password, self.username, self.email)
        self.connection.query(sql)

    def find(self, username, email):
        sql = "select * from Admins where username ='{}' and email ='{}'".format(username, email)
        result = self.connection.query(sql, False)
        if len(result) == 0:
            raise AdminNotFoundError(f"No admin user found with username or email '{username}'")
        for row in result:
            return row

    def find_id_by_username(self):
        sql = "select * from Admins where username = '{}'".format(self.username)
        result = self.connection.query(sql, False)
        for row in result:
            return row.id

    def delete(self, username, email):
        sql = "delete from Admins where username ='{}' and email ='{}'" \
            .format(username, email)
        self.username = None
        self.email = None
        self.password = None
        self.connection.query(sql)
