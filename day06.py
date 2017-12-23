def calc_a(input):
    states = set()
    iterations = 0
    bank = get_bank(input)
    bank_size = len(bank)
    while tuple(bank) not in states:
        states.add(tuple(bank))
        largest = max(bank)
        index = bank.index(largest)

        bank[index] = 0
        to_distribute = largest
        chunk_size = round(largest / bank_size, 0)

        while to_distribute > 0:
            index = (index + 1) % bank_size
            bank[index] += chunk_size if chunk_size <= to_distribute else to_distribute
            to_distribute -= chunk_size

        iterations += 1


    return iterations


def calc_b(input):
    states = {}
    iterations = 0
    bank = get_bank(input)
    bank_size = len(bank)
    while tuple(bank) not in states:
        states[tuple(bank)] = iterations
        largest = max(bank)
        index = bank.index(largest)

        bank[index] = 0
        to_distribute = largest
        chunk_size = round(largest / bank_size, 0)

        while to_distribute > 0:
            index = (index + 1) % bank_size
            bank[index] += chunk_size if chunk_size <= to_distribute else to_distribute
            to_distribute -= chunk_size

        iterations += 1

    first_state_iteration = states[tuple(bank)]
    return iterations - first_state_iteration


def get_bank(input):
    return list(map(lambda i: int(i, 10), input.split()))