import itertools
import math

def main():
    day_01()


def day_01():
    with open('2020/input/2020-01.txt', 'r') as infile:
        report = [int(line.strip()) for line in infile]
    entries = find_comb(report, comb_size = 2)
    print('day 01 part 1:', math.prod(entries))

    print('day 01 part 2:', math.prod(find_comb(report, comb_size = 3)))


def find_comb(entry_list, comb_size = 2, number = 2020):
    for comb in itertools.combinations(entry_list, comb_size):
        if sum(comb) == number:
            return list(comb)


if __name__ == "__main__":
    main()