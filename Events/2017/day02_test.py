import unittest
from day02 import Solution


s = Solution()


class TestSolution201702(unittest.TestCase):

    def test_part_01(self):
        s.data = "5 1 9 5"
        s.solve(1)
        self.assertEqual(s.p1, 8)

        s.data = "7 5 3"
        s.solve(1)
        self.assertEqual(s.p1, 4)

        s.data = "2 4 6 8"
        s.solve(1)
        self.assertEqual(s.p1, 6)

    def test_part_02(self):
        s.data = "5 9 2 8"
        s.solve(2)
        self.assertEqual(s.p2, 4)

        s.data = "9 4 7 3"
        s.solve(2)
        self.assertEqual(s.p2, 3)

        s.data = "3 8 6 5"
        s.solve(2)
        slf.assertEqual(s.p2, 2)


if __name__ == '__main__':
    unittest.main()
