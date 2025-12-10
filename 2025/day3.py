'''
Solution file for Advent of Code Day 3
https://adventofcode.com/2025/day/3

Puzzle summary:


'''
from ingest import read_file

def bank_max_joltage(bank):
    bank_i = [int(bank[i]) for i in range(len(bank))]
    biggest_digit = max(bank_i)
    index_max = bank_i.index(biggest_digit)
    if index_max == len(bank) - 1:
        second_digit = biggest_digit
        first_digit = max(bank_i[:-1])
    else:
        first_digit = biggest_digit
        rest_of_list = bank_i[index_max + 1:]
        second_digit = max(rest_of_list)

    return (10 * first_digit) + second_digit




def total_joltage(bank_list):
    total = 0
    for bank in bank_list:
        total += bank_max_joltage(bank)
    
    return total

def main():
    input = read_file('day3/input.txt')
    
    pt1_answer = total_joltage(input)
    print('Pt1 Answer:', pt1_answer)



if __name__ == '__main__':
    main()
