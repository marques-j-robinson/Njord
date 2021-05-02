import unittest
from day01 import Solution


s = Solution()


class TestSolution201501(unittest.TestCase):

    def test_part_01(self):
        s.data = "(())"
        s.solve(1)
        self.assertEqual(s.p1, 0)

        s.data = "()()"
        s.solve(1)
        self.assertEqual(s.p1, 0)

        s.data = "((("
        s.solve(1)
        self.assertEqual(s.p1, 3)

        s.data = "(()(()("
        s.solve(1)
        self.assertEqual(s.p1, 3)

        s.data = "))((((("
        s.solve(1)
        self.assertEqual(s.p1, 3)

        s.data = "())"
        s.solve(1)
        self.assertEqual(s.p1, -1)

        s.data = "))("
        s.solve(1)
        self.assertEqual(s.p1, -1)

        s.data = ")))"
        s.solve(1)
        self.assertEqual(s.p1, -3)

        s.data = ")())())"
        s.solve(1)
        self.assertEqual(s.p1, -3)

    def test_part_02(self):
        s.data = ")"
        s.solve(2)
        self.assertEqual(s.p2, 1)

        s.data = "()())"
        s.solve(2)
        self.assertEqual(s.p2, 5)


if __name__ == '__main__':
    unittest.main()
