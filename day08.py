mut_reg = 0
mut_op = 1
mut_val = 2

condition_reg = 4
condition_op = 5
condition_val = 6


def check_condition(registers, reg, op, val):
    if op == '>':
        return registers.get(reg, 0) > val
    if op == '<':
        return registers.get(reg, 0) < val
    if op == '>=':
        return registers.get(reg, 0) >= val
    if op == '<=':
        return registers.get(reg, 0) <= val
    if op == '==':
        return registers.get(reg, 0) == val
    if op == '!=':
        return registers.get(reg, 0) != val


def get_mutation(op, val):
    if op == 'inc':
        return val
    if op == 'dec':
        return -val


def calc(input):
    registers = {}
    max_val = 0
    rows = input.split('\n')
    for row in rows:
        instr = row.split()
        if check_condition(registers, instr[condition_reg], instr[condition_op], int(instr[condition_val])):
            reg = instr[mut_reg]
            new_val = registers.get(reg, 0) + get_mutation(instr[mut_op], int(instr[mut_val]))
            registers[reg] = new_val
            if new_val > max_val:
                max_val = new_val

    return registers, max_val


def calc_a(input):
    registers, _ = calc(input)
    return max(registers.values())


def calc_b(input):
    _, max_val = calc(input)
    return max_val

