import unittest
from day06 import Solution


s = Solution()


class TestSolution202006(unittest.TestCase):

    def test_part_01(self):
        s.data = "abcx\nabcy\nabcz"
        s.solve(1)
        self.assertEqual(s.p1, 6)

        s.data = "abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb"
        s.solve(1)
        self.assertEqual(s.p1, 11)

    def test_part_02(self):
        s.data = "abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb"
        s.solve(2)
        self.assertEqual(s.p2, 6)


if __name__ == '__main__':
    unittest.main()
