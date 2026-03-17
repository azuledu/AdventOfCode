import unittest

from dial import Dial


class TestSecretEntrance(unittest.TestCase):
    def test_initial_dial_position(self):
        self.assertEqual(Dial().position(), 50)
