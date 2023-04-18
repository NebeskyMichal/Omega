from models.database_connector import DatabaseConnectionSingleton as Connection


class ActiveRecordUsers:

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
        if not isinstance(value, str):
            raise TypeError('Username must be a string')
        if len(value) < 4:
            raise ValueError('Username must be at least 4 characters long')
        self._username = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError('Email must be a string')
        if '@' not in value:
            raise ValueError('Invalid email address')
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('Password must be a string')
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characters long')
        self._password = value

    def save(self):
        sql = "insert into Users (username,email,password) values ('{}','{}','{}')" \
            .format(self.username, self.email, self.password)
        self.connection.query(sql)

    def update(self, username, email, password):
        sql = "update Users set username = '{}', email = '{}', password = '{}' " \
              "where username = '{}' and email = '{}' and password = '{}'" \
            .format(username, email, password, self.username, self.email, self.password)
        self.username = username
        self.email = email
        self.password = password
        self.connection.query(sql)

    def find(self, username, email):
        sql = "select * from Users where username ='{}' and email ='{}'".format(username, email)
        result = self.connection.query(sql)
        for row in result:
            return row

    def find_all(self):
        sql = "select * from Users"
        result = self.connection.query(sql)
        return result

    def find_all_not_banned(self):
        sql = "SELECT Users.id, Users.username, Users.email, Users.password FROM Users " \
              "LEFT JOIN Bans ON Users.id = Bans.users_id WHERE Bans.id IS NULL"
        result = self.connection.query(sql)
        return result

    def delete(self, username, email):
        sql = "delete from Users where username ='{}' and email ='{}'" \
            .format(username, email)
        self.username = None
        self.email = None
        self.password = None
        self.connection.query(sql)

    def update_password(self):
        sql = "update Users set password = '{}' where username = '{}' and email = '{}' " \
            .format(self.password, self.username, self.email)
        self.connection.query(sql)

    def total(self):
        sql = "select count(*) as Count from Users"
        result = self.connection.query(sql)
        for row in result:
            return row
