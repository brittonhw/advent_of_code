'''
Solution file for Advent of Code Day 1
https://adventofcode.com/2025/day/1

Puzzle summary:
Use sequence of rotations to tally number of times it points to 0

'''

from ingest import read_file
import random

# rotating right is adding, left is subtraction
def parse_rotation(rotation):
    return int(rotation[1:]) if rotation[0] == 'R' else  0 - int(rotation[1:])

def tally_lefts(rotation_list):
    position = 50
    left_count = 0
    for rotation in rotation_list:
        position += parse_rotation(rotation)
        position = position % 100
        if position == 0:
            left_count += 1
    return left_count

# using the modulus to track position around circle
def tally_zero_pass_bys(rotation_list, verbose=False):
    position = 50
    zero_count = 0
    for rotation in rotation_list:
        rotation_result = position + parse_rotation(rotation)
        amount_added = 0
        amount_added += abs(rotation_result // 100)
        
        # edge case to not count moving off of 0 when going left, or double count when going right
        if (position == 0 and rotation_result < 0) or (rotation_result % 100 == 0 and rotation_result > 0):
            amount_added -= 1
        if rotation_result%100 == 0:
            amount_added += 1
        zero_count += amount_added
        
        # random sample for debugging output to avoid flooding
        if (random.random() < 0.01 or len(rotation_list) < 20) and verbose == True:
            print("inc 0 count by", amount_added, 'for rotation', rotation, 'from position', position, 'to', rotation_result)
        
        # set new position
        position = rotation_result % 100
    return zero_count

def main():
    
    input = read_file('day1/input.txt')
    password1 = tally_lefts(input)
    password2 = tally_zero_pass_bys(input, verbose=False)
    print ('Part 1 password is:', password1)
    print ('Part 2 Password is:', password2)



if __name__ == '__main__':
    main()


