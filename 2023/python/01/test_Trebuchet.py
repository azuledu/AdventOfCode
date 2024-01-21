import unittest
import Trebuchet as Tr


class TestTrebuchet(unittest.TestCase):

    # Part one
    def test_01(self):
        self.assertEqual(12, Tr.calibrate('1abc2'))

    def test_02(self):
        self.assertEqual(38, Tr.calibrate('pqr3stu8vwx'))

    def test_03(self):
        self.assertEqual(15, Tr.calibrate('a1b2c3d4e5f'))

    def test_04(self):
        self.assertEqual(77, Tr.calibrate('treb7uchet'))

    # Part two
    def test_05(self):
        self.assertEqual(29, Tr.calibrate('two1nine'))

    def test_06(self):
        self.assertEqual(83, Tr.calibrate('eightwothree'))

    def test_07(self):
        self.assertEqual(13, Tr.calibrate('abcone2threexyz'))

    def test_08(self):
        self.assertEqual(24, Tr.calibrate('xtwone3four'))

    def test_09(self):
        self.assertEqual(42, Tr.calibrate('4nineeightseven2'))

    def test_10(self):
        self.assertEqual(14, Tr.calibrate('zoneight234'))

    def test_11(self):
        self.assertEqual(76, Tr.calibrate('7pqrstsixteen'))

    # Additional tests
    def test_12(self):
        self.assertEqual(51, Tr.calibrate('jjhxddmg5mqxqbgfivextlcpnvtwothreetwonerzk'))
