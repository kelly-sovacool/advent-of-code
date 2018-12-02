#!/usr/local/bin/python3
import collections


def main():
    with open('input.txt', 'r') as file:
        box_ids = [str(line) for line in file]
    print('part1:', checksum(box_ids))
    print('part2:', find_common_letters(box_ids))


    def checksum(box_ids):
        candidates = {2: 0, 3: 0}
        for box_id in box_ids:
            characters_to_counts = collections.defaultdict(int)
            for char in box_id:
                characters_to_counts[char] += 1
            counts = set(characters_to_counts.values())
            if 2 in counts:
                candidates[2] += 1
            if 3 in counts:
                candidates[3] += 1
        return candidates[2] * candidates[3]


    def find_common_letters(box_ids):
        common_letters = None
        pair_found = False
        list_pos_a = 0
        while not pair_found and list_pos_a < len(box_ids):
            list_pos_b = 0
            while not pair_found and list_pos_b < len(box_ids):
                if list_pos_a != list_pos_b:
                    id_a = box_ids[list_pos_a]
                    id_b = box_ids[list_pos_b]
                    length = len(min(id_a, id_b))
                    common_letters = list()
                    num_mismatches = 0
                    id_pos = 0
                    while num_mismatches <= 1 and id_pos < length:
                        if id_a[id_pos] == id_b[id_pos]:
                            common_letters.append(id_a[id_pos])
                        else:
                            num_mismatches += 1
                        id_pos += 1
                    if id_pos == length and num_mismatches == 1:
                        pair_found = True
                        common_letters = ''.join(common_letters)
                list_pos_b += 1
            list_pos_a += 1
        return common_letters


if __name__ == "__main__":
    main()
