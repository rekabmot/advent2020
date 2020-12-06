import functools
import string
import operator

filename = "day06/input"

with open(filename) as file_object:
    lines = [x.strip() for x in file_object.readlines()]


def process_for_anyone(group):
    positive_responses = []

    for member in group:
        for answer in member:
            if answer not in positive_responses:
                positive_responses.append(answer) 

    return len(positive_responses)

def process_for_everyone(group):
    result = 0
    for q in string.ascii_lowercase:
        if(functools.reduce(lambda acc, x: acc and (q in x), group, True)):
            result = result + 1

    return result


groups = []
next_group = []

for line in lines:
    if len(line) == 0:
        groups.append(next_group)
        next_group = []
    else :
        next_group.append(line)

groups.append(next_group)

print(functools.reduce(lambda acc, g: acc + process_for_anyone(g), groups, 0))
print(functools.reduce(lambda acc, g: acc + process_for_everyone(g), groups, 0))