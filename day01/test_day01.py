#!/usr/local/bin/python3.7
import unittest
import day01


class TestPart1(unittest.TestCase):

    def test_sum(self):
        tests = {0: [-1, 1], 3: [2, 1], 6: [1, 2, 3]}
        for answer, input_list in tests.items():
            self.assertEqual(answer, day01.part1(input_list))


class TestPart2(unittest.TestCase):

    def test(self):
        tests = {0: [1, -1], 5: [-6, +3, +8, +5, -6], 14: [+7, +7, -2, -7, -4], 10: [+3, +3, +4, -2, -4]}
        for answer, input_list in tests.items():
            self.assertEqual(answer, day01.part2(input_list))


if __name__ == "__main__":
    unittest.main()
