#!/usr/local/bin/python3
import unittest
import day03


class TestDay03(unittest.TestCase):

    def test_part1(self):
        pass

    def test_part2(self):
        test_input = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
        return self.assertEqual(day03.part2(test_input), '3')


if __name__ == "__main__":
    unittest.main()
