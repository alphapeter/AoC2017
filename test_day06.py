import day06
import unittest

input = "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6"

test_input = "0 2   7   0"


class TestDay06a(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(5, day06.calc_a(test_input))

    def test_input(self):
        self.assertEqual(14029, day06.calc_a(input))


class TestDay06b(unittest.TestCase):

    def test_case1(self):
       self.assertEqual(4, day06.calc_b(test_input))

    def test_case(self):
       self.assertEqual(2765, day06.calc_b(input))



