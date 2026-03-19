import unittest

from dial import Dial


class TestSecretEntrance(unittest.TestCase):
    def test_initial_dial_position(self):
        self.assertEqual(Dial().position(), 50)

    def test_move_dial_to_right(self):
        self.assertEqual(60, Dial().position_after('R10'))

    def test_move_dial_to_left(self):
        self.assertEqual(40, Dial().position_after('L10'))

    def test_move_dial_overflow_right(self):
        self.assertEqual(10, Dial().position_after('R60'))

    def test_move_dial_overflow_left(self):
        self.assertEqual(90, Dial().position_after('L60'))

    # def test_input(self):
    #     dial = Dial()
    #     print('')
    #     with open('2025/python/01/test_input.txt') as input_file:
    #         for move in input_file:
    #             dial.position_after(move)
    #             print(f'{move.rstrip("\n")} - {dial.position()}')
    #
    #     print(f'Final position: ', dial.position())
    #     self.assertEqual(32, dial.position())

    def test_input(self):
        positions: list = Dial().position_after_moves_in_file('2025/python/01/test_input.txt')

        self.assertEqual(32, positions[-1])

    def test_password(self):
        dial = Dial()
        positions: list = dial.position_after_moves_in_file('2025/python/01/test_input.txt')

        self.assertEqual(3, dial.get_password(positions))
