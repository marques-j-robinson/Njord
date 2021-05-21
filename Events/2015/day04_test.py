import unittest
from day04 import Solution


s = Solution()


class TestSolution201504(unittest.TestCase):

    def test_part_01(self):
        s.data = "abcdef"
        s.solve(1)
        self.assertEqual(s.p1, 609043)

        s.data = "pqrstuv"
        s.solve(1)
        self.assertEqual(s.p1, 1048970)

    # NOTE: This puzzle has no test data for part 2
    # def test_part_02(self):
        # s.data = ""
        # s.solve(2)
        # self.assertEqual(s.p2, 0)


if __name__ == '__main__':
    unittest.main()
