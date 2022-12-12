#!/usr/local/bin/python3
import sys

def day01():
    elves = [0]
    curr_elf = 0
    with open('input/2022/01.txt', 'r') as file:
        for line in file:
            if line.isspace():
                curr_elf += 1
                elves.append(0)
            else:
                elves[curr_elf] += int(line.strip())
    print('part 1:', max(elves))
    print('part 2:', sum(sorted(elves, reverse=True)[:3]))

def day02_p1():
    shape_scores = {'rock': 1, 'paper': 2, 'scissors': 3}
    who_beats_what = {'rock': 'scissors',
                      'paper': 'rock',
                      'scissors': 'paper'}
    shape_names = {'A': 'rock', 'B': 'paper', 'C': 'scissors',
                   'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
    outcome_scores = {'win': 6, 'lose': 0, 'draw': 3}
    total_score = 0
    with open('input/2022/02.txt', 'r') as file:
        for line in file:
            opp, you = line.split()
            opp_shape = shape_names[opp]
            you_shape = shape_names[you]
            if opp_shape == you_shape:
                round_outcome = 'draw'
            elif who_beats_what[opp_shape] == you_shape:
                round_outcome = 'lose'
            else:
                round_outcome = 'win'
            total_score += outcome_scores[round_outcome] + shape_scores[you_shape]
    print('part 1:', total_score)

def day02_p2():
    shape_scores = {'rock': 1, 'paper': 2, 'scissors': 3}
    who_beats_what = {'rock': 'scissors',
                      'paper': 'rock',
                      'scissors': 'paper'}
    who_loses_to_what = {val: key for key, val in who_beats_what.items()}
    shape_names = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
    outcome_codes = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
    outcome_scores = {'win': 6, 'lose': 0, 'draw': 3}
    total_score = 0
    with open('input/2022/02.txt', 'r') as file:
        for line in file:
            opp, you = line.split()
            opp_shape = shape_names[opp]
            outcome = outcome_codes[you]
            # lose
            if outcome == 'lose':
                you_shape = who_beats_what[opp_shape]
            # draw
            elif outcome == 'draw':
                you_shape = opp_shape
            # win
            else:
                you_shape = who_loses_to_what[opp_shape]
            total_score += outcome_scores[outcome] + shape_scores[you_shape]
    print('part 2:', total_score)

def main():
    day02_p2()

if __name__ == "__main__":
    main()