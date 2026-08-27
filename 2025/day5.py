def check_id_over_ranges(ranges, ids):
    for id in ids:
        if id








if __name__ == "__main__":
    input = []
    with open("day5/input.txt") as f:
        ranges_and_ids = f.read().split('\n\n')
        ranges = ranges_and_ids[0].splitlines()
        ids = ranges_and_ids[1].splitlines()
        ids = [int(id) for id in ids]
    print(len(ranges_and_ids))
    print(len(ranges))
    print(len(ids))

