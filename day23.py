def calc_a(input):
    registers = {}

    pc = 0
    rows = input.split('\n')
    multiplies = 0
    while True:
        if pc < 0 or pc > (len(rows) - 1):
            return multiplies

        row = rows[pc]

        instruction = row.split()

        operation = instruction[0]

        reg_x = instruction[1]
        reg_y = instruction[2] if len(instruction) > 2 else ''

        if operation == 'set':
            registers[reg_x] = get_value(registers, reg_y)

        elif operation == 'sub':
            registers[reg_x] = registers.get(reg_x, 0) - get_value(registers, reg_y)

        elif operation == 'mul':
            multiplies += 1
            registers[reg_x] = registers.get(reg_x, 0) * get_value(registers, reg_y)

        elif operation == 'jnz':
            if get_value(registers, reg_x) != 0:
                val = get_value(registers, reg_y)
                if val == 0:
                    val = 1
                    pc += val

                pc += val
                continue

        pc += 1

    return multiplies


def calc_b():
    return b_optimized()


def b_step_1():
    a = 1
    b = c = d = e = f = g = h = 0

    b = 65              #set b 65
    c = b               #set c b
    if a == 0:          #jnz a 2
        pass   #GOTO B  #jnz 1 5
    b *= 100            #mul b 100
    b += 100000         #sub b -100000
    c = b               #set c b
    c += 17000          #sub c -17000
    f = 1  #B           #set f 1
    d = 2               #set d 2
    e = 2  #D           #set e 2
    g = d  #C           #set g d
    g *= e              #mul g e
    g -= b              #sub g b
    if g == 0:          #jnz g 2
        f = 0           #set f 0
    e +=1               #sub e -1
    g = e               #set g e
    g -= b              #sub g b
    #if g != 0: GOTO C  #jnz g -8
    d += 1              #sub d -1
    g = d               #set g d
    g -= b              #sub g b
    #if g != 0  GOTO D  #jnz g -13
    if f == 0:          #jnz f 2
        h += 1          #sub h -1
    g = b               #set g b
    g -= c              #sub g c
    if g == 0:          #jnz g 2
        return h #END   #jnz 1 3
    b += 17             #sub b -17
    # GOTO #B           #jnz 1 -23

def b_step_2():
    a = 1
    b = c = d = e = f = g = h = 0

    b = 65                                  #set b 65
    c = b                                   #set c b
    if a != 0:                              #jnz a 2
    #          #GOTO B                      #jnz 1 5
        b = b * 100 + 100000                #mul b 100 #sub b -100000
        c = b + 17000                       #set c b #sub c -17000
    while True:
        f = 1  #B                           #set f 1
        d = 2                               #set d 2
        while d - b != 0: # should be do while!
            e = 2  #D                       #set e 2
            while e - b != 0:
                if d * e - b == 0:          #jnz g 2 #set g d #mul g e #sub g b
                    f = 0                   #set f 0
                e +=1                       #sub e -1
                #g = e -b                   #set g e #sub g b - moved into while loop
                #if g != 0: GOTO C          #jnz g -8

            d += 1                          #sub d -1
            #g = d - b                      #set g d #sub g b -- moved into while loop
            #if g != 0  GOTO D              #jnz g -13
        if f == 0:                          #jnz f 2
            h += 1                          #sub h -1
        if b - c == 0:                          #jnz g 2 #set g b #sub g c
            return h #END                   #jnz 1 3
        b += 17                             #sub b -17
    # GOTO #B                               #jnz 1 -23 - While True


def b_step_3():

    b = c = d = e = f = g = h = 0
    b = 65 * 100 + 100000
    c = b + 17000

    while True:
        f = 1
        d = 2
        while d <= b:
            e = 2
            while e - b != 0:
                if d * e == b:
                    f = 0
                e += 1
            d += 1
        if f == 0:
            h += 1
        if b == c:
            return h
        b += 17


def b_step_4():

    b = c = d = e = f = g = h = 0
    b = 65 * 100 + 100000
    c = b + 17000

    while b <= c:
        d = 2
        while d < b:
            e = 2
            while e < b:
                if d * e == b:
                    h += 1
                    break
                e += 1
            d += 1
        b += 17


def b_optimized():
    h = 0
    b = 65 * 100 + 100000
    c = b + 17000

    while b <= c:
        d = 2
        while d < b:
            if b % d == 0:
                h += 1
                break
            d += 1
        b += 17

    return h


def get_value(registers, name):
    try:
        int_val = int(name, 10)
        return int_val
    except:
        return registers.get(name, 0)
    return 0
