import unittest
from day02 import Solution


s = Solution()


class TestSolution201502(unittest.TestCase):

    def test_part_01(self):
        s.data = "2x3x4"
        s.solve(1)
        self.assertEqual(s.p1, 58)

        s.data = "1x1x10"
        s.solve(1)
        self.assertEqual(s.p1, 43)

    def test_part_02(self):
        s.data = "2x3x4"
        s.solve(2)
        self.assertEqual(s.p2, 34)

        s.data = "1x1x10"
        s.solve(2)
        self.assertEqual(s.p2, 14)


if __name__ == '__main__':
    unittest.main()
