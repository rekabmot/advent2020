import math

filename = "day05/input"

with open(filename) as file_object:
    lines = [x.strip() for x in file_object.readlines()]

def get_seat_number(line):
    upper = 127
    lower = 0
    left = 0
    right = 7

    for letter in line[:7]:
        x = (upper + lower) / 2
        if (letter == 'F'):
            upper = math.floor(x)
        else:
            lower = math.ceil(x)

    for letter in line[7:]:
        x = (left + right) / 2
        if (letter == 'L'):
            right = math.floor(x)
        else:
            left = math.ceil(x)

    return upper * 8 + left

highest = 0

results = []

for line in lines:
    result = get_seat_number(line)

    results.append(result)

    if (result > highest):
        highest = result

print(highest)

results.sort()

for i in range(1, len(results)):
    if(results[i] - results[i - 1] > 1):
        print(results[i] - 1)