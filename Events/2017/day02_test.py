import unittest
from day02 import Solution


class TestSolution201702(unittest.TestCase):

    def test_part_01(self):
        data = "5 1 9 5"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 8)

        data = "7 5 3"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 4)

        data = "2 4 6 8"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 6)

    def test_part_02(self):
        data = "5 9 2 8"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 4)

        data = "9 4 7 3"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 3)

        data = "3 8 6 5"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 2)


if __name__ == '__main__':
    unittest.main()
