import unittest

import gear_ratios as gr


class MyTestCase(unittest.TestCase):

    def test_get_line_numbers1(self):
        self.assertEqual(['123'], gr.get_line_numbers('..123..'))

    def test_get_line_numbers2(self):
        self.assertEqual(['123', '456'], gr.get_line_numbers('..123..456..'))

    def test_get_line_numbers3(self):
        self.assertEqual(['123', '456'], gr.get_line_numbers('..#123..456#..'))

    def test_get_part_numbers1(self):
        self.assertEqual([], gr.get_part_numbers('..123..'))

    def test_get_part_numbers2(self):
        self.assertEqual(['123'], gr.get_part_numbers('..#123..'))

    def test_get_part_numbers3(self):
        self.assertEqual(['456'], gr.get_part_numbers('..456#..'))

    def test_get_part_numbers4(self):
        self.assertEqual(['123', '456'], gr.get_part_numbers('..#123..456#..'))

    def test_get_part_numbers5(self):
        self.assertEqual(['123', '456'], gr.get_part_numbers('#123..456#'))

    def test_get_part_numbers6(self):
        self.assertEqual(['123', '456'], gr.get_part_numbers('#123#456#'))

    def test_is_adjacent_to_a_symbol_from_the_same_line1(self):
        self.assertFalse(gr.is_adjacent_to_a_symbol_from_the_same_line('..123..', '123'))

    def test_is_adjacent_to_a_symbol_from_the_same_line2(self):
        self.assertTrue(gr.is_adjacent_to_a_symbol_from_the_same_line('..#123..', '123'))

    def test_is_adjacent_to_a_symbol_from_the_same_line3(self):
        self.assertTrue(gr.is_adjacent_to_a_symbol_from_the_same_line('..123#..', '123'))

    def test_is_adjacent_to_a_symbol_from_other_line1(self):
        self.assertFalse(gr.is_adjacent_to_a_symbol_from_other_line('..123..', '.......', '123'))

    def test_is_adjacent_to_a_symbol_from_other_line2(self):
        self.assertTrue(gr.is_adjacent_to_a_symbol_from_other_line('.123', '#...', '123'))

    def test_is_adjacent_to_a_symbol_from_other_line3(self):
        self.assertTrue(gr.is_adjacent_to_a_symbol_from_other_line('123', '#..', '123'))

    def test_is_adjacent_to_a_symbol_from_other_line4(self):
        self.assertTrue(gr.is_adjacent_to_a_symbol_from_other_line('123.', '...#', '123'))

    # def test_line_adjacency1(self):
    #     self.assertFalse(Gr.line_adjacency('..123..'))
    #
    # def test_line_adjacency2(self):
    #     self.assertTrue(Gr.line_adjacency('..123#.'))


if __name__ == '__main__':
    unittest.main()
