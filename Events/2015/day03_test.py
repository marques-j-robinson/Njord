import unittest
from day03 import Solution


s = Solution()


class TestSolution201503(unittest.TestCase):

    def test_part_01(self):
        s.data = ">"
        s.solve(1)
        self.assertEqual(s.p1, 2)

        s.data = "^>v<"
        s.solve(1)
        self.assertEqual(s.p1, 4)

        s.data = "^v^v^v^v^v"
        s.solve(1)
        self.assertEqual(s.p1, 2)

    def test_part_02(self):
        s.data = "^v"
        s.solve(2)
        self.assertEqual(s.p2, 3)

        s.data = "^>v<"
        s.solve(2)
        self.assertEqual(s.p2, 3)

        s.data = "^v^v^v^v^v"
        s.solve(2)
        self.assertEqual(s.p2, 11)


if __name__ == '__main__':
    unittest.main()
