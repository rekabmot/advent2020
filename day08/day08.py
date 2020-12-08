filename = "day08/input"

with open(filename) as file_object:
    lines = [x.strip() for x in file_object.readlines()]

class Computer:
    def __init__(self):
        self.visited_instructions = []

        self.instruction = 0
        self.accumulator = 0

    def nop(self, x):
        self.instruction = self.instruction + 1

    def acc(self, x):
        self.accumulator = self.accumulator + x
        self.instruction = self.instruction + 1

    def jmp(self, x):
        self.instruction = self.instruction + x

    def run(self, input, alter_instruction = None):
        alter_candidate = 0
        while True:
            if self.instruction in self.visited_instructions:
                print('LOOPED!')
                return False

            if self.instruction == len(input):
                print('Finished!')
                return True

            self.visited_instructions.append(self.instruction)

            current = input[self.instruction].split(' ')

            if (current[0] == 'nop' or current[0] == 'jmp'):
                alter_candidate = alter_candidate + 1

                if alter_candidate == alter_instruction:
                    if current[0] == 'nop':
                        current[0] = 'jmp'
                    else:
                        current[0] = 'nop'


            getattr(self, current[0])(int(current[1]))

        print(f'Accumulator = {self.accumulator}')

# Part 1
c = Computer()
c.run(lines)
print(c.instruction)
print(c.accumulator)

# Part 2
last_result = False
i = 0

while not last_result:
    i = i + 1

    c = Computer()
    last_result = c.run(lines, i)

print(c.instruction)
print(c.accumulator)
