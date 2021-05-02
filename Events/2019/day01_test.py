import unittest
from day01 import Solution


class TestSolution201901(unittest.TestCase):

    def test_part_01(self):
        data = "12"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 2)

        data = "14"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 2)

        data = "1969"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 654)

        data = "100756"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 33583)

    def test_part_02(self):
        data = "14"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 2)

        data = "1969"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 966)

        data = "100756"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 50346)


if __name__ == '__main__':
    unittest.main()
