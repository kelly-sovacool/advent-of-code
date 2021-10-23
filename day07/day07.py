def main(infilename):
    with open(infilename, 'r') as infile:
        steps = [parse_step(line) for line in infile]
    nodes = {step: Node(step) for step in {step[0] for step in steps}.union({step[1] for step in steps})}

    for step in steps:
        current = step[0]
        child = step[1]
        nodes[current].children.append(nodes[child])

    head_node = nodes[steps[0][0]]
    head_node.traverse(0)
    print(sorted(nodes.values()))

def parse_step(line):
    current = line.strip('Step').strip()[0]
    next = line.rstrip(' can begin.\n')[-1]
    return current, next

class Node:
    def __init__(self, name, level = -1):
        self.name = name
        self.level = level
        self.children = list()

    def __repr__(self):
        return f"{self.name}({self.level})"

    def __eq__(self, other):
        return self.level == other and self.name == name

    def __lt__(self, other):
        return self.level < other.level or ((self.level == other.level) and (self.name < other.name))

    def traverse(self, level):
        self.level = level
        level += 1
        for child in self.children:
            child.traverse(level)

if __name__ == "__main__":
    main('input.txt')