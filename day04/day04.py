import re

filename = "day04/input"

with open(filename) as file_object:
    lines = [x.strip() for x in file_object.readlines()]

HGT_PATTERN = re.compile('([0-9]+)(in|cm)$')
HCL_PATTERN = re.compile('#[0-9a-f]{6}$')
PID_PATTERN = re.compile('[0-9]{9}$')

eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

class Passport:
    def validate1(self):
        if len(passport.__dict__) == 8 or (len(passport.__dict__) == 7 and getattr(passport, 'cid', None) is None):
            return True

        return False

    def validate2(self):
        if (hasattr(self, 'byr') == False or int(self.byr) < 1920 or int(self.byr) > 2002):
            return False

        if (hasattr(self, 'iyr') == False or int(self.iyr) < 2010 or int(self.iyr) > 2020):
            return False

        if (hasattr(self, 'eyr') == False or int(self.eyr) < 2020 or int(self.eyr) > 2030):
            return False

        if (hasattr(self, 'hgt') == False):
            return False

        hgt_match = HGT_PATTERN.match(self.hgt)

        if (hgt_match is None):
            return False

        height = int(hgt_match.group(1))
        unit = hgt_match.group(2)

        if ((unit == 'cm' and (height < 150 or height > 193)) or (unit == 'in' and (height < 59 or height > 76))):
            return False

        if (hasattr(self, 'hcl') == False or HCL_PATTERN.match(self.hcl) is None):
            return False

        if (hasattr(self, 'ecl') == False or self.ecl not in eye_colours):
            return False

        if (hasattr(self, 'pid') == False or PID_PATTERN.match(self.pid) is None):
            return False

        return True


passports = []

current_passport = Passport()

for line in lines:
    if (len(line) == 0):
        passports.append(current_passport)
        current_passport = Passport()
        continue

    tokens = line.split(" ")

    for token in tokens:
        k, v = token.split(":")
        setattr(current_passport, k, v)

passports.append(current_passport)

valid1 = 0
valid2 = 0

for passport in passports:
    if passport.validate1():
        valid1 = valid1 + 1
    if passport.validate2():
        valid2 = valid2 + 1

print(valid1)
print(valid2)