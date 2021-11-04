import itertools
import math


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


def day_02():
    passwords = list()
    with open('2020/input/2020-02.txt', 'r') as infile:
        passwords = [Password.from_line(line) for line in infile]
    valid_passwords = sum(1 for pw in passwords if pw.is_valid_p1)
    print('day 02 part 1:', valid_passwords)
    print('day 02 part 2:', sum(1 for pw in passwords if pw.is_valid_p2))


class Password:
    def __init__(self, min_char, max_char, char, password):
        self.min_char = int(min_char)
        self.max_char = int(max_char)
        self.char = str(char)
        self.password = str(password)

    @classmethod
    def from_line(cls, line):
        line = line.strip().split(":")
        char = line[0].split()[1]
        min_char = line[0].split('-')[0]
        max_char = line[0].split()[0].split('-')[1]
        password = line[1].strip()
        return cls(min_char, max_char, char, password)

    @property
    def is_valid_p1(self):
        n_char = sum(1 for c in self.password if c == self.char)
        return n_char >= self.min_char and n_char <= self.max_char

    @property
    def is_valid_p2(self):
        pos1 = self.min_char - 1
        pos2 = self.max_char - 1
        n_chars = sum(self.password[pos] == self.char for pos in [pos1, pos2])
        return n_chars == 1


def main():
    day_02()


if __name__ == "__main__":
    main()