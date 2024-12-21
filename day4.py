import re

import numpy as np


def part1(lines):
    total = 0
    arr = []
    for line in lines:
        temp = []
        for char in line.strip():
            temp.append(char)
        arr.append(temp)
    arr = np.array(arr)

    pattern = re.compile(r"(?=(XMAS|SAMX))")
    # rows
    for line in lines:
        result = pattern.finditer(line.strip())
        total += sum(1 for _ in result)  # Count matches

    # columns
    for line in arr.T:
        line = "".join(line)
        result = pattern.finditer(line)
        total += sum(1 for _ in result)

    # diagonals
    for offset in range(-len(arr) + 1, len(arr)):
        diag1 = np.diag(arr, offset)
        diag2 = np.diag(np.fliplr(arr), offset)  # anti-diagonals
        diag1 = "".join(diag1)
        diag2 = "".join(diag2)
        result1 = pattern.finditer(diag1)
        result2 = pattern.finditer(diag2)
        total += sum(1 for _ in result1)
        total += sum(1 for _ in result2)

    return total


def part2(lines):
    total = 0
    arr = []
    for line in lines:
        temp = []
        for char in line.strip():
            temp.append(char)
        arr.append(temp)
    arr = np.array(arr)

    def is_mas(diag):
        return "".join(diag) in ["MAS", "SAM"]

    for idx, row in enumerate(arr):
        if idx == 0 or idx == len(arr) - 1:
            continue

        for idy, char in enumerate(row):
            if idy == 0 or idy == len(arr) - 1:
                continue

            if char == "A":
                # Check both diagonals
                diag1 = [
                    arr[idx - 1][idy - 1],
                    arr[idx][idy],
                    arr[idx + 1][idy + 1],
                ]  # upper-left to lower-right
                diag2 = [
                    arr[idx - 1][idy + 1],
                    arr[idx][idy],
                    arr[idx + 1][idy - 1],
                ]  # upper-right to lower-left

                if is_mas(diag1) and is_mas(diag2):
                    total += 1

    return total


if __name__ == "__main__":
    with open("data/day4.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
