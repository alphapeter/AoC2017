import day03
import unittest

input = 312051

class TestDay03a(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(0, day03.calc_a(1))

    def test_case2(self):
        self.assertEqual(1, day03.calc_a(2))
    def test_case3(self):
        self.assertEqual(2, day03.calc_a(3))
    def test_case4(self):
        self.assertEqual(1, day03.calc_a(4))
    def test_case5(self):
        self.assertEqual(2, day03.calc_a(5))
    def test_case6(self):
        self.assertEqual(1, day03.calc_a(6))
    def test_case7(self):
        self.assertEqual(2, day03.calc_a(7))
    def test_case8(self):
        self.assertEqual(1, day03.calc_a(8))
    def test_case9(self):
        self.assertEqual(2, day03.calc_a(9))


    def test_case12(self):
        self.assertEqual(3, day03.calc_a(12))

    def test_case23(self):
        self.assertEqual(2, day03.calc_a(23))

    def test_case1024(self):
        self.assertEqual(31, day03.calc_a(1024))

    def test_input(self):
        self.assertEqual(430, day03.calc_a(input))


class TestDay03b(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(2, day03.calc_b(1))

    def test_case4(self):
        self.assertEqual(5, day03.calc_b(4))

    def test_case25(self):
        self.assertEqual(26, day03.calc_b(25))

    def test_case26(self):
        self.assertEqual(54, day03.calc_b(26))

    def test_input(self):
            self.assertEqual(312453, day03.calc_b(input))