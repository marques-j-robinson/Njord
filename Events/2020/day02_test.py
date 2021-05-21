import unittest
from day02 import Solution


s = Solution()


class TestSolution202002(unittest.TestCase):

    def test_part_01(self):
        s.data = "1-3 a: abcde"
        s.solve(1)
        self.assertEqual(s.p1, 1)

        s.data = "1-3 b: cdefg"
        s.solve(1)
        self.assertEqual(s.p1, 0)

        s.data = "2-9 c: ccccccccc"
        s.solve(1)
        self.assertEqual(s.p1, 1)

    def test_part_02(self):
        s.data = "1-3 a: abcde"
        s.solve(2)
        self.assertEqual(s.p2, 1)

        s.data = "1-3 b: cdefg"
        s.solve(2)
        self.assertEqual(s.p2, 0)

        s.data = "2-9 c: ccccccccc"
        s.solve(2)
        self.assertEqual(s.p2, 0)


if __name__ == '__main__':
    unittest.main()
