from models.database_connector import DatabaseConnectionSingleton as Connection


class ActiveRecordReports:

    def __init__(self):
        self.connection = Connection.get_instance()
        self._reporter_id = None
        self._reported_id = None
        self._checked = None
        self._reason = None

    @property
    def reporter_id(self):
        return self._reporter_id

    @reporter_id.setter
    def reporter_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Reporter ID must be an integer.")
        self._reporter_id = value

    @property
    def reported_id(self):
        return self._reported_id

    @reported_id.setter
    def reported_id(self, value):
        if not isinstance(value, int):
            raise ValueError("Reported ID must be an integer.")
        self._reported_id = value

    @property
    def checked(self):
        return self._checked

    @checked.setter
    def checked(self, value):
        if not isinstance(value, str) or value not in ["0", "1"]:
            raise ValueError("Checked field must be a string containing either 0 or 1.")
        self._checked = value

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        if not isinstance(value, str):
            raise ValueError("Reason must be a string.")
        self._reason = value

    def save(self):
        sql = "insert into Reports(reported_id, reported_id, checked, reason) values({},{},'{}','{}')" \
            .format(self.reporter_id, self.reported_id, self.checked, self.reason)
        self.connection.query(sql)

    def find_all(self):
        sql = "select Reports.id, reporter.username as Reporter, reported.username as Reported, reason from " \
              "Reports inner join Users as reporter on reporter.id = Reports.reporter_id " \
              "inner join Users as reported on reported.id = reports.reported_id"
        result = self.connection.query(sql, False)
        return result

    def find_not_confirmed(self):
        sql = "select Reports.id, reporter.username as Reporter, reported.username as Reported, reason " \
              "from Reports inner join Users as reporter on reporter.id = Reports.reporter_id " \
              "inner join Users as reported on reported.id = reports.reported_id where checked = '0'"
        result = self.connection.query(sql, False)
        return result

    def confirm_report(self, id):
        sql = "update Reports set checked = '1' where id = {}" \
            .format(id)
        self.connection.query(sql)

    def reports_by_username(self, username):
        sql = "select count(reporter_id) as Count from Reports " \
              "inner join Users on Users.id = Reports.reporter_id where Users.username = '{}'".format(username)
        result = self.connection.query(sql, False)
        for row in result:
            return row
