import copy
import itertools as it

import numpy as np

N_MAX = 5


def is_valid(mat, move):
    i, j = move
    if i == j:
        return False
    match mat[i], mat[j]:
        case [], _:
            return False
        case _, []:
            return True
        case x, y:
            return (len(y) < N_MAX) and (x[-1] == y[-1])
        case _:
            return False


def move(mat, movement):
    _mat = copy.deepcopy(mat)
    i, j = movement
    _mat[j].append(_mat[i].pop())
    return _mat


def to_str(mat):
    return str(tuple(map(tuple, mat)))


def all_permutations(mat):
    n_tubes = len(mat)
    return list(it.permutations(range(n_tubes), 2))


def is_blocked(mat):
    pass


def solve(mat, acc, explored):
    if is_blocked(mat):
        pass
    perms = all_permutations(input)
    for perm in perms:
        if is_valid(input, perm):
            _m = move(input, perm)
            _s = to_str(_m)
            if _s not in explored:
                explored.add(_s)
                return append(perm)


def main():
    input = [
        [1, 1, 1],
        [2, 1, 2, 1, 1],
        [
            1,
        ],
    ]
    s = to_str(input)
    explored = set({})
    explored.add(s)
    res = is_valid(input, (1, 2))
    perms = all_permutations(input)
    paths = []
    for perm in perms:
        if is_valid(input, perm):
            _m = move(input, perm)
            _s = to_str(_m)
            if _s not in explored:
                explored.add(_s)
                paths.append(perm)

    print(explored)
    print(paths)


if __name__ == "__main__":
    main()
