import math


def calc_a(input):
    if input == 1:
        return 0

    side_length = 1
    while math.sqrt(input) > side_length:
        side_length += 2
    inner_width = side_length-2
    return abs((input - math.pow(inner_width, 2)) % (side_length - 1) - math.floor(side_length / 2)) + math.floor(side_length / 2)


def calc_b(input):
    graph = Graph()

    while graph.get_value() <= input:
        graph.move()

    return graph.get_value()


class Graph:
    def __init__(self):
        self.direction = 0
        self.nodes = {}
        self.x = 0
        self.y = 0

    def get_value(self):

        if self.direction == 0:
            n1 = (self.x + 1, self.y - 1)
            n2 = (self.x + 1, self.y)
            n3 = (self.x + 1, self.y + 1)

            n4 = (self.x, self.y + 1)

        elif self.direction == 1:
            n1 = (self.x - 1, self.y + 1)
            n2 = (self.x,     self.y + 1)
            n3 = (self.x + 1, self.y + 1)

            n4 = (self.x - 1, self.y)

        elif self.direction == 2:
            n1 = (self.x - 1, self.y - 1)
            n2 = (self.x - 1, self.y)
            n3 = (self.x - 1, self.y + 1)

            n4 = (self.x, self.y - 1)

        else:
            n1 = (self.x - 1, self.y - 1)
            n2 = (self.x,     self.y - 1)
            n3 = (self.x + 1, self.y - 1)

            n4 = (self.x + 1, self.y)

        value = self.nodes.get(n1, 0) + self.nodes.get(n2, 0) + self.nodes.get(n3, 0) + self.nodes.get(n4, 0)
        return value if value > 0 else 1

    forward_moves = {
        0: (0, -1),  #down
        1: (1, 0),  #rigth
        2: (0, +1), #up
        3: (-1, 0)  #left
    }

    def has_node_to_the_left (self):
        left_move = self.forward_moves[(self.direction + 1) % 4]
        x_ = self.x + left_move[0]
        y_ = self.y + left_move[1]
        return (x_, y_) in self.nodes

    def move(self):
        #save value for current node position
        self.nodes[self.x, self.y] = self.get_value()

        #try move left
        if not self.has_node_to_the_left():
            self.direction = (self.direction + 1) % 4

        move = self.forward_moves.get(self.direction)
        self.x += move[0]
        self.y += move[1]
