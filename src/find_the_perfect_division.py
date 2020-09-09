# The task:
# Form a number with total length 9 using each number from 1 - 9 once.
# E.g. 142356879
# Let us denote the positions of the numbers as
# abcdefghi
# The number must have the following attributes:
# 1 divides a
# 2 divides ab
# 3 divides abc
# 4 divides abcd
# ...

import itertools


def get_number(iteration, n):
    return int(''.join([str(n) for n in iteration[:n]]))


def iteration_can_be_excluded(iteration, i):
    number = get_number(iteration, i)
    return (number % i != 0)


def is_solution(iteration):
    for i in range(2, 9):
        if iteration_can_be_excluded(iteration, i):
            return False
    return True


if __name__ == "__main__":
    possible_iterations = list(itertools.permutations(
        [1, 2, 3, 4, 5, 6, 7, 8, 9]))

    for iteration in possible_iterations:
        if is_solution(iteration):
            print(iteration)
