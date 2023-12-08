import math
import time
from typing import Callable, List

from part_1 import NodeDict, parse_input, get_num_steps


def main():
    start = time.perf_counter()
    lr_instructions, node_dict = parse_input()
    start_nodes = [node for node in node_dict if node.endswith("A")]
    num_steps = get_num_steps_simultaneous(start_nodes, lr_instructions, node_dict, lambda s: s.endswith("Z"))
    end = time.perf_counter()
    print(f"(Part 2) Number of Steps: {num_steps} | Time: {end - start}s")


def get_num_steps_simultaneous(start_nodes: List[str], lr_instructions: str, node_dict: NodeDict, predicate: Callable[[str], bool]) -> int:
    num_steps_list = [get_num_steps(node, lr_instructions, node_dict, predicate) for node in start_nodes] 
    num_steps = math.lcm(*num_steps_list)
    return num_steps


if __name__ == "__main__":
    main()
