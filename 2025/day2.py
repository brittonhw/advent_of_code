'''
Solution file for Advent of Code Day 2
https://adventofcode.com/2025/day/2

Puzzle summary:
you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice.
So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

Find, then add up together all of the invalid ids.

'''
from ingest import read_file
import textwrap

# break into ranges
def parse_as_range(input_item):
    item_range = input_item.split('-')
    print( 'Length of range:', int(item_range[1]) - int(item_range[0]) + 1)
    return range(int(item_range[0]), int(item_range[1]) + 1)

# break and half and check if both halves are the same
def find_single_repeating_ids(input_list):
    total = 0
    for item in input_list:
        for id in parse_as_range(item):
            stringified_id = str(id)
            length = len(stringified_id)
            half_length = length // 2
            if stringified_id[:half_length] == stringified_id[half_length:]:
                total += id
    return total

# break into chunks of n and check if all are the same
def find_n_repeating_ids(input_list):
    total = 0
    for item in input_list:
        for id in parse_as_range(item):
            stringified_id = str(id)
            length = len(stringified_id)
            # only need to check up to half the length
            for i in range(1, length//2 + 1):
                wrapped = textwrap.wrap(stringified_id, i)
                if wrapped and all(x == wrapped[0] for x in wrapped):
                    total += id
                    # once found, no need to check other lengths, and don't want to multi-count
                    break
    return total

def main():
    input = read_file('day2/input.txt')
    input = input[0].split(',')

    p1_answer = find_single_repeating_ids(input)
    p2_answer = find_n_repeating_ids(input)

    
    print("P1 Total:", p1_answer)
    print("P2 Total:", p2_answer)



if __name__ == '__main__':
    main()
