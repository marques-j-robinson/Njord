import unittest
from day01 import Solution


s = Solution()


class TestSolution201701(unittest.TestCase):

    def test_part_01(self):
        s.data = "1122"
        s.solve(1)
        self.assertEqual(s.p1, 3)

        s.data = "1111"
        s.solve(1)
        self.assertEqual(s.p1, 4)

        s.data = "1234"
        s.solve(1)
        self.assertEqual(s.p1, 0)

        s.data = "91212129"
        s.solve(1)
        self.assertEqual(s.p1, 9)

    def test_part_02(self):
        s.data = "1212"
        s.solve(2)
        self.assertEqual(s.p2, 6)

        s.data = "1221"
        s.solve(2)
        self.assertEqual(s.p2, 0)

        s.data = "123425"
        s.solve(2)
        self.assertEqual(s.p2, 4)

        s.data = "123123"
        s.solve(2)
        self.assertEqual(s.p2, 12)

        s.data = "12131415"
        s.solve(2)
        self.assertEqual(s.p2, 4)


if __name__ == '__main__':
    unittest.main()
