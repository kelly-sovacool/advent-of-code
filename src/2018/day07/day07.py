def main(infilename):
    steps = parse_file(infilename)
    nodes = get_nodes(steps)
    print(get_node_order(nodes))


def get_node_order(nodes):
    leaf = [node for node in nodes.values() if not node.children].pop()
    print('leaf', leaf)
    stack = [leaf]
    on_deck = leaf.parents.copy()
    print('leaf parents', leaf.parents)
    while on_deck:
        on_deck.sort()
        next_node = on_deck.pop(0)
        stack.insert(0, next_node)
        on_deck += next_node.parents.copy()
    return stack


def get_node_order_from_head(head_node):
    order = []
    available = [head_node]
    while available:
        available.sort()
        next_up = available.pop(0)
        order.append(next_up)
        print(next_up)
        available += next_up.children
    return order


def sort_nodes(nodes):
    return ''.join(node.name for node in sorted(nodes.values()))


def get_nodes(steps):
    nodes = {step: Node(step) for step in {step[0] for step in steps}.union({step[1] for step in steps})}
    for step in steps:
        current = step[0]
        child = step[1]
        nodes[current].children.append(nodes[child])
        nodes[child].parents.append(nodes[current])
    return nodes


def parse_file(infilename):
    with open(infilename, 'r') as infile:
        steps = [parse_step(line) for line in infile]
    return steps


def parse_step(line):
    current = line.strip('Step').strip()[0]
    next = line.rstrip(' can begin.\n')[-1]
    return current, next


class Node:
    def __init__(self, name):
        self.name = name
        self.children = list()
        self.parents = list()

    def __repr__(self):
        return f"{self.name}({''.join(n.name for n in self.children)})"

    def __eq__(self, other):
        return self.name == name

    def __lt__(self, other):
        return self.name < other.name



if __name__ == "__main__":
    main('input.txt')