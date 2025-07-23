


def main():
    levels = []


    with open('/Users/HenryBritton/advent_of_code/2024/day2/input.txt', 'r') as file:
        for row in file:
            items = row.strip().split(' ')

            levels.append(items)
    print(levels[0:3])


if __name__ == '__main__':
    main()