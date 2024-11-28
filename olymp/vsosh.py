from itertools import combinations
import math


def task1():
    n, m = map(int, input().split())
    area = n * m
    squares_to_erase = 0
    if n % 2 == 0 and m % 2 == 0:
        squares_to_erase = 4
    if n % 2 != 0 or m % 2 != 0:
        squares_to_erase = 2
    if n % 2 != 0 and m % 2 != 0:
        squares_to_erase = 1
    print(area - squares_to_erase)


def task2():
    x, y = map(int, input().split())
    scores = [10, 20, 30, 40, 50]
    indices = range(len(scores))
    correct_combinations = combinations(indices, x)
    results = set()
    for correct in correct_combinations:
        correct_set = set(correct)
        for wrong in combinations([i for i in indices if i not in correct_set], y):
            score = sum(scores[i] for i in correct_set) - \
                sum(scores[i] for i in wrong)
            results.add(score)

    print(" ".join(map(str, sorted(results))))


def task3():
    n, k, l, p = map(int, input().split())
    blocks_needed = math.ceil(n / (2 * k))

    total_length_needed = blocks_needed * 2 * p

    if total_length_needed > l or blocks_needed == 1:
        print(-1)
    else:
        remaining_space = l - total_length_needed

        if blocks_needed == 1:
            print(-1)
        else:
            max_distance_between_blocks = remaining_space // (
                blocks_needed - 1)

            print(max_distance_between_blocks)


def task4():
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    area = n * m
    doe_cells = (x2 - x1 + 1) * (y2 - y1 + 1)
    area -= doe_cells
    if x1 == x2 and y1 == y2:
        print(area // 2 - 1)
    else:
        print(area // 2)


if __name__ == "__main__":
    # task1()
    task2()
    # task3()
    # task4()
