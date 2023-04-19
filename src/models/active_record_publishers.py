from models.database_connector import DatabaseConnectionSingleton as Connection


class ActiveRecordPublishers:
    def __init__(self):
        self.connection = Connection.get_instance()
        self._name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string')
        if len(value) < 2:
            raise ValueError('Name must be at least 2 characters long')
        self._name = value

    def save(self):
        sql = "insert into Publishers (name) values ('{}')".format(self.name)
        self.connection.query(sql)

    def update(self, name):
        sql = "update Publishers set name = {} where name = {}".format(name, self.name)
        self.name = name
        self.connection.query(sql)

    def delete(self):
        sql = "delete from Publishers where name = {}".format(self.name)
        self.connection.query(sql)

    def find(self):
        sql = "select * from Publishers where name = '{}'".format(self.name)
        result = self.connection.query(sql, False)
        for row in result:
            return row

    def find_by_id(self, id):
        sql = "select * from Publishers where id = {}".format(id)
        result = self.connection.query(sql, False)
        for row in result:
            return row

    def insert_if_not_found(self):
        res = self.find()
        if res is None:
            self.save()
            return True
        return res.id
