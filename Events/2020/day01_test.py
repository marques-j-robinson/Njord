import unittest
from day01 import Solution


s = Solution()


class TestSolution202001(unittest.TestCase):

    def test_part_01(self):
        s.data = "1721\n979\n366\n299\n675\n1456"
        s.solve(1)
        self.assertEqual(s.p1, 514579)

    def test_part_02(self):
        s.data = "1721\n979\n366\n299\n675\n1456"
        s.solve(2)
        self.assertEqual(s.p2, 241861950)


if __name__ == '__main__':
    unittest.main()
