import unittest
from day03 import Solution


data = "..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#"


class TestSolution202003(unittest.TestCase):

    def test_part_01(self):
        s = Solution(data)
        s.part_01()
        self.assertEqual(s.p1, 7)

    def test_part_02(self):
        s = Solution(data)
        s.part_02()
        self.assertEqual(s.p2, 336)


if __name__ == '__main__':
    unittest.main()
