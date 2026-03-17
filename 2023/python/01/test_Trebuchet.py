import unittest

import trebuchet as tr


class TestTrebuchet(unittest.TestCase):

    # Part one
    def test_01(self):
        self.assertEqual(12, tr.calibrate('1abc2'))

    def test_02(self):
        self.assertEqual(38, tr.calibrate('pqr3stu8vwx'))

    def test_03(self):
        self.assertEqual(15, tr.calibrate('a1b2c3d4e5f'))

    def test_04(self):
        self.assertEqual(77, tr.calibrate('treb7uchet'))

    # Part two
    def test_05(self):
        self.assertEqual(29, tr.calibrate('two1nine'))

    def test_06(self):
        self.assertEqual(83, tr.calibrate('eightwothree'))

    def test_07(self):
        self.assertEqual(13, tr.calibrate('abcone2threexyz'))

    def test_08(self):
        self.assertEqual(24, tr.calibrate('xtwone3four'))

    def test_09(self):
        self.assertEqual(42, tr.calibrate('4nineeightseven2'))

    def test_10(self):
        self.assertEqual(14, tr.calibrate('zoneight234'))

    def test_11(self):
        self.assertEqual(76, tr.calibrate('7pqrstsixteen'))

    # Additional tests
    def test_12(self):
        self.assertEqual(51, tr.calibrate('jjhxddmg5mqxqbgfivextlcpnvtwothreetwonerzk'))
