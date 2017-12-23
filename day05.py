import math


def calc_a(input):
    jumps = 0
    pc = 0
    instruction_list = get_instructions(input)
    while 0 <= pc < len(instruction_list):
        offset = instruction_list[pc]
        instruction_list[pc] = offset + 1
        pc += offset
        jumps += 1

    return jumps

def get_instructions(input):
    return list(map(lambda i: int(i), input.split('\n')))

def calc_b(input):
    jumps = 0
    pc = 0
    instruction_list = get_instructions(input)
    while 0 <= pc < len(instruction_list):
        offset = instruction_list[pc]
        instruction_list[pc] = offset + (1 if offset < 3 else -1)
        pc += offset

        jumps += 1

    return jumps
