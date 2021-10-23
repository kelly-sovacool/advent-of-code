#!/usr/local/bin/python3

def main():
    with open('input.txt', 'r') as infile:
        polymer_input = next(infile).strip()
    print('Part1', part1(polymer_input))
    print('Part2', part2(polymer_input))


def part1(polymer_input):  # this is inefficient
    polymer = [char for char in polymer_input]
    index = 1
    len_polymer = len(polymer)
    while index < len_polymer:
        if index > 0 and is_opposite(polymer[index], polymer[index-1]):
            polymer.pop(index)
            polymer.pop(index-1)
            index = index-2
            len_polymer = len(polymer)
        else:
            index += 1
    return len(polymer)


def part2(polymer_input):
    monomers = {char.lower() for char in polymer_input}
    polymers = {char: part1(strip_char(polymer_input, char)) for char in monomers}
    min_char = min(polymers, key = lambda x: polymers[x])
    return polymers[min_char]


def strip_char(polymer, badchar):
    return ''.join(char for char in polymer if not is_opposite(char, badchar) and char != badchar)


def is_opposite(char1, char2):
    return char1.lower() == char2.lower() and ((char1.islower() and char2.isupper()) or (char1.isupper() and char2.islower()))


if __name__ == "__main__":
    main()
