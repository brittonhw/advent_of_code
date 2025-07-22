
# complexity of O(n): n = len(li1) == len(li2)

def similarity_score(li1, li2):
    count_dict = {}
    result = 0

    #count occurrences in li2, store in hash
    for item in li2:
        if item in count_dict.keys():
            count_dict[item] += 1
        else:
            count_dict[item]= 1
    
    # perform similarity calculation based on occurrences
    for item in li1:
        if item in count_dict.keys():
            result = result + (item * count_dict[item]) 

    return result

def main():
    li1 = []
    li2 = []

    with open('/Users/HenryBritton/advent_of_code/2024/day1/input.txt', 'r') as file:
        for row in file:
            items = row.strip().split('   ')
            #print(items)
            if len(items) == 2:
                li1.append(int(items[0]))
                li2.append(int(items[1]))

    score = similarity_score(li1, li2)
    print('Similarity Score is:', score)

    return score



if __name__ == "__main__":
    main()