import re
import functools

filename = "day07/input"

with open(filename) as file_object:
    lines = [x.strip() for x in file_object.readlines()]

COLOUR_PATTERN = re.compile("([0-9]) ([a-z ]+) bags?\.?")

bag_rules = dict()

for line in lines:
    container, contains = line.split(" contain ")

    container_color = container[:-5]

    bag_rules[container_color] = []

    for token in contains.split(", "):
        if token == 'no other bags.':
            continue

        match = COLOUR_PATTERN.match(token)
        bag_qty = int(match.group(1))
        bag_color = match.group(2)
        
        bag_rules[container_color].append((bag_color, bag_qty))

print(bag_rules)

def recursive_contains(color, search_target):
    if search_target in list(map(lambda x: x[0], bag_rules[color])):
        return True

    return functools.reduce(lambda acc, x: acc or recursive_contains(x[0], search_target), bag_rules[color], False)

def count_contained_bags(color):
    return 1 + functools.reduce(lambda acc, x: acc + x[1] * count_contained_bags(x[0]), bag_rules[color], 0)

print(functools.reduce(lambda acc, x: acc + (1 if recursive_contains(x, "shiny gold") else 0), bag_rules, 0))
print(count_contained_bags("shiny gold") - 1)




