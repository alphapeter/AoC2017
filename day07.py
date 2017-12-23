import re
def calc_a(input):
    ancestors = set()

    rows = input.split('\n')
    # collect all ancestors
    for row in rows:
        if '->' in row:
            children = row.split('->')[1].split()
            for child in children:
                ancestors.add(child.replace(',', ''))

    # get node that's not an ancestor
    for row in rows:
        node = row.split()[0]
        if node not in ancestors:
            return node

    return "not found "

def calc_b(input):
    nodes = {}
    weight_patter = re.compile(".*\((\d+)\).*")

    rows = input.split('\n')
    # create all nodes
    for row in rows:
        name = row.split()[0]
        m = weight_patter.match(row)
        weight = int(m.group(1), 10)
        node = Node(weight, name)
        nodes[name] = node

    # build graph (connect all children)
    for row in rows:
        if '->' in row:
            name = row.split()[0]
            node = nodes[name]
            children = row.split('->')[1].split()
            for child in children:
                child_name = child.replace(',', '')
                child_node = nodes[child_name]
                node.add_child(child_node)

    parent_name = calc_a(input)

    parent_node = nodes[parent_name]

    return parent_node.find_imbalance()



class Node:

    def __init__(self, weight, name):
        self.weight = weight
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def get_weight(self):
        child_weights = 0

        for child in self.children:
            child_weights += child.get_weight()
        return self.weight + child_weights

    def has_imbalanced_children(self):
        if len(self.children) == 0:
            return False
        weight = self.children[0].get_weight()
        for child in self.children:
            if child.get_weight() != weight:
                return True
        return False

    def find_imbalance(self):
        # seems like there's always an overweight rather than underweight
        max = 0
        min = 999999999
        for child in self.children:
            # print(child.name, child.get_weight(), child.weight)
            if child.get_weight() < min:
                min = child.get_weight()
            if child.get_weight() > max:
                max = child.get_weight()
                unbalanced_node = child

        if unbalanced_node.has_imbalanced_children():
            return unbalanced_node.find_imbalance()

        return unbalanced_node.weight - (max - min)