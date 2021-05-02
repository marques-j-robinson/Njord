import unittest
from day01 import Solution


class TestSolution201601(unittest.TestCase):

    def test_part_01(self):
        data = "R2, L3"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 5)

        data = "R2, R2, R2"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 2)

        data = "R5, L5, R5, R3"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 12)

    def test_part_02(self):
        data = "R8, R4, R4, R8"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 4)


if __name__ == '__main__':
    unittest.main()
