import unittest
from models.active_record_games import ActiveRecordGames


class TestActiveRecordGames(unittest.TestCase):

    def setUp(self):
        self.game = ActiveRecordGames()

    def tearDown(self):
        self.game.delete()

    def test_save(self):
        self.game.publisher_id = 1
        self.game.title = 'Test Game'
        self.game.release_date = '2022-01-01'
        self.game.global_rating = 8.5
        self.game.save()
        result = self.game.find()
        self.assertEqual(result[2], 'Test Game')

    def test_update(self):
        self.game.publisher_id = 1
        self.game.title = 'Test Game'
        self.game.release_date = '2022-01-01'
        self.game.global_rating = 8.5
        self.game.save()
        self.game.update(1, 'New Test Game', '2023-01-01', 9.0)
        result = self.game.find()
        print(result)
        self.assertEqual(result[2], 'New Test Game')

    def test_delete(self):
        self.game.publisher_id = 1
        self.game.title = 'Test Game'
        self.game.release_date = '2022-01-01'
        self.game.global_rating = 8.5
        self.game.save()
        self.game.delete()
        result = self.game.find()
        self.assertIsNone(result)

    def test_insert_if_not_found(self):
        self.game.title = 'Test Game'
        self.game.release_date = '2022-01-01'
        self.assertTrue(self.game.insert_if_not_found('Test Publisher'))


if __name__ == '__main__':
    unittest.main()
