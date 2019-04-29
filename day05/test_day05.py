#!/usr/local/bin/python3
import unittest
import day05


class TestDay05(unittest.TestCase):
    test_input = 'dabAcCaCBAcCcaDA'

    def test_part1(self):
        result = 'dabCBAcaDA'
        return self.assertEqual(day05.part1(self.test_input), result)

    def test_part2(self):
        pass


if __name__ == "__main__":
    unittest.main()
