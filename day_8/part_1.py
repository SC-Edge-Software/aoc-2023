import time
from typing import Callable, Dict, Tuple

INPUT_FILE = "input.txt"

NodeDict = Dict[str, Tuple[str, str]]


def main():
    start = time.perf_counter()
    lr_instructions, node_dict = parse_input()
    start_node = "AAA"
    end_node = "ZZZ"
    num_steps = get_num_steps(start_node, lr_instructions, node_dict, lambda s: s == end_node)
    end = time.perf_counter()
    print(f"(Part 1) Number of steps from {start_node} to {end_node}: {num_steps} | Time: {end - start}s")


def parse_input() -> Tuple[str, NodeDict]:
    with open(INPUT_FILE, "r") as f:
        inp = f.read()
        f.close()
    lr_instructions, node_strs = inp.split("\n\n")
    node_dict = {}
    for node_str in node_strs.split("\n"):
        node, lr_tuple = node_str.split(" = ")
        # Remove parentheses
        lr_tuple = lr_tuple[1:len(lr_tuple) - 1]
        l, r = lr_tuple.split(", ")
        node_dict[node] = l, r
    return lr_instructions, node_dict


def get_num_steps(start_node: str, lr_instructions: str, node_dict: NodeDict, predicate: Callable[[str], bool]) -> int:
    curr_node = start_node
    steps = 0
    lr_instructions_ptr = 0
    while not predicate(curr_node):
        curr_lr_instruction = lr_instructions[lr_instructions_ptr]
        if curr_lr_instruction == "L":
            curr_node = node_dict[curr_node][0]
        elif curr_lr_instruction == "R":
            curr_node = node_dict[curr_node][1]
        else:
            raise RuntimeError("Received unrecognized L/R instruction")
        steps += 1
        lr_instructions_ptr += 1
        if lr_instructions_ptr >= len(lr_instructions):
            lr_instructions_ptr = 0
    return steps


if __name__ == "__main__":
    main()
