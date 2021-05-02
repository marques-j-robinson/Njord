import unittest
from day01 import Solution

data = "1721\n979\n366\n299\n675\n1456"


class TestSolution202001(unittest.TestCase):

    def test_part_01(self):
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 514579)

    def test_part_02(self):
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 241861950)


if __name__ == '__main__':
    unittest.main()
