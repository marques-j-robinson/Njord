import unittest
from day03 import Solution


class TestSolution201503(unittest.TestCase):

    def test_part_01(self):
        data = ">"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 2)

        data = "^>v<"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 4)

        data = "^v^v^v^v^v"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 2)

    def test_part_02(self):
        data = "^v"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 3)

        data = "^>v<"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 3)

        data = "^v^v^v^v^v"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 11)


if __name__ == '__main__':
    unittest.main()
