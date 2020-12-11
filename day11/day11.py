filename = "day11/input"

with open(filename) as file_object:
    lines = [list(x.strip()) for x in file_object.readlines()] 

def immediate_neighbours(x_coord, y_coord, grid):
    neighbours = 0
    for x in range(max(x_coord - 1, 0), min(x_coord + 2, len(grid))):
        for y in range(max(y_coord - 1, 0), min(y_coord + 2, len(grid))):
            if x == x_coord and y == y_coord:
                continue
            if grid[x][y] == '#':
                neighbours += 1
    
    return neighbours

directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

def apply_direction(direction, x, y, grid):
    while True:
        x += direction[0]
        y += direction[1]

        if x < 0 or y < 0 or x == len(grid) or y == len(grid) or grid[x][y] == 'L':
            return 0

        if grid[x][y] == '#':
            return 1

def cardinal_neighbours(x, y, grid):
    return sum([apply_direction(d, x, y, grid) for d in directions])

def next_generation(current_gen, neighbour_func, neighbour_limit):
    next_gen = [line.copy() for line in current_gen]

    grid_size = len(current_gen)

    for x in range(0, grid_size):
        for y in range(0, grid_size):
            if current_gen[x][y] in ['L', '#']:
                n = neighbour_func(x, y, current_gen)

                if current_gen[x][y] == 'L' and n == 0:
                    next_gen[x][y] = '#'
                elif current_gen[x][y] == '#' and n >= neighbour_limit:
                    next_gen[x][y] = 'L'

    return next_gen

def process_grid(lines, neighbour_function, neighbour_limit):
    current_gen = lines

    while True:
        next_gen = next_generation(current_gen, neighbour_function, neighbour_limit)

        if next_gen == current_gen:
            break

        current_gen = next_gen

    print(sum([x.count('#') for x in current_gen]))

process_grid(lines.copy(), immediate_neighbours, 4)
process_grid(lines.copy(), cardinal_neighbours, 5)