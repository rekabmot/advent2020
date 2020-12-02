filename = "day01/input"

with open(filename) as file_object:
    lines = list(map(lambda x: int(x), file_object.readlines()))

for x in lines:
    for y in lines:
        for z in lines:
            if x + y + z == 2020:
                print(x * y * z)
