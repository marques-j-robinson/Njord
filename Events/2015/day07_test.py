import unittest
from day07 import Solution


s = Solution()


class TestSolution201507(unittest.TestCase):

    def test_part_01(self):
        print(s.res)
        s.data = ""
        s.solve(1)
        self.assertEqual(s.p1, 0)

    # def test_part_02(self):
        # s.data = ""
        # s.solve(2)
        # self.assertEqual(s.p2, 0)


if __name__ == '__main__':
    unittest.main()
