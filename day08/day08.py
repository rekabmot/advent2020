filename = "day08/input"

with open(filename) as file_object:
    lines = [x.strip() for x in file_object.readlines()]



visited_instructions = []

instruction = 0
accumulator = 0

def nop(x):
    global instruction
    instruction = instruction + 1

def acc(x):
    global instruction
    global accumulator
    accumulator = accumulator + x
    instruction = instruction + 1

def jmp(x):
    global instruction
    instruction = instruction + x

functions = {
    'nop': nop,
    'acc': acc,
    'jmp': jmp
}

while instruction not in visited_instructions:
    visited_instructions.append(instruction)

    current = lines[instruction].split(' ')

    functions[current[0]](int(current[1]))

print(accumulator)