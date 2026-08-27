from ingest import read_file
import copy

def is_roll(input, row, col):
    row_dim = len(input)
    col_dim = len(input[0])
    if row not in range(row_dim) or col not in range(col_dim):
        return False
    else:
        return input[row][col] == '@'


def get_neighbor_map(roll_map):
    neighbors_map = [[0 for col in row] for row in roll_map]
    for row in range(len(roll_map)):
        for col in range(len(roll_map[0])):
            if is_roll(roll_map, row, col):
                neighbors_map[row][col] += 1 if is_roll(roll_map, row + 1, col) else 0
                neighbors_map[row][col] += 1 if is_roll(roll_map, row + 1, col + 1) else 0
                neighbors_map[row][col] += 1 if is_roll(roll_map, row + 1, col - 1) else 0
                neighbors_map[row][col] += 1 if is_roll(roll_map, row, col + 1) else 0
                neighbors_map[row][col] += 1 if is_roll(roll_map, row, col - 1) else 0
                neighbors_map[row][col] += 1 if is_roll(roll_map, row - 1, col) else 0
                neighbors_map[row][col] += 1 if is_roll(roll_map, row - 1, col + 1) else 0
                neighbors_map[row][col] += 1 if is_roll(roll_map, row - 1, col - 1) else 0

    return neighbors_map

def find_accessible_rolls(input):

    grid = [list(line) for line in input]

    neighbors_map = get_neighbor_map(grid)
    accessible_rolls = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if is_roll(grid, row, col) and neighbors_map[row][col] < 4:    # Note: this is checking if its a ROLL and has <4 neighbors, not if its a ROLL and has <4 neighbors
                accessible_rolls += 1

    return accessible_rolls



def check_removables(neighbor_map, input):
    for row in range(len(neighbor_map)):
        for col in range(len(neighbor_map[0])):
            if neighbor_map[row][col] < 4 and is_roll(input, row, col):
                return True
    
    return False

def kill_removables(neighbor_map, input):
    rolls_removed = 0
    output = copy.deepcopy(input)
    for row in range(len(neighbor_map)):
        for col in range(len(neighbor_map[0])):
            if neighbor_map[row][col] < 4 and is_roll(input, row, col):
                output[row][col] = '.'
                rolls_removed += 1
    return output, rolls_removed

def find_accessible_rolls_with_mutation(input):
    
    input_copy = [list(line) for line in input]

    neighbors_map = get_neighbor_map(input_copy)
    accessible_rolls = 0
    
    while check_removables(neighbors_map, input_copy):
        input_copy, rolls_removed = kill_removables(neighbors_map, input_copy)
        accessible_rolls += rolls_removed
        neighbors_map = get_neighbor_map(input_copy)

    return accessible_rolls
    


def main():
    input = read_file('day4/input.txt')
    
    print(find_accessible_rolls(input))

    print(find_accessible_rolls_with_mutation(input.copy()))
    
    





if __name__ == '__main__':
    main()