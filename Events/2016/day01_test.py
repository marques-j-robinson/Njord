import unittest
from day01 import Solution


s = Solution()


class TestSolution201601(unittest.TestCase):

    def test_part_01(self):
        s.data = "R2, L3"
        s.solve(1)
        self.assertEqual(s.p1, 5)

        s.data = "R2, R2, R2"
        s.solve(1)
        self.assertEqual(s.p1, 2)

        s.data = "R5, L5, R5, R3"
        s.solve(1)
        self.assertEqual(s.p1, 12)

    def test_part_02(self):
        s.data = "R8, R4, R4, R8"
        s.solve(2)
        self.assertEqual(s.p2, 4)


if __name__ == '__main__':
    unittest.main()
