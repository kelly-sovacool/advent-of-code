#!/usr/local/bin/python3
import sys

def day01():
    elves = [0]
    curr_elf = 0
    with open('input/2022/01-part-1.txt', 'r') as infile:
        for line in infile:
            if line.isspace():
                curr_elf += 1
                elves.append(0)
            else:
                elves[curr_elf] += int(line.strip())
    print('part 1:', max(elves))
    print('part 2:', sum(sorted(elves, reverse=True)[:3]))



def main():
    day02()

if __name__ == "__main__":
    main()