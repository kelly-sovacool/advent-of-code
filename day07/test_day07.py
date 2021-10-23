#!/usr/local/bin/python3
import unittest
from day07 import *


class TestDay07(unittest.TestCase):

    def test_part1(self):
        steps = parse_file('test_input.txt')
        nodes = get_nodes(steps)
        head_node = nodes[steps[0][0]]
        print(get_node_order(nodes))

    def test_part2(self):
        pass


if __name__ == "__main__":
    unittest.main()
