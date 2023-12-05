import re
from typing import List, Tuple

INPUT_FILE = "input.txt"
SEEDS_REGEX = r"seeds:( \d+)+"
NUM_REGEX = r"\d+"
MAP_REGEX = r"([a-z]+-to-[a-z]+ map:\n(\d+ \d+ \d+\n?)+)"
MAP_RANGE_REGEX = r"\d+ \d+ \d+"


class Map:
    def __init__(self):
        self.dest_ranges: List[range] = []
        self.src_ranges: List[range] = []
    
    def add_dest_range(self, range: range):
        self.dest_ranges.append(range)
    
    def add_src_range(self, range: range):
        self.src_ranges.append(range)


class Seed:
    def __init__(self, num: int):
        self.num: int = num


def main():
    with open(INPUT_FILE, "r") as f:
        inp = f.read()
        f.close()

    seeds, maps = parse_input(inp)
    converted_seed_values = []
    for seed in seeds:
        converted_seed_values.append(convert_seed_number(seed, maps)) 
    
    lowest_location_number = min(converted_seed_values)
    print(f"(Part 1) Lowest Location Number: {lowest_location_number}")


def parse_input(inp: str) -> Tuple[List[Seed], List[Map]]:
    """Parses the contents of the input file to retrieve a list of seeds and maps.

    Args:
        inp (str): The contents of the input fil.

    Returns:
        Tuple[List[Seed], List[Map]]: (<list_of_seeds>, <list_of_maps>).
    """

    # Parse the seeds
    seeds_str = re.match(SEEDS_REGEX, inp).group()
    seeds = [Seed(int(x)) for x in re.findall(NUM_REGEX, seeds_str)]

    # Parse the maps
    maps = []
    map_strs = re.findall(MAP_REGEX, inp)
    for map_str in map_strs:
        curr_map = Map()
        map_str = map_str[0] # Required since multiple groups are captured in regex
        range_strs = re.findall(MAP_RANGE_REGEX, map_str)
        for range_str in range_strs:
            dest_range_start_str, src_range_start_str, range_length_str = range_str.split()
            dest_range_start = int(dest_range_start_str)
            src_range_start = int(src_range_start_str)
            range_length = int(range_length_str)
            dest_range = range(dest_range_start, dest_range_start + range_length)
            src_range = range(src_range_start, src_range_start + range_length)
            curr_map.add_dest_range(dest_range)
            curr_map.add_src_range(src_range)

        maps.append(curr_map)

    return seeds, maps


def convert_seed_number(seed: Seed, maps: List[Map]) -> int:
    """Converts a given seed's number using a list of maps.

    Args:
        seed (Seed): The seed to convert.
        maps (List[map]): The list of maps used to convert the seed.

    Returns:
        int: The result of the conversion.
    """

    result = seed.num
    for curr_map in maps:
        for i, src_range in enumerate(curr_map.src_ranges):
            if result in src_range:
                # Retrieve the corresponding destination map
                dest_range = curr_map.dest_ranges[i]

                # Determine the index into the destination range
                idx = result - src_range.start

                # Retrieve the corresponding destination value
                result = dest_range[idx]
                break
    
    return result


if __name__ == "__main__":
    main()
