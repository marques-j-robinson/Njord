import unittest
from day09 import Solution


data = "35\n20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576"


class TestSolution202009(unittest.TestCase):

    def test_part_01(self):
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 127)

    def test_part_02(self):
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 62)


if __name__ == '__main__':
    unittest.main()
