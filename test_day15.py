import day15
import unittest

input = """Generator A starts with 591
Generator B starts with 393
"""

test_input = """Generator A starts with 65
Generator B starts with 8921
"""


class TestDay15a(unittest.TestCase):

    def test_input_a(self):
        self.assertEqual(588, day15.calc_a(test_input))

    def test_input(self):
        self.assertEqual(619, day15.calc_a(input))


class TestDay15b(unittest.TestCase):

    def test_input_a(self):
        self.assertEqual(309, day15.calc_b(test_input))

    def test_case(self):
        self.assertEqual(290, day15.calc_b(input))
