#!/usr/local/bin/python3
import itertools


def main():
    with open('input.txt', 'r') as file:
        input_list = [int(line) for line in file]
    print('part 1:', part1(input_list))
    print('part 2:', part2(input_list))


def part1(input_list):
    return sum(input_list)


def part2(input_list):
    current_freq = 0
    cycle = itertools.cycle(input_list)
    prev_freqs = set()
    duplicate_found = False
    while not duplicate_found:
        prev_freqs.add(current_freq)
        current_freq += next(cycle)
        if current_freq in prev_freqs:
            duplicate_found = True
    return current_freq


if __name__ == "__main__":
    main()
