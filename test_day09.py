import day09
import unittest


def getInput():
    file = open('day09.input.txt', 'r')
    content = file.read()
    file.close()
    return content


class TestDay09a(unittest.TestCase):

    def test_case_garbage_1(self):
            self.assertEqual(0, day09.calc_a("<>"))

    def test_case_garbage_2(self):
            self.assertEqual(0, day09.calc_a("<random characters>"))

    def test_case_garbage_3(self):
            self.assertEqual(0, day09.calc_a("<<<<>"))

    def test_case_garbage_4(self):
            self.assertEqual(0, day09.calc_a("<{!>}>"))

    def test_case_garbage_5(self):
            self.assertEqual(0, day09.calc_a("<!!>"))

    def test_case_garbage_6(self):
            self.assertEqual(0, day09.calc_a("<!!!>>"))

    def test_case_garbage_7(self):
            self.assertEqual(0, day09.calc_a('<{o"i!a,<{i<a>'))

    def test_case_group_1(self):
            self.assertEqual(1, day09.calc_a('{}'))

    def test_case_group_2(self):
            self.assertEqual(6, day09.calc_a('{{{}}}'))

    def test_case_group_3(self):
            self.assertEqual(5, day09.calc_a('{{},{}}'))

    def test_case_group_4(self):
            self.assertEqual(16, day09.calc_a('{{{},{},{{}}}}'))

    def test_case_group_5(self):
            self.assertEqual(1, day09.calc_a('{<a>,<a>,<a>,<a>}'))

    def test_case_group_6(self):
            self.assertEqual(9, day09.calc_a('{{<ab>},{<ab>},{<ab>},{<ab>}}'))

    def test_case_group_7(self):
            self.assertEqual(9, day09.calc_a('{{<!!>},{<!!>},{<!!>},{<!!>}}'))

    def test_case_group_8(self):
            self.assertEqual(3, day09.calc_a('{{<a!>},{<a!>},{<a!>},{<ab>}}'))

    def test_input(self):
        self.assertEqual(14204, day09.calc_a(getInput()))


class TestDay09b(unittest.TestCase):

    def test_case_garbage_1(self):
            self.assertEqual(0, day09.calc_b("<>"))

    def test_case_garbage_2(self):
            self.assertEqual(17, day09.calc_b("<random characters>"))

    def test_case_garbage_3(self):
            self.assertEqual(3, day09.calc_b("<<<<>"))

    def test_case_garbage_4(self):
            self.assertEqual(2, day09.calc_b("<{!>}>"))

    def test_case_garbage_5(self):
            self.assertEqual(0, day09.calc_b("<!!>"))

    def test_case_garbage_6(self):
            self.assertEqual(0, day09.calc_b("<!!!>>"))

    def test_case_garbage_7(self):
            self.assertEqual(10, day09.calc_b('<{o"i!a,<{i<a>'))

    def test_case(self):
       self.assertEqual(6622, day09.calc_b(getInput()))


