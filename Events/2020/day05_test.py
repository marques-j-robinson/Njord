import unittest
from day05 import Solution


s = Solution()


class TestSolution202005(unittest.TestCase):

    def test_part_01(self):
        s.data = "FBFBBFFRLR"
        s.solve(1)
        self.assertEqual(s.p1, 357)

        s.data = "BFFFBBFRRR"
        s.solve(1)
        self.assertEqual(s.p1, 567)

        s.data = "FFFBBBFRRR"
        s.solve(1)
        self.assertEqual(s.p1, 119)

        s.data = "BBFFBBFRLL"
        s.solve(1)
        self.assertEqual(s.p1, 820)

    # NOTE: This puzzle has no test data for part 2
    # def test_part_02(self):
        # s.data = ""
        # s.solve(2)
        # self.assertEqual(s.p2, 0)


if __name__ == '__main__':
    unittest.main()
