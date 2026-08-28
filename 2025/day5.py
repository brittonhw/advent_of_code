# return count of ids in the ranges
def check_id_over_ranges(ids, ranges):

    valid_id_count = 0
    for id in ids:
       valid_id_count += 1 if check_id(id, ranges) else 0

    return valid_id_count


def check_id(id, ranges):

    for id_range in ranges:
        if id >= id_range[0] and id <= id_range[1]:
            return True
    return False 


def build_non_overlap_ranges(ranges):
    cannonical_ranges = [ranges[0]] # this variable will be ranges without overlaps

    for id_range in ranges: # first range should just be total overlap here
        for range_candidate in cannonical_ranges:
            # if overlapping adjust window
            if id_range[0] <= range_candidate[1] and id_range[1] >= range_candidate[0]:
                range_candidate[0] = min(id_range[0], range_candidate[0])
                range_candidate[1] = max(id_range[1], range_candidate[1])
                




if __name__ == "__main__":
    input = []
    with open("day5/input.txt") as f:
        # split first at the blank space
        ranges_and_ids = f.read().split('\n\n')

        # convert ranges to ranges
        ranges = ranges_and_ids[0].splitlines()
        ranges = [[int(id) for id in id_range.split('-')] for id_range in ranges]

        # convert ids to ints
        ids = ranges_and_ids[1].splitlines()
        ids = [int(id) for id in ids]
    print(len(ranges_and_ids))
    print(len(ranges))

    print (ranges[0], ranges[1])
    print('Valid ID count:', check_id_over_ranges(ids, ranges))


