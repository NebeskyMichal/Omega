from models.database_connector import DatabaseConnectionSingleton as Connection
from models.active_record_publishers import ActiveRecordPublishers
import datetime


class ActiveRecordGames:

    def __init__(self):
        self.connection = Connection.get_instance()
        self.ar_publishers = ActiveRecordPublishers()
        self._publisher_id = None
        self._title = None
        self._release_date = None
        self._global_rating = 0

    @property
    def publisher_id(self):
        return self._publisher_id

    @publisher_id.setter
    def publisher_id(self, value):
        if not isinstance(value, int):
            raise TypeError('Publisher ID must be an integer')
        if value < 1:
            raise ValueError('Publisher ID must be greater than 0')
        self._publisher_id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError('Title must be a string')
        if len(value) < 2:
            raise ValueError('Title must be at least 2 characters long')
        self._title = value

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        if not isinstance(value, str):
            raise TypeError('Release date must be a string in the format YYYY-MM-DD')
        try:
            datetime.datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Incorrect date format, should be YYYY-MM-DD')
        self._release_date = value

    @property
    def global_rating(self):
        return self._global_rating

    @global_rating.setter
    def global_rating(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError('Global rating must be a float or an integer')
        if value < 0 or value > 10:
            raise ValueError('Global rating must be between 0 and 10')
        self._global_rating = value

    def save(self):
        sql = "insert into Games (publisher_id, title, release_date, global_rating) values ({},'{}','{}',{})" \
            .format(self.publisher_id, self.title, self.release_date, self.global_rating)
        self.connection.query(sql)

    def update(self, publisher_id, title, release_date, global_rating):
        sql = "update Games set publisher_id={}, title='{}', release_date='{}' where " \
              "publisher_id={} and title='{}' and release_date='{}' and global_rating={}" \
            .format(publisher_id, title, release_date, self.publisher_id, self.title,
                    self.release_date, self.global_rating)
        self.publisher_id = publisher_id
        self.title = title
        self.release_date = release_date
        self.global_rating = global_rating
        self.connection.query(sql)

    def update_title(self, new_title):
        sql = "update Games set title='{}' where title='{}' and release_date = '{}'" \
            .format(new_title, self.title, self.release_date)
        self.connection.query(sql)

    def update_release_date(self, new_release_date):
        sql = "update Games set release_date='{}' where title='{}' and release_date = '{}'" \
            .format(new_release_date, self.title, self.release_date)
        self.connection.query(sql)

    def delete(self):
        sql = "delete from Games where publisher_id={} and title='{}' and release_date='{}'" \
            .format(self.publisher_id, self.title, self.release_date)
        self.connection.query(sql)

    def find(self):
        sql = "select * from Games where title='{}' and release_date='{}'".format(self.title, self.release_date)
        result = self.connection.query(sql, False)
        for row in result:
            return row

    def find_all(self):
        sql = "select * from Games"
        result = self.connection.query(sql, False)
        return result

    def get_game_ratings(self):
        sql = "select title, global_rating from Games"
        result = self.connection.query(sql, False)
        return result

    def insert_if_not_found(self, publisher):
        res = self.find()
        if res is None:
            self.ar_publishers.name = publisher
            publisher_id = self.ar_publishers.insert_if_not_found()
            self.publisher_id = publisher_id
            self.save()
            return True
        return False

    def total(self):
        sql = "select count(*) as Count from Games"
        result = self.connection.query(sql, False)
        for row in result:
            return row

    def find_by_title(self, title):
        sql = "select * from Games where title = '{}'".format(title)
        result = self.connection.query(sql, False)
        for row in result:
            return row
