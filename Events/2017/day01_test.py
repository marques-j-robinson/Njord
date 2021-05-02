import unittest
from day01 import Solution


class TestSolution201701(unittest.TestCase):

    def test_part_01(self):
        data = "1122"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 3)

        data = "1111"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 4)

        data = "1234"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 0)

        data = "91212129"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 9)

    def test_part_02(self):
        data = "1212"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 6)

        data = "1221"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 0)

        data = "123425"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 4)

        data = "123123"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 12)

        data = "12131415"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 4)


if __name__ == '__main__':
    unittest.main()
