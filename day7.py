import itertools
import os

from joblib import Parallel, delayed


def part1(lines):
    equations = []
    results = []
    for line in lines:
        res, eq = line.strip().split(":")
        eq = eq.strip()
        equations.append(eq)
        results.append(res)

    def eval_equation(equation, target):
        opss = list(itertools.product(["*", "+"], repeat=len(equation.split()) - 1))
        equation = [int(val) for val in equation.split()]
        for ops in opss:
            res = 0
            for idx, num in enumerate(equation):
                if idx == 0:
                    res += num
                else:
                    match ops[idx - 1]:
                        case "+":
                            res += num
                        case "*":
                            res *= num
            if res == int(target):
                return res

        return 0

    res = Parallel(n_jobs=os.cpu_count(), verbose=3)(
        delayed(eval_equation)(equation, target)
        for equation, target in zip(equations, results)
    )

    return sum(res)


def part2(lines):
    equations = []
    results = []
    for line in lines:
        res, eq = line.strip().split(":")
        eq = eq.strip()
        equations.append(eq)
        results.append(res)

    def eval_equation(equation, target):
        opss = list(
            itertools.product(["*", "+", "c"], repeat=len(equation.split()) - 1)
        )
        equation = [val for val in equation.split()]
        for ops in opss:
            res = ""
            for idx, num in enumerate(equation):
                if idx == 0:
                    res = num
                else:
                    match ops[idx - 1]:
                        case "+":
                            res = int(res)
                            res += int(num)
                            res = str(res)
                        case "*":
                            res = int(res)
                            res *= int(num)
                            res = str(res)
                        case "c":
                            res += num
            if int(res) == int(target):
                return int(res)

        return 0

    res = Parallel(n_jobs=os.cpu_count(), verbose=3)(
        delayed(eval_equation)(equation, target)
        for equation, target in zip(equations, results)
    )

    return sum(res)


if __name__ == "__main__":
    with open("data/day7.txt") as file:
        lines = list(file)
        part1_ans = part1(lines)
        part2_ans = part2(lines)
        print(f"Answer for Part 1: {part1_ans}")
        print(f"Answer for Part 2: {part2_ans}")
