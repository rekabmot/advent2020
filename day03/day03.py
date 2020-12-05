import functools

filename = "day03/input"

with open(filename) as file_object:
    grid = [x.strip() for x in file_object.readlines()]

def test(t):
    pos = (0, 0)

    trees = 0

    while pos[1] < len(grid):
        if grid[pos[1]][pos[0]] == '#':
            trees = trees + 1

        pos = ((pos[0] + t[0]) % len(grid[0]), pos[1] + t[1])

    return trees

trajectories = [(1,1),(3,1),(5,1),(7,1),(1,2)]

print(test((3, 1)))
print(functools.reduce(lambda a, x: a * test(x), trajectories, 1))
