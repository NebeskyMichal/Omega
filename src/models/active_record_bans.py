from models.database_connector import DatabaseConnectionSingleton as Connection


class ActiveRecordBans:

    def __init__(self):
        self.connection = Connection.get_instance()
        self._user_id = None
        self._admin_id = None
        self._release_date = None
        self._reason = None

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if not isinstance(value, int):
            raise ValueError("User ID must be an integer.")
        self._user_id = value

    @property
    def admin_id(self):
        return self._admin_id

    @admin_id.setter
    def admin_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Admin ID must be an integer.")
        self._admin_id = value

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        if not isinstance(value, str):
            raise ValueError("Release date must be a string.")
        self._release_date = value

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        if not isinstance(value, str):
            raise ValueError("Reason must be a string.")
        self._reason = value

    def save(self):
        sql = "insert into Bans (users_id,admins_id,release_date,reason) values ({},{},'{}','{}')" \
            .format(self.user_id, self.admin_id, self.release_date, self.reason)
        self.connection.query(sql)

    def find_all(self):
        sql = "select Admins.username as Admin, Users.username as Client, Bans.release_date as Issued_on, Bans.reason " \
              "as Reason from Bans inner join Users on Users.id = Bans.users_id " \
              "inner join Admins on Bans.admins_id = Admins.id"
        result = self.connection.query(sql, False)
        return result

    def total(self):
        sql = "select count(*) as Count from Bans"
        result = self.connection.query(sql, False)
        for row in result:
            return row

    def find_if_banned(self, username):
        sql = "select Bans.reason from Bans inner join " \
              "Users on Users.id = Bans.users_id where Users.username='{}'".format(username)
        result = self.connection.query(sql)
        for row in result:
            return row
