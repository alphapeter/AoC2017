import day14
import unittest


class TestDay14a(unittest.TestCase):

    def test_input_1(self):
        self.assertEqual(8108, day14.calc_a("flqrgnkx"))

    def test_input(self):
        self.assertEqual(8222, day14.calc_a("amgozmfv"))


class TestDay14b(unittest.TestCase):


    def test_input_1(self):
        self.assertEqual(1242, day14.calc_b("flqrgnkx"))

    def test_case(self):
       self.assertEqual(1086, day14.calc_b("amgozmfv"))
