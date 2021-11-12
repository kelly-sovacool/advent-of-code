#!/usr/local/bin/python3
import collections


def main():
    with open('input.txt', 'r') as file:
        input_list = [line for line in file]
    print('part 1:', part1(input_list))
    print('part 2:', part2(input_list))


class Claim:
    def __init__(self, string):
        str_split = string.split()
        self.id = str_split[0].strip('#')
        self.left = int(str_split[2].split(',')[0])
        self.top = int(str_split[2].split(',')[1].strip(':'))
        self.right = self.left + int(str_split[3].split('x')[0])
        self.bottom = self.top + int(str_split[3].split('x')[1])
        self.coords = set()
        for x in range(self.left, self.right):
            for y in range(self.top, self.bottom):
                self.coords.add(f'{x},{y}')


def get_claim_counts(claims):
    # TODO: instead of keeping set of all coords, only needs to include vertices of polygon
    fabric_claim_counts = collections.defaultdict(int)
    for claim in claims:
        for coord in claim.coords:
            fabric_claim_counts[coord] += 1
    return fabric_claim_counts


def part1(input_list):
    claims = [Claim(string) for string in input_list]
    fabric_claim_counts = get_claim_counts(claims)
    count = 0
    for coord in fabric_claim_counts:
        if fabric_claim_counts[coord] > 1:
            count += 1
    return count


def part2(input_list):
    claims = [Claim(string) for string in input_list]
    fabric = get_claim_counts(claims)
    unique_claim_found = False
    i = 0
    while not unique_claim_found and i < len(claims):
        claim = claims[i]
        is_unique = True
        coords = claim.coords
        while is_unique and coords:
            if fabric[coords.pop()] != 1:
                is_unique = False
        if not coords and is_unique:
            unique_claim_found = True
        i += 1
    return claim.id if unique_claim_found else None


if __name__ == "__main__":
    main()
