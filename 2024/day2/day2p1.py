
def safely_asc(a, b):
    return (b - a) in [1, 2, 3]

def safely_desc(a, b):
    return (a - b) in [1, 2, 3]

def check_level_asc(level):
    for i in range(len(level) - 1):
        if not (safely_asc(level[i], level[i+1])):
            return False
    return True

def check_level_desc(level):
    for i in range(len(level) - 1):
        if not (safely_desc(level[i], level[i+1])):
            return False
    return True

def main():
    levels = []

    with open('/Users/HenryBritton/advent_of_code/2024/day2/input.txt', 'r') as file:
        for row in file:
            items = [int(x) for x in row.strip().split(' ')]

            levels.append(items)

    total = 0
    print(len(levels))
    for level in levels:
        if check_level_asc(level) or check_level_desc(level):
            total += 1
            print(level)

    print(f"Total safe levels: {total}")

if __name__ == '__main__':
    main()