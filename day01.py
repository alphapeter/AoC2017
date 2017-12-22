def calc_a(input):
    sum = 0
    current = int(input[len(input)-1], 10)
    for x in input:
        next = int(x, 10)
        if current == next:
            sum += next
        current = next
    return sum

def calc_b(input):
    sum = 0
    length = len(input)
    steps = int(length/2)
    for x in range(0, len(input)):
        a = int(input[x], 10)
        b = int(input[(x + steps) % length], 10)
        if a == b:
            sum += a
    return sum
