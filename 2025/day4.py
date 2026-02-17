from ingest import read_file
import copy

def is_roll(input, row, col):
    row_dim = len(input)
    col_dim = len(input[0])
    if row not in range(row_dim) or col not in range(col_dim):
        return False
    else:
        return input[row][col] == '@'

def find_accessible_rolls(input):

    grid = [list(line) for line in input]

    neighbors_map = [[0 for col in row] for row in input]

    accessible_rolls = 0
    for row in range(len(grid)):
        for col in range(len(input[0])):
            if is_roll(input, row, col):
                neighbors_map[row][col] += 1 if is_roll(input, row + 1, col) else 0
                neighbors_map[row][col] += 1 if is_roll(input, row + 1, col + 1) else 0
                neighbors_map[row][col] += 1 if is_roll(input, row + 1, col - 1) else 0
                neighbors_map[row][col] += 1 if is_roll(input, row, col + 1) else 0
                neighbors_map[row][col] += 1 if is_roll(input, row, col - 1) else 0
                neighbors_map[row][col] += 1 if is_roll(input, row - 1, col) else 0
                neighbors_map[row][col] += 1 if is_roll(input, row - 1, col + 1) else 0
                neighbors_map[row][col] += 1 if is_roll(input, row - 1, col - 1) else 0

                if neighbors_map[row][col] < 4:
                    accessible_rolls += 1

    return accessible_rolls

def check_removables(neighbor_map, input):
    print(neighbor_map)
    for row in range(len(neighbor_map)):
        for col in range(len(neighbor_map[0])):
            if neighbor_map[row][col] < 4 and is_roll(input, row, col):
                return True
    
    return False


def find_accessible_rolls_with_mutation(input):
    
    input_copy = []
    for line in input:
        added_line = []
        for item in list(line):
            added_line.append(0) if item == '.' else added_line.append(1)
        input_copy.append(added_line)


    neighbors_map = [[0 for col in row] for row in input]

    accessible_rolls = 0
    
    while check_removables(neighbors_map, input):

        for row in range(len(input_copy)):
            for col in range(len(input_copy[0])):
                if is_roll(input_copy, row, col):
                    neighbors_map[row][col] += 1 if is_roll(input_copy, row + 1, col) else 0
                    neighbors_map[row][col] += 1 if is_roll(input_copy, row + 1, col + 1) else 0
                    neighbors_map[row][col] += 1 if is_roll(input_copy, row + 1, col - 1) else 0
                    neighbors_map[row][col] += 1 if is_roll(input_copy, row, col + 1) else 0
                    neighbors_map[row][col] += 1 if is_roll(input_copy, row, col - 1) else 0
                    neighbors_map[row][col] += 1 if is_roll(input_copy, row - 1, col) else 0
                    neighbors_map[row][col] += 1 if is_roll(input_copy, row - 1, col + 1) else 0
                    neighbors_map[row][col] += 1 if is_roll(input_copy, row - 1, col - 1) else 0

                    if neighbors_map[row][col] < 4:
                        accessible_rolls += 1
                        input_copy[row][col] = '.'

    return accessible_rolls
    


def main():
    input = read_file('day4/input.txt')
    
    print(find_accessible_rolls(input))

    print(find_accessible_rolls_with_mutation(input.copy()))
    
    





if __name__ == '__main__':
    main()