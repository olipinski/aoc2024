import re


def part1(lines):
    total = 0
    pattern = re.compile(r"mul\(\d*,\d*\)")
    for line in lines:
        result = pattern.findall(line)
        for instruction in result:
            instruction = instruction[4:-1]
            n1, n2 = instruction.split(",")
            n1 = int(n1)
            n2 = int(n2)
            total += n1 * n2
    return total


def part2(lines):
    total = 0
    pattern = re.compile(r"mul\(\d*,\d*\)|do\(\)|don\'t\(\)")
    enabled = True
    for line in lines:
        result = pattern.findall(line)
        for instruction in result:
            if instruction == "do()":
                enabled = True
                continue
            elif instruction == "don't()":
                enabled = False
                continue
            else:
                if enabled:
                    instruction = instruction[4:-1]
                    n1, n2 = instruction.split(",")
                    n1 = int(n1)
                    n2 = int(n2)
                    total += n1 * n2
    return total


if __name__ == "__main__":
    with open("data/day3.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
