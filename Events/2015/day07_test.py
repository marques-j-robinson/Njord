import unittest
from day07 import Solution


s = Solution()


class TestSolution201507(unittest.TestCase):

    def test_part_01(self):
        s.data = "b AND c -> a\n123 -> b\n456 -> c"
        s.solve(1)
        self.assertEqual(s.p1, 72)

        s.data = "123 -> a"
        s.solve(1)
        self.assertEqual(s.p1, 123)

        s.data = "123 -> x\n456 -> y\nx AND y -> a"
        s.solve(1)
        self.assertEqual(s.p1, 72)

        s.data = "123 -> x\n456 -> y\nx OR y -> a"
        s.solve(1)
        self.assertEqual(s.p1, 507)

        s.data = "123 -> x\nx LSHIFT 2 -> a"
        s.solve(1)
        self.assertEqual(s.p1, 492)

        s.data = "456 -> y\ny RSHIFT 2 -> a"
        s.solve(1)
        self.assertEqual(s.p1, 114)

        s.data = "123 -> x\nNOT x -> a"
        s.solve(1)
        self.assertEqual(s.p1, 65412)

        s.data = "456 -> y\nNOT y -> a"
        s.solve(1)
        self.assertEqual(s.p1, 65079)

    # def test_part_02(self):
        # s.data = ""
        # s.solve(2)
        # self.assertEqual(s.p2, 0)


if __name__ == '__main__':
    unittest.main()
