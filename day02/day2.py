import re

filename = "day02/input"

with open(filename) as file_object:
    lines = [x.strip() for x in file_object.readlines()]

PATTERN = re.compile('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')

class Password:
    def __init__(self, line):
        rm = PATTERN.search(line)

        self.a = int(rm.group(1))
        self.b = int(rm.group(2))
        self.l = rm.group(3)
        self.p = rm.group(4)

    def apply(self, policy):
        return policy(self.a, self.b, self.l, self.p)

v1 = 0
v2 = 0

passwords = list(map(lambda x: Password(x), lines))

policy_1 = lambda a, b, l, p: 1 if p.count(l) >= a and p.count(l) <= b else 0
policy_2 = lambda a, b, l, p: 1 if ((p[a - 1] == l or p[b - 1] == l) and (p[a - 1] != p[b - 1])) else 0

print(sum(map(lambda p: p.apply(policy_1), passwords)))
print(sum(map(lambda p: p.apply(policy_2), passwords)))
