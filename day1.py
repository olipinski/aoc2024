import numpy as np


def part1(lines):
    lefts = []
    rights = []
    for line in lines:
        split = line.strip().split()
        left = split[0]
        right = split[-1]
        lefts.append(int(left))
        rights.append(int(right))

    lefts = sorted(lefts)
    rights = sorted(rights)

    res = 0
    for idx in range(len(lefts)):
        res += abs(lefts[idx] - rights[idx])

    return res


def part2(lines):
    lefts = []
    rights = []
    for line in lines:
        split = line.strip().split()
        left = split[0]
        right = split[-1]
        lefts.append(int(left))
        rights.append(int(right))

    lefts, lefts_counts = np.unique(lefts, return_counts=True)
    rights, rights_counts = np.unique(rights, return_counts=True)

    res = 0
    for left in lefts:
        if rights_counts[rights == left].size > 0:
            res += rights_counts[rights == left][0] * left

    return res


if __name__ == "__main__":
    with open("data/day1.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
