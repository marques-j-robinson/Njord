import unittest
from day02 import Solution


class TestSolution202002(unittest.TestCase):

    def test_part_01(self):
        data = "1-3 a: abcde"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 1)

        data = "1-3 b: cdefg"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 0)

        data = "2-9 c: ccccccccc"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 1)

    def test_part_02(self):
        data = "1-3 a: abcde"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 1)

        data = "1-3 b: cdefg"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 0)

        data = "2-9 c: ccccccccc"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 0)


if __name__ == '__main__':
    unittest.main()
