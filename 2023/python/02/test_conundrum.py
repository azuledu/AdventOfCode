import unittest
import conundrum as cn


class NumbersTest(unittest.TestCase):

    # def test_even(self):
    #     games = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    #              'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    #              'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    #              'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    #              'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']
    #     for game in games:
    #         with self.subTest(game = game):
    #             self.assertEqual(valid, )

    def test_rgb(self):
        game = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
        cubesets = game.split(':')[1].replace(';', ',').split(',')  # [' 3 blue', ' 4 red', ' 1 red', ' 2 green', ' 6 blue', ' 2 green']
        self.assertEqual([4, 2, 6], cn.get_rgb(cubesets))

    def test_is_valid_game(self):
        game = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
        self.assertTrue(cn.is_valid_game(game, [12, 13, 14]))
        self.assertTrue(cn.is_valid_game(game, [4, 2, 6]))
        self.assertFalse(cn.is_valid_game(game, [4, 2, 5]))
        self.assertTrue(cn.is_valid_game('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', [12, 13, 14]))
        self.assertFalse(cn.is_valid_game('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', [12, 13, 14]))
        self.assertFalse(cn.is_valid_game('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', [12, 13, 14]))
        self.assertTrue(cn.is_valid_game('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green', [12, 13, 14]))
