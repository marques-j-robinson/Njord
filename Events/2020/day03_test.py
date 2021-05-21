import unittest
from day03 import Solution


s = Solution()


class TestSolution202003(unittest.TestCase):

    def test_part_01(self):
        s.data = "..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#"
        s.solve(1)
        self.assertEqual(s.p1, 7)

    def test_part_02(self):
        s.data = "..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#"
        s.solve(2)
        self.assertEqual(s.p2, 336)


if __name__ == '__main__':
    unittest.main()
