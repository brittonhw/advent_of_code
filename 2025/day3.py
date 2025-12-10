'''
Solution file for Advent of Code Day 3
https://adventofcode.com/2025/day/3

Puzzle summary:


'''
from ingest import read_file

# naive way for pt1
def bank_max_joltage(bank_i):
    biggest_digit = max(bank_i)
    index_max = bank_i.index(biggest_digit)
    if index_max == len(bank_i) - 1:
        second_digit = biggest_digit
        first_digit = max(bank_i[:-1])
    else:
        first_digit = biggest_digit
        rest_of_list = bank_i[index_max + 1:]
        second_digit = max(rest_of_list)

    return (10 * first_digit) + second_digit


# greedy baby: 12 biggest joltage: biggest number 12 or more end, then biggest number 11 or more before rest, etc.
def n_total_joltage(bank, n):
    if n == 0:
        return max(bank)
    eligible_range = bank[:-n]
    max_digit = max(eligible_range)
    digit_index = bank.index(max_digit)
    return (max_digit * (10**n)) + n_total_joltage(bank[digit_index+1:], n - 1 )




def total_joltage(bank_list):
    total = 0
    total_12bats = 0
    for bank in bank_list:
        bank_i = [int(bank[i]) for i in range(len(bank))]
        total += bank_max_joltage(bank_i)
        total_12bats += n_total_joltage(bank_i, 11)
    
    return total, total_12bats

def main():
    input = read_file('day3/input.txt')
    print(input[0])
    
    pt1_answer, pt2_answer = total_joltage(input)

    print('Pt1 Answer:', pt1_answer)
    print('Pt2 Answer:', pt2_answer)







if __name__ == '__main__':
    main()
