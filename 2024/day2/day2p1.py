
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


def check_asc_dampener_dynamic(level):
    skip_point = None
    for i in range(len(level) - 1):
        if i == skip_point:
            pass
        if not (safely_asc(level[i], level[i+1])):
            if (skip_point is None) and i < (len(level)-2): # if our skip is available and there's a place to skip to
                skip_point = i + 1 # no more skips now
                if (safely_asc(level[i], level[i+2])):
                    pass
                else:
                    return False
                
            else:
                return False # not safe, and no more skips
    return True

def check_desc_dampener_dynamic(level):
    skip_point = None
    for i in range(len(level) - 1):
        if i == skip_point:
            pass
        if not (safely_desc(level[i], level[i+1])):
            if (skip_point is None) and i < (len(level)-2): # if our skip is available and there's a place to skip to
                skip_point = i + 1 # no more skips now
                if (safely_desc(level[i], level[i+2])):
                    pass
                else:
                    return False
                
            else:
                return False # not safe, and no more skips
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
        if check_asc_dampener_dynamic(level) or check_desc_dampener_dynamic(level):
            total += 1
            
        else:
            print(level)

    print(f"Total safe levels: {total}")

if __name__ == '__main__':
    main()