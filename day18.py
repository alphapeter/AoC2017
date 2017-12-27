from collections import deque
def calc_a(input):
    registers = {}
    last_played_frequency = 0

    pc = 0
    rows = input.split('\n')

    while True:
        row = rows[pc]
        instruction = row.split()
        operation = instruction[0]
        reg_x = instruction[1]
        reg_y = instruction[2] if len(instruction) > 2 else ''

        if operation == 'snd':
            last_played_frequency = registers.get(reg_x, 0)

        elif operation == 'set':
            registers[reg_x] = get_value(registers, reg_y)

        elif operation == 'add':
            registers[reg_x] = registers.get(reg_x, 0) + get_value(registers, reg_y)

        elif operation == 'mul':
            registers[reg_x] = registers.get(reg_x, 0) * get_value(registers, reg_y)

        elif operation == 'mod':
            registers[reg_x] = registers.get(reg_x, 0) % get_value(registers, reg_y)

        elif operation == 'rcv':
            if last_played_frequency != 0:
                return last_played_frequency

        elif operation == 'jgz':
            if registers.get(reg_x, 0) > 0:
                val = get_value(registers, reg_y)
                if val == 0:
                    val = 1
                pc += val
                continue

        pc += 1

    return last_played_frequency


def calc_b(input):
    registers = [{'p': 0}, {'p': 1}]

    pc = [0, 0]
    rows = input.split('\n')

    queues = [deque(), deque()]
    waiting = [False, False]
    program_1_sent = 0
    id = 1

    while True:
        id = 0 if id == 1 else 1
        other_id = 0 if id == 1 else 1
        while True:
            row = rows[pc[id]]

            instruction = row.split()

            operation = instruction[0]
            reg_x = instruction[1]
            reg_y = instruction[2] if len(instruction) > 2 else ''

            if operation == 'snd':
                value = get_value(registers[id], reg_x)
                queues[other_id].append(value)

                waiting[other_id] = False
                if id == 1:
                    program_1_sent += 1

            elif operation == 'set':
                registers[id][reg_x] = get_value(registers[id], reg_y)

            elif operation == 'add':
                registers[id][reg_x] = registers[id].get(reg_x, 0) + get_value(registers[id], reg_y)

            elif operation == 'mul':
                registers[id][reg_x] = registers[id].get(reg_x, 0) * get_value(registers[id], reg_y)

            elif operation == 'mod':
                registers[id][reg_x] = registers[id].get(reg_x, 0) % get_value(registers[id], reg_y)

            elif operation == 'rcv':
                if len(queues[id]) == 0:
                    if waiting[other_id]:
                        return program_1_sent

                    waiting[id] = True
                    break
                else:
                    registers[id][reg_x] = queues[id].popleft()

            elif operation == 'jgz':
                if get_value(registers[id], reg_x) > 0:
                    val = get_value(registers[id], reg_y)
                    if val == 0:
                        val = 1
                    pc[id] += val
                    continue

            pc[id] += 1


def get_value(registers, name):
    try:
        int_val = int(name, 10)
        return int_val
    except:
        return registers.get(name, 0)
