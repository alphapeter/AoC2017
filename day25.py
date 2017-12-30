def calc_a(input):
    tape = {}
    start_state, number_of_steps, states = parse_input(input)

    current_state_name = start_state
    position = 0
    for _ in range(number_of_steps):
        state = states[current_state_name]
        position, current_state_name = state.operate(tape, position)

    one_count = 0
    for value in tape.values():
        if value == 1:
            one_count += 1

    return one_count


def parse_input(input):
    rows = input.split('\n')
    start_state = rows[0].strip('.').split()[3]
    number_of_steps = int(rows[1].split()[5])

    states = {}

    for i in range(3, len(rows), 10):
        state = State(rows[i:i+10])
        states[state.state_name] = state

    return start_state, number_of_steps, states


class State:
    def __init__(self, rows):
        self.state_name = rows[0].strip(':').split()[2]

        self.if_zero_write = int(rows[2].strip('.').split()[4])
        self.if_zero_move = rows[3].strip('.').split()[6]
        self.if_zero_next_state = rows[4].strip('.').split()[4]

        self.if_one_write = int(rows[6].strip('.').split()[4])
        self.if_one_move = rows[7].strip('.').split()[6]
        self.if_one_next_state = rows[8].strip('.').split()[4]

    def operate(self, tape, position):
        value = tape.get(position, 0)

        if value == 0:
            tape[position] = self.if_zero_write
            next_state = self.if_zero_next_state
            move_direction = self.if_zero_move
        else:
            tape[position] = self.if_one_write
            next_state = self.if_one_next_state
            move_direction = self.if_one_move

        next_position = position + 1 if move_direction == 'right' else position - 1
        return next_position, next_state
    