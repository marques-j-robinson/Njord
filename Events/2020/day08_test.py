import unittest
from day08 import Solution


data = "nop +0\nacc +1\njmp +4\nacc +3\njmp -3\nacc -99\nacc +1\njmp -4\nacc +6"


class TestSolution202008(unittest.TestCase):

    def test_part_01(self):
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 5)

    def test_part_02(self):
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 8)


if __name__ == '__main__':
    unittest.main()