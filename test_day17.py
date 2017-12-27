import day17
import unittest


input = 312

class TestDay17a(unittest.TestCase):

    def test_test_input(self):
        self.assertEqual(638, day17.calc_a(3))

    def test_input(self):
        self.assertEqual(772, day17.calc_a(input))


class TestDay17b(unittest.TestCase):

    def test_case(self):
       self.assertEqual(42729050, day17.calc_b(input))
