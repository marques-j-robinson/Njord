import unittest
from day06 import Solution


class TestSolution202006(unittest.TestCase):

    def test_part_01(self):
        data = "abcx\nabcy\nabcz"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 6)

        data = "abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb"
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 11)

    def test_part_02(self):
        data = "abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb"
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 6)


if __name__ == '__main__':
    unittest.main()
