import unittest
from day6 import Solution


class TestSolution201506(unittest.TestCase):

    def test_part_01(self):
        data = "turn on 0,0 through 999,999"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 1000000)

        data = "toggle 0,0 through 999,0"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 1000)

        data = "turn off 499,499 through 500,500"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 0)

    def test_part_02(self):
        data = "turn on 0,0 through 0,0"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 1)

        data = "toggle 0,0 through 999,999"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 2000000)


if __name__ == '__main__':
    unittest.main()
