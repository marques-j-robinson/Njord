import unittest
from day04 import Solution


class TestSolution201504(unittest.TestCase):

    def test_part_01(self):
        data = "abcdef"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 609043)

        data = "pqrstuv"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 1048970)

    # NOTE: This puzzle has no test data for part 2
    # def test_part_02(self):
        # data = ""
        # s = Solution(data)
        # s.part_02()
        # self.assertEqual(s.p2, 0)


if __name__ == '__main__':
    unittest.main()
