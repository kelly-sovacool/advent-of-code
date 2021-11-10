import itertools
import math
import pprint


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


def day_03(infilename = '2020/input/2020-03.txt'):
    grid = Grid.from_file(infilename)
    print(f'grid dimensions: x={grid.xlen} y={grid.ylen}')
    
    right = 3
    down = 1
    tob = Toboggan(right, down)
    print('part 1 trees: ', tob.count_trees(grid))

    toboggans = [Toboggan(x,y) for x,y in [(1,1), (3,1), (5,1), (7,1), (1,2)]]
    n_trees = [tob.count_trees(grid) for tob in toboggans]
    print('part 2 trees multiplied: ', math.prod(n_trees))


class Grid(list):

    def __init__(self, things):
        super().__init__(things)

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as infile:
            grid = cls([line.strip() for line in infile])
        return grid

    @property
    def ylen(self):
        return len(self)
    
    @property
    def xlen(self):
        return len(self[0])

    def xpos(self, x):
        return x % self.xlen

    def get_loc(self, x, y):
        return self[y][self.xpos(x)]


class Toboggan:
    
    def __init__(self, right, down):
        self.xpos = 0
        self.ypos = 0
        self.right = right
        self.down = down

    def __repr__(self):
        return f"Tob(s({self.right},{self.down})@[{self.xpos},{self.ypos}])"

    def move(self):
        self.xpos += self.right
        self.ypos += self.down

    def get_loc(self, grid):
        if self.ypos >= grid.ylen:
            raise ValueError(f"The toboggan is at the bottom of the hill ({self.xpos}, {self.ypos})")
        return grid.get_loc(self.xpos, self.ypos)

    def count_trees(self, grid, tree = '#'):
        n_trees = 0
        self.move()
        while self.ypos < grid.ylen:
            n_trees += self.get_loc(grid) == tree
            self.move()
        return n_trees


def main():
    day_03('input/2020-03.txt')


if __name__ == "__main__":
    main()