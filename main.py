import copy
import itertools as it
import statistics

N_MAX = 5
N_TUBES = 4
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


def score_disorder(mat):
    d = 0
    for tube in mat:
        d += len(set(tube))
    return d


def solve(mat, path):
    if has_won(mat):
        print("WINNING")
        return path
    else:
        to_check = []
        has_valid = False
        for perm in PERMUTATIONS:
            if is_valid(mat, perm):
                has_valid = True
                _mat = move(mat, perm)
                _s = to_str(_mat)
                if has_won(_mat):
                    print("WINNING")
                    print(_mat)
                    return path + [perm]
                if _s not in explored:
                    explored.add(_s)
                    to_check.append((_mat, perm))
        if has_valid == False:
            return
        s = []
        sort_perms = sorted(to_check, key=lambda x: score_disorder(x[0]))
        for _mat_, _perm_ in sort_perms:
            s = solve(_mat_, path + [_perm_])
            if s is not None:
                return s


def is_unexplored(t):
    _, grid = t
    return to_str(grid) not in explored


def std(t):
    verif = len(t) not in (0, N_MAX)
    if len(t) <= 1:
        return N_MAX + N_MAX * verif
    else:
        return statistics.stdev(t) + N_MAX * verif


def disorder(grid):
    return sum(std(t) for t in grid)


def solve(grid, path):
    explored.add(to_str(grid))
    valid_perms = filter(lambda p: is_valid(grid, p), PERMUTATIONS)
    valid_grids = map(lambda p: (p, move(grid, p)), valid_perms)
    unexplored_grids = filter(is_unexplored, valid_grids)
    # print(list(unexplored_grids))
    sorted_by_variance = sorted(unexplored_grids, key=lambda x: disorder(x[1]))
    # print(list(sorted_by_variance))
    solved = []
    for perm, _grid in sorted_by_variance:
        if has_won(_grid):
            return path + [perm]
        else:
            solved.append(solve(_grid, path + [perm]))

    for elem in solved:
        if elem is not None:
            return elem


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
