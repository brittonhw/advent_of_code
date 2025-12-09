'''
Solution file for Advent of Code Day 2
https://adventofcode.com/2025/day/2

Puzzle summary:
you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice.
So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

Find, then add up together all of the invalid ids.

'''
from ingest import read_file


def parse_as_range(input_item):
    item_range = input_item.split('-')
    print( 'Length of range:', int(item_range[1]) - int(item_range[0]) + 1)
    return range(int(item_range[0]), int(item_range[1]) + 1)

def find_single_repeating_ids(input_list):
    total = 0
    for item in input_list:
        for id in parse_as_range(item):
            stringified_id = str(id)
            length = len(stringified_id)
            half_length = length // 2
            if stringified_id[:half_length] == stringified_id[half_length:]:
                #print(stringified_id)
                total += id
    return total


def main():
    input = read_file('day2/input.txt')
    input = input[0].split(',')

    answer = find_single_repeating_ids(input)
    
    print("Final Total:", answer)



if __name__ == '__main__':
    main()
