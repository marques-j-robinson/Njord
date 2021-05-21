import unittest
from day06 import Solution


s = Solution()


class TestSolution201506(unittest.TestCase):

    def test_part_01(self):
        s.data = "turn on 0,0 through 999,999"
        s.solve(1)
        self.assertEqual(s.p1, 1000000)

        s.data = "toggle 0,0 through 999,0"
        s.solve(1)
        self.assertEqual(s.p1, 1000)

        s.data = "turn off 499,499 through 500,500"
        s.solve(1)
        self.assertEqual(s.p1, 0)

    def test_part_02(self):
        s.data = "turn on 0,0 through 0,0"
        s.solve(2)
        self.assertEqual(s.p2, 1)

        s.data = "toggle 0,0 through 999,999"
        s.solve(2)
        self.assertEqual(s.p2, 2000000)


if __name__ == '__main__':
    unittest.main()
