def calc_a(input):
    sum = 0
    for row in input.split("\n"):
        min = 99999
        max = 0
        for v in row.split():
            val = int(v)
            if val < min:
                min = val
            if val > max:
                max = val
        sum += max-min
    return sum

def calc_b(input):
    sum = 0
    for row in input.split("\n"):
        for v1 in row.split():
            for v2 in row.split():
                if v1 == v2:
                    continue
                val1 = int(v1, 10)
                val2 = int(v2, 10)
                if val1 % val2 == 0:
                    sum += val1 / val2
                    break
    return sum
