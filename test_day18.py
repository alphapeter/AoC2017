import day18
import unittest


class TestDay18a(unittest.TestCase):

    def test_test_input(self):
        self.assertEqual(4, day18.calc_a(test_input_a))

    def test_input(self):
        self.assertEqual(3188, day18.calc_a(input))


class TestDay18b(unittest.TestCase):

    def test_test_case_a(self):
       self.assertEqual(1, day18.calc_b(test_input_a))

    def test_test_case_b(self):
       self.assertEqual(3, day18.calc_b(test_input_b))

    def test_case(self):
       self.assertEqual(7112, day18.calc_b(input))


test_input_a = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""

test_input_b = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""

input = """set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 680
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19"""