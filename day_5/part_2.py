import re
from typing import List, Tuple

from part_1 import INPUT_FILE, MAP_REGEX, MAP_RANGE_REGEX, SEEDS_REGEX, Map


def main():
    with open(INPUT_FILE, "r") as f:
        inp = f.read() 
        f.close()

    seed_ranges, maps = parse_input(inp)
    min_location_num = get_minimum_location_num(seed_ranges, maps)

    print(f"(Part 2) Minimum Location Number: {min_location_num}")


def parse_input(inp) -> Tuple[List[range], List[Map]]:
    # Parse the seed ranges
    seed_ranges = []
    seeds_str = re.match(SEEDS_REGEX, inp).group()
    seeds_str = seeds_str.split(":")[1]
    seed_vals = [int(x) for x in seeds_str.split()]
    curr_range_start = 0
    curr_range_length = 0
    for i, seed_val in enumerate(seed_vals):
        if i % 2 == 0:
            curr_range_start = seed_val
        else:
            curr_range_length = seed_val
            seed_ranges.append(range(curr_range_start, curr_range_start + curr_range_length))

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

    return seed_ranges, maps


def get_minimum_location_num(seed_ranges: List[range], maps: List[Map]) -> int:
    location_num = 0
    while not num_maps_to_seed(location_num, seed_ranges, maps):
        location_num += 1

    return location_num 


def num_maps_to_seed(num: int, seed_ranges: List[range], maps: List[Map]) -> bool:
    # Iterate backwards through the maps
    for i, curr_map in enumerate(maps[::-1]):
        # Determine the source value that the current destination value maps to
        for j, dest_range in enumerate(curr_map.dest_ranges):
            if num in dest_range:
                # Retrieve the source range that corresponds to the current destination range
                src_range = curr_map.src_ranges[j]

                # Retrieve the value from the source range that corresponds with the current destination range
                idx = num - dest_range.start 
                num = src_range[idx]
                break

    # Check for the final value in the seed ranges
    for seed_range in seed_ranges:
        if num in seed_range:
            return True
    
    return False


if __name__ == "__main__":
    main()
