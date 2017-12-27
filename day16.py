def test_a(input):
    program = ['a','b','c','d','e']
    return ''.join(execute(input, program))


def calc_a(input):
    program = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    return ''.join(execute(input, program))


def calc_b(input):
    program = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    i = 0

    while i < 1000000000:
        i += 1
        program = execute(input, program)

        if program == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']:
            print('loop at ', i)
            i = 1000000000 - 1000000000 % i

    return ''.join(program)


def execute(input, program):
    size = len(program)

    moves = input.split(',')

    for move in moves:
        if move[0] == 's':
            spin = size - int(move[1:])
            program = program[spin:] + program[:spin]

        elif move[0] == 'x':
            swap = move[1:].split('/')
            swap_a = int(swap[0])
            swap_b = int(swap[1])
            program = swap_elements(program, swap_a, swap_b)

        elif move[0] == 'p':
            swap = move[1:].split('/')
            p_a = swap[0]
            p_b = swap[1]
            swap_a = program.index(p_a)
            swap_b = program.index(p_b)

            program = swap_elements(program, swap_a, swap_b)

    return program


def swap_elements(program, swap_a, swap_b):
    temp = program[swap_a]
    program[swap_a] = program[swap_b]
    program[swap_b] = temp
    return program
