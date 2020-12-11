filename = "day09/input"

with open(filename) as file_object:
    lines = [int(x.strip()) for x in file_object.readlines()]



# Part 1
def validate(number, preceding_numbers):
    for a in range(0, len(preceding_numbers)):
        for b in range(a, len(preceding_numbers)):
            if preceding_numbers[a] + preceding_numbers[b] == number:
                return True

    return False

preamble_length = 25

invalid_number = 0

for i in range(preamble_length, len(lines)):
    if not validate(lines[i], lines[i - preamble_length:i]):
        invalid_number = lines[i]
        break

print(invalid_number)


for x in range(0, len(lines)):
    for y in range(x, len(lines)):
        test_range = lines[x:y]
        test_range_sum = sum(test_range)
        if test_range_sum == invalid_number:
            
            print(min(test_range) + max(test_range))

        if test_range_sum > invalid_number:
            break


        
