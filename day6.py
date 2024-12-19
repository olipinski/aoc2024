import copy
from collections import defaultdict

import numpy as np
from tqdm import tqdm


def part1(lines):
    arr_temp = []
    for line in lines:
        line = line.strip()
        char_arr = []
        for char in line:
            char_arr.append(char)
        arr_temp.append(char_arr)
    map = np.array(arr_temp)

    while True:
        temp = np.where(map == "^")
        start = [temp[0][0], temp[1][0]]
        next = start[0] - 1
        if next == -1:
            map[next][start[1]] = "X"
            break
        if map[next][start[1]] == "#":
            map = np.rot90(map)
        elif map[next][start[1]] == "." or map[next][start[1]] == "X":
            map[start[0]][start[1]] = "X"
            map[next][start[1]] = "^"

        # os.system('cls' if os.name == 'nt' else 'clear')
        # for line in map.tolist():
        #     print(line)
        # time.sleep(1)

    return np.sum(map == "X")


def part2(lines):
    arr_temp = []
    for line in lines:
        line = line.strip()
        char_arr = []
        for char in line:
            char_arr.append(char)
        arr_temp.append(char_arr)
    map = np.array(arr_temp)
    init_start = np.where(map == "^")
    init_start = [init_start[0][0].tolist(), init_start[1][0].tolist()]
    init_map = copy.deepcopy(map)
    rotations = 0

    while True:
        temp = np.where(map == "^")
        start = [temp[0][0], temp[1][0]]
        next = start[0] - 1
        if next == -1:
            map[start[0]][start[1]] = "X"
            break
        if map[next][start[1]] == "#":
            map = np.rot90(map)
            rotations += 1
            rotations %= 3
        elif map[next][start[1]] == "." or map[next][start[1]] == "X":
            map[start[0]][start[1]] = "X"
            map[next][start[1]] = "^"

    # map re-oriented
    map = np.rot90(map, k=rotations)
    x, y = np.where(map == "X")
    path = list(zip(x.tolist(), y.tolist()))
    path.remove((init_start[0], init_start[1]))

    inf_loops = 0

    for point in tqdm(path, desc="Evaluating possible obstacles"):
        new_map = copy.deepcopy(init_map)
        new_map[point[0]][point[1]] = "#"
        rotations = 0
        visited = defaultdict(int)
        while True:
            temp = np.where(new_map == "^")
            start = [temp[0][0], temp[1][0]]

            # check for inf loop
            if visited[(start[0], start[1], rotations)] >= 5:
                inf_loops += 1
                break
            else:
                visited[(start[0], start[1], rotations)] += 1

            next = start[0] - 1
            if next == -1:
                break
            if new_map[next][start[1]] == "#":
                new_map = np.rot90(new_map)
                rotations += 1
                rotations %= 4
            elif new_map[next][start[1]] == ".":
                new_map[start[0]][start[1]] = "."
                new_map[next][start[1]] = "^"

        del new_map

    return inf_loops


if __name__ == "__main__":
    with open("data/day6.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
