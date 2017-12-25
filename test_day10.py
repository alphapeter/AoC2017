import day10
import unittest


input = 83, 0, 193, 1, 254, 237, 187, 40, 88, 27, 2, 255, 149, 29, 42, 100


class TestDay10a(unittest.TestCase):

    def test_input_1(self):
        self.assertEqual(2, day10.calc_a((3,), 5))

    def test_input_2(self):
        self.assertEqual(12, day10.calc_a((3, 4), 5))

    def test_input_3(self):
        self.assertEqual(12, day10.calc_a((3, 4, 1), 5))

    def test_input_4(self):
        self.assertEqual(12, day10.calc_a((3, 4, 1, 5), 5))

    def test_input(self):
        self.assertEqual(20056, day10.calc_a(input, 256))


class TestDay10b(unittest.TestCase):

    def test_case(self):
       self.assertEqual(6622, day10.calc_b(input))
