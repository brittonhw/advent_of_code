from ingest import read_file

def is_roll(input, row, col):
    row_dim = len(input)
    col_dim = len(input[0])
    if row not in range(row_dim) or col not in range(col_dim):
        return False
    else:
        return input[row][col] == '@'

def tally_neighbors(input):

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





def main():
    input = read_file('day4/input.txt')
    
    print(tally_neighbors(input))
    
    





if __name__ == '__main__':
    main()