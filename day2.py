def safe_report(nums):
    if nums[0] > nums[1]:
        incrs = False
    elif nums[0] < nums[1]:
        incrs = True
    else:
        return False
    for idx in range(len(nums) - 1):
        if nums[idx] > nums[idx + 1] and incrs:
            return False
        if nums[idx] < nums[idx + 1] and not incrs:
            return False
        if abs(nums[idx] - nums[idx + 1]) > 3 or abs(nums[idx + 1] - nums[idx]) < 1:
            return False
    return True


def part1(lines):
    safe = 0
    for line in lines:
        nums = line.strip().split()
        nums = [int(num) for num in nums]
        if safe_report(nums):
            safe += 1

    return safe


def part2(lines):
    safe = 0
    for line in lines:
        nums = line.strip().split()
        nums = [int(num) for num in nums]
        if safe_report(nums):
            safe += 1
            continue
        else:
            for i in range(len(nums)):
                test = nums[:i] + nums[i + 1 :]
                if safe_report(test):
                    safe += 1
                    break

    return safe


if __name__ == "__main__":
    with open("data/day2.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
