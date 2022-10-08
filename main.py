import copy
import itertools as it
import functools as ft

N_MAX = 5
N_TUBES = 4
N_COLORS = 2
PERMUTATIONS = list(it.permutations(range(N_TUBES), 2))
explored = set({})


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


def has_won(mat):
    for tube in mat:
        length_condition = len(tube) in (0, N_MAX)
        homogeneous_condition = all_same(tube)
        print(homogeneous_condition)
        if (not length_condition) or (not homogeneous_condition):
            return False
    return True


def all_same(tube):
    return len(set(tube)) in (0, 1)


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


def solve(mat, path):
    if has_won(mat):
        print("WINNING")
        return path
    else:
        for perm in PERMUTATIONS:
            if is_valid(mat, perm):
                _mat = move(mat, perm)
                _s = to_str(_mat)
                if has_won(_mat):
                    return path + [perm]
                if _s not in explored:
                    explored.add(_s)
                    return solve(_mat, path + [perm])


def play_paths(mat, paths):
    return list(it.accumulate(paths, move, initial=mat))


def main():
    input = [
        [1, 1, 1, 2],
        [2, 1, 2, 1],
        [2, 2],
        [],
    ]
    paths = solve(input, [])
    print(paths)
    print(play_paths(input, paths))


if __name__ == "__main__":
    main()
