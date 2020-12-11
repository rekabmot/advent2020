import functools

filename = "day10/input"

with open(filename) as file_object:
    lines = [int(x.strip()) for x in file_object.readlines()]



lines = sorted(lines)

device_rating = lines[-1] + 3

lines.append(device_rating)
lines.insert(0, 0)

diff_1 = 0
diff_3 = 0

for i in range(1, len(lines)):
    if lines[i] - lines[i - 1] == 3:
        diff_3 = diff_3 + 1
    
    if lines[i] - lines[i - 1] == 1:
        diff_1 = diff_1 + 1

# Part 1
print(diff_1 * diff_3)


segments = []
current_segment = [0]

for i in range(1, len(lines)):
    if lines[i] - lines[i - 1] == 3:
        segments.append(current_segment)
        current_segment = [lines[i]]
    else:
        current_segment.append(lines[i])

segments.append(current_segment)

def explore(index, input):
    x = index + 1

    if x >= len(input):
        return 1

    found_routes = 0
    while x < len(input) and input[x] - input[index] <= 3:
        found_routes += explore(x, input)
        x = x + 1

    return found_routes

routes_per_segment = [explore(0, segment) for segment in segments]
print(functools.reduce(lambda acc, x: acc * x, routes_per_segment, 1))

