import argparse

#https://adventofcode.com/2024/day/1



def main():
    li1 = []
    li2 = []

    with open('input.txt', 'r') as file:
        for row in file:
            items = row.strip().split('   ')
            print(items)
            if len(items) == 2:
                li1.append(int(items[0]))
                li2.append(int(items[1]))
    li1.sort()
    li2.sort()
    answer = 0
    for i in range(len(li1)):
        print(abs(li1[i] - li2[i]))
        answer += abs(li1[i] - li2[i])
    return answer


if __name__ == "__main__":
    main()