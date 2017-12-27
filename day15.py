factor_a = 16807
factor_b = 48271

divider = 2147483647


def calc_a(input):
    matches = 0
    bit_mask = int('1111111111111111', 2)
    gen_a, gen_b = get_start_values(input)
    for _ in range(40000000):
        gen_a = (factor_a * gen_a) % divider
        gen_b = (factor_b * gen_b) % divider

        if gen_a & bit_mask == gen_b & bit_mask:
            matches += 1

    return matches


def calc_b(input):
    matches = 0
    bit_mask = int('1111111111111111', 2)
    gen_a, gen_b = get_start_values(input)
    for _ in range(5000000):

        gen_a = (factor_a * gen_a) % divider
        while gen_a % 4 != 0:
            gen_a = (factor_a * gen_a) % divider

        gen_b = (factor_b * gen_b) % divider
        while gen_b % 8 != 0:
            gen_b = (factor_b * gen_b) % divider

        if gen_a & bit_mask == gen_b & bit_mask:
            matches += 1

    return matches


def get_start_values(input):
    generators = input.split('\n')
    start_a = int(generators[0].split()[4])
    start_b = int(generators[1].split()[4])
    return start_a, start_b
