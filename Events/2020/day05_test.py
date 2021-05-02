import unittest
from day05 import Solution


class TestSolution202005(unittest.TestCase):

    def test_part_01(self):
        data = "FBFBBFFRLR"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 357)

        data = "BFFFBBFRRR"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 567)

        data = "FFFBBBFRRR"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 119)

        data = "BBFFBBFRLL"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 820)

    # NOTE: This puzzle has no test data for part 2
    # def test_part_02(self):
        # data = ""
        # s = Solution(data)
        # s.part_02()
        # self.assertEqual(s.p2, 0)


if __name__ == '__main__':
    unittest.main()
