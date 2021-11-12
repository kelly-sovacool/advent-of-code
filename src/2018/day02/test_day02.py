#!/usr/local/bin/python3
import unittest
import day02


class TestPart1(unittest.TestCase):

    def test_part1(self):
        test_input = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
        self.assertEqual(day02.checksum(test_input), 12)


class TestPart2(unittest.TestCase):
    test_input = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

    def test_common_letters(self):
        self.assertEqual(day02.find_common_letters(self.test_input), 'fgij')


if __name__ == "__main__":
    unittest.main()
