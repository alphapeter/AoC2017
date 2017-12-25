import day10
import unittest


input_a = 83, 0, 193, 1, 254, 237, 187, 40, 88, 27, 2, 255, 149, 29, 42, 100
input_b = "83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100"


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
        self.assertEqual(20056, day10.calc_a(input_a, 256))


class TestDay10b(unittest.TestCase):

    def test_case_1(self):
       self.assertEqual('a2582a3a0e66e6e86e3812dcb672a272', day10.calc_b('', 256))
    def test_case_2(self):
       self.assertEqual('33efeb34ea91902bb2f59c9920caa6cd', day10.calc_b('AoC 2017', 256))
    def test_case_3(self):
       self.assertEqual('3efbe78a8d82f29979031a4aa0b16a9d', day10.calc_b('1,2,3', 256))
    def test_case_4(self):
       self.assertEqual('63960835bcdc130f0b66d7ff4f6a5a8e', day10.calc_b('1,2,4', 256))

    def test_case_4(self):
       self.assertEqual('d9a7de4a809c56bf3a9465cb84392c8e', day10.calc_b(input_b, 256))
