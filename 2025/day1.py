'''
Solution file for Advent of Code Day 1
https://adventofcode.com/2025/day/1

Puzzle summary:
Use sequence of rotations to tally number of times it points to 0

'''

from ingest import read_file

# rotating right is adding, left is subtraction
def parse_rotation(rotation):
     return int(rotation[1:]) if rotation[0] == 'R' else  0 - int(rotation[1:])

def tally_lefts(rotation_list):
    position = 50
    left_count = 0
    for rotation in rotation_list:
        position += parse_rotation(rotation)
        position = position%100
        if position == 0:
            left_count += 1

    return left_count

def main():
    input = read_file('day1/input.txt')
    password = tally_lefts(input)
    print ('Password is:', password)



if __name__ == '__main__':
    main()


