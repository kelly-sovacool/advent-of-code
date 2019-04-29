#!/usr/local/bin/python3
from itertools import cycle


def main():
    with open('input.txt', 'r') as infile:
        polymer_input = next(infile).strip()
    print('Part1', part1(polymer_input))


# TO-DO: implement recursive solution
def part1_TODO(polymer_input):
    indices = list(list())
    for index, char in polymer_input[1:]:
        prev_index = index-1
        prev_char = polymer_input[prev_index]
        if is_opposite(char, prev_char) and prev_index not in indices[-1]:
            if indices[-1][-1] == prev_index-1:
                indices[-1].extend([index, prev_index])
            else:
                indices.append([index, prev_index])
    for stretch in indices:
        pass


def part1(polymer_input):  # this is inefficient
    polymer = [char for char in polymer_input]
    index = 1
    len_polymer = len(polymer)
    while index < len_polymer:
        print(index)
        if index > 0 and is_opposite(polymer[index], polymer[index-1]):
            polymer.pop(index)
            polymer.pop(index-1)
            index = index-2
            len_polymer = len(polymer)
        else:
            index += 1
    return ''.join(polymer)


def is_opposite(char1, char2):
    return char1.lower() == char2.lower() and ((char1.islower() and char2.isupper()) or (char1.isupper() and char2.islower()))


if __name__ == "__main__":
    main()
