import sys
from math import lcm

with open('8/data.txt') as f:
    lines = f.readlines()

instructions = lines[0].strip()

node_strings = lines[2:]

class MapNode:
    name: str
    left: "MapNode"
    right: "MapNode"

    def __init__(self, name: str, left: str = None, right: str = None)  -> None:
        self.name=name
        self.left=left
        self.right = right

    def __str__(self) -> str:
        return f"{self.name}"

nodes: list[MapNode] = []

for node in node_strings:
    node_name = node.split(" ")[0].strip()
    node_left_name = node.split("(")[1].split(",")[0]
    node_right_name = node.split("(")[1].split(")")[0].split(",")[1].strip()
    nodes.append(MapNode(node_name, node_left_name, node_right_name))

def assign_left_right(nodes: list[MapNode]):
    for node in nodes:
        for node2 in nodes:
            if node2.name == node.left:
                node.left = node2
            if node2.name == node.right:
                node.right = node2
print()
assign_left_right(nodes)

def get_node(name: str, nodes: list[MapNode]):
    for node in nodes:
        if node.name == name:
            return node
    return None

start_node = get_node("AAA", nodes)
sys.setrecursionlimit(20000)
def traverse(node: MapNode, passed_instructions: str, number: int = 0):
    if passed_instructions == "":
        passed_instructions = instructions
    
    if node.name == "ZZZ":
        print(number)
        return
    
    if passed_instructions[0] == "L":
        return traverse(node.left, passed_instructions[1:], number+1)
    else:
        return traverse(node.right, passed_instructions[1:], number+1)
        
def iterative_traverse(start_node, instructions):
    node = start_node
    number = 0
    restart_instructions = 0
    recursive_instructions = instructions
    while node.name != "ZZZ":
        if recursive_instructions == "":
            recursive_instructions = instructions
        if recursive_instructions[0] == "L":
            node = node.left
        else:
            node = node.right
        recursive_instructions = recursive_instructions[1:]
        number+=1
    print(number)


# traverse(start_node, instructions)
# iterative_traverse(start_node, instructions)

# Part 2


def multiple_iterative_traverse(start_nodes, instructions):
    nodes = start_nodes
    node_names_last_letter = [node.name[-1] for node in nodes]
    number = 0
    recursive_instructions = instructions
    print(node_names_last_letter)
    print(["Z"]*len(nodes))
    while any(node_names_last_letter) != ["Z"]:
        if recursive_instructions == "":
            if any(node_names_last_letter) == "Z":
                print(node_names_last_letter)
                recursive_instructions = instructions
                number = 0
            recursive_instructions = instructions
        if recursive_instructions[0] == "L":
            nodes = [node.left for node in nodes]
        else:
            nodes = [node.right for node in nodes]
        recursive_instructions = recursive_instructions[1:]
        number+=1
        node_names_last_letter = [node.name[-1] for node in nodes]
    print(number)
# multiple_iterative_traverse(start_nodes, instructions)

def modified_traverse(node: MapNode, passed_instructions: str, number: int = 0):
    if passed_instructions == "":
        passed_instructions = instructions
    
    if node.name[-1] == "Z":
        print(number)
        return
    
    if passed_instructions[0] == "L":
        return traverse(node.left, passed_instructions[1:], number+1)
    else:
        return traverse(node.right, passed_instructions[1:], number+1)

def modified_iterative_traverse(start_node, instructions):
    node = start_node
    number = 0
    restart_instructions = 0
    recursive_instructions = instructions
    while node.name[-1] != "Z":
        if recursive_instructions == "":
            recursive_instructions = instructions
        if recursive_instructions[0] == "L":
            node = node.left
        else:
            node = node.right
        recursive_instructions = recursive_instructions[1:]
        number+=1
    return(number)

start_nodes = [node for node in nodes if node.name[-1] == "A"]

numbers = []
for node in start_nodes:
    numbers.append(modified_iterative_traverse(node, instructions))
print(lcm(*numbers))