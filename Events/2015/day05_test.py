import unittest
from day05 import Solution


s = Solution()


class TestSolution201505(unittest.TestCase):

    def test_part_01(self):
        s.data = "ugknbfddgicrmopn"
        s.solve(1)
        self.assertEqual(s.p1, 1)

        s.data = "aaa"
        s.solve(1)
        self.assertEqual(s.p1, 1)

        s.data = "jchzalrnumimnmhp"
        s.solve(1)
        self.assertEqual(s.p1, 0)

        s.data = "haegwjzuvuyypxyu"
        s.solve(1)
        self.assertEqual(s.p1, 0)

        s.data = "dvszwmarrgswjxmb"
        s.solve(1)
        self.assertEqual(s.p1, 0)

    def test_part_02(self):
        s.data = "qjhvhtzxzqqjkmpb"
        s.solve(2)
        self.assertEqual(s.p2, 1)

        s.data = "xxyxx"
        s.solve(2)
        self.assertEqual(s.p2, 1)

        s.data = "uurcxstgmygtbstg"
        s.solve(2)
        self.assertEqual(s.p2, 0)

        s.data = "ieodomkazucvgmuy"
        s.solve(2)
        self.assertEqual(s.p2, 0)


if __name__ == '__main__':
    unittest.main()
