import unittest
from day02 import Solution


class TestSolution201502(unittest.TestCase):

    def test_part_01(self):
        data = "2x3x4"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 58)

        data = "1x1x10"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 43)

    def test_part_02(self):
        data = "2x3x4"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 34)

        data = "1x1x10"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 14)


if __name__ == '__main__':
    unittest.main()
