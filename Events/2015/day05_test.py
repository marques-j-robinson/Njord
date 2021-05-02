import unittest
from day05 import Solution


class TestSolution201505(unittest.TestCase):

    def test_part_01(self):
        data = "ugknbfddgicrmopn"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 1)

        data = "aaa"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 1)

        data = "jchzalrnumimnmhp"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 0)

        data = "haegwjzuvuyypxyu"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 0)

        data = "dvszwmarrgswjxmb"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 0)

    def test_part_02(self):
        data = "qjhvhtzxzqqjkmpb"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 1)

        data = "xxyxx"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 1)

        data = "uurcxstgmygtbstg"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 0)

        data = "ieodomkazucvgmuy"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 0)


if __name__ == '__main__':
    unittest.main()
