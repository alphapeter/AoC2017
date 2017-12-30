import day24
import unittest


class TestDay24a(unittest.TestCase):

    def test_test_input(self):
        self.assertEqual(31, day24.calc_a(test_input))

    def test_input(self):
        self.assertEqual(1868, day24.calc_a(input))


class TestDay24b(unittest.TestCase):

    def test_test_input(self):
        self.assertEqual(19, day24.calc_b(test_input))

    def test_case(self):
       self.assertEqual(1841, day24.calc_b(input))

test_input = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""

input = """25/13
4/43
42/42
39/40
17/18
30/7
12/12
32/28
9/28
1/1
16/7
47/43
34/16
39/36
6/4
3/2
10/49
46/50
18/25
2/23
3/21
5/24
46/26
50/19
26/41
1/50
47/41
39/50
12/14
11/19
28/2
38/47
5/5
38/34
39/39
17/34
42/16
32/23
13/21
28/6
6/20
1/30
44/21
11/28
14/17
33/33
17/43
31/13
11/21
31/39
0/9
13/50
10/14
16/10
3/24
7/0
50/50"""