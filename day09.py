def calc(input):
    score = 0
    level = 0

    i = 0

    garbage = 0

    while i < len(input):
        c = input[i]
        if c == '!':
            i += 2
            continue
        if c == '<':
            while c != '>':
                if c == '!':
                    i += 2
                    c = input[i]
                else:
                    i += 1
                    c = input[i]
                garbage += 1 if c != '>' and c != '!' else 0

        if c == '{':
            level += 1
        if c == '}':
            score += level
            level -= 1
        i += 1

    return score, garbage

def calc_a(input):
    score, _ = calc(input)
    return score


def calc_b(input):
    _, garbage = calc(input)
    return garbage

