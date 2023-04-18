from models.database_connector import DatabaseConnectionSingleton as Connection


class ActiveRecordRatings:

    def __init__(self):
        self.connection = Connection.get_instance()
        self._users_id = None
        self._game_id = None
        self._rating = None
        self._review = None

    @property
    def users_id(self):
        return self._users_id

    @users_id.setter
    def users_id(self, value):
        if not isinstance(value, int):
            raise TypeError('User ID must be an integer')
        if value < 1:
            raise ValueError('User ID must be greater than 0')
        self._users_id = value

    @property
    def game_id(self):
        return self._game_id

    @game_id.setter
    def game_id(self, value):
        if not isinstance(value, int):
            raise TypeError('Game ID must be an integer')
        if value < 1:
            raise ValueError('Game ID must be greater than 0')
        self._game_id = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError('Rating must be a float or an integer')
        if value < 1 or value > 10:
            raise ValueError('Rating must be between 1 and 10')
        self._rating = value

    @property
    def review(self):
        return self._review

    @review.setter
    def review(self, value):
        if not isinstance(value, str):
            raise TypeError('Review must be a string')
        if len(value) > 500:
            raise ValueError('Review must be no longer than 500 characters')
        self._review = value

    def save(self):
        sql = "insert into Ratings (users_id, game_id, rating, review) values ({},{},{},'{}')" \
            .format(self.users_id, self.game_id, self.rating, self.review)
        self.connection.query(sql)

    def update(self, users_id, game_id, rating, review):
        sql = "update Ratings set users_id={}, game_id={}, rating={}, review='{}' where" \
              "users_id={} and game_id={} and rating={} and review='{}'" \
            .format(users_id, game_id, rating, review, self.users_id, self.game_id,
                    self.rating, self.review)
        self.users_id = users_id
        self.game_id = game_id
        self.rating = rating
        self.review = review
        self.connection.query(sql)

    def delete(self):
        sql = "delete from Ratings where users_id={}, game_id={}, rating={}, review='{}'" \
            .format(self.users_id, self.game_id, self.rating, self.review)
        self.connection.query(sql)

    def find_by_game_title(self, game_title):
        sql = "select Users.username, Ratings.rating, Ratings.review  from ratings inner join Users on Users.id = ratings.users_id inner join Games on Games.id = ratings.game_id where Games.title = '{}'" \
            .format(game_title)
        result = self.connection.query(sql)
        return result

    def find_by_user_id(self, user_id):
        sql = "select Ratings.rating, Ratings.review from Ratings where Ratings.users_id = {}".format(user_id)
        result = self.connection.query(sql)
        return result

    def find_by_user_username(self, username):
        sql = "select count(users_id) as Count from Ratings inner join Users on Users.id = Ratings.users_id " \
              "where Users.username = '{}'".format(username)
        result = self.connection.query(sql)
        for row in result:
            return row

    def get_mean_score(self, username):
        sql = "select AVG(Ratings.rating) as Count from Ratings inner join " \
              "Users on Users.id = Ratings.users_id where Users.username = '{}'".format(username)
        result = self.connection.query(sql)
        for row in result:
            return row

    def total(self):
        sql = "select count(*) as Count from Ratings"
        result = self.connection.query(sql)
        for row in result:
            return row

    def get_game_ratings_for_user(self, username):
        sql = "select Games.title, Ratings.rating, Ratings.review from Ratings " \
              "inner join Games on Games.id = Ratings.game_id " \
              "inner join Users on Users.id = Ratings.users_id " \
              "where Users.username = '{}'".format(username)
        result = self.connection.query(sql)
        return result
