import unittest
from day01 import Solution


s = Solution()


class TestSolution201901(unittest.TestCase):

    def test_part_01(self):
        s.data = "12"
        s.solve(1)
        self.assertEqual(s.p1, 2)

        s.data = "14"
        s.solve(1)
        self.assertEqual(s.p1, 2)

        s.data = "1969"
        s.solve(1)
        self.assertEqual(s.p1, 654)

        s.data = "100756"
        s.solve(1)
        self.assertEqual(s.p1, 33583)

    def test_part_02(self):
        s.data = "14"
        s.solve(2)
        self.assertEqual(s.p2, 2)

        s.data = "1969"
        s.solve(2)
        self.assertEqual(s.p2, 966)

        s.data = "100756"
        s.solve(2)
        self.assertEqual(s.p2, 50346)


if __name__ == '__main__':
    unittest.main()
