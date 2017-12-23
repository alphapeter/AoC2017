import math


def calc_a(input):
    count = 0
    for row in input.split('\n'):
        count += 1 if verify_row(row) else 0

    return count


def verify_row(row):
    tokens = row.split()
    for i, t1 in enumerate(tokens):
        # print(i, t1, tokens[:i] + tokens[i + 1:])
        for t2 in (tokens[:i] + tokens[i + 1:]):
            if t1 == t2:
                return False
    return True






def verify_row_b(row):
    tokens = row.split()
    for i, t1 in enumerate(tokens):
        # print(i, t1, tokens[:i] + tokens[i + 1:])
        for t2 in (tokens[:i] + tokens[i + 1:]):
            if ''.join(sorted(t1)) == ''.join(sorted(t2)):
                return False
    return True

def calc_b(input):
    count = 0
    for row in input.split('\n'):
        count += 1 if verify_row_b(row) else 0

    return count
