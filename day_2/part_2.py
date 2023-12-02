from typing import Tuple

from part_1 import INPUT_FILE, GameInfo, parse_line 


def main():
    with open(INPUT_FILE, "r") as f:
        set_power_sum = 0
        for line in f.readlines():
            game_info = parse_line(line)
            red_min, green_min, blue_min = min_required_for_possibility(game_info)
            set_power = red_min * green_min * blue_min
            set_power_sum += set_power

        f.close()
    
    print(f"(Part 2) Set power sum: {set_power_sum}")


def min_required_for_possibility(game_info: GameInfo) -> Tuple[int, int, int]:
    """Determines the minimum number of cubes of each color that must be present in the bag for a given game to be possible.

    Args:
        game_info (GameInfo): The game to evaluate.

    Returns:
        Tuple[int, int, int]: The minimum number of red, green, and blue cubes required to make the game possible, respectively.
    """

    red_max = 0
    green_max = 0
    blue_max = 0
    for pull in game_info.pulls:
        if pull.red > red_max:
            red_max = pull.red
        if pull.green > green_max:
            green_max = pull.green
        if pull.blue > blue_max:
            blue_max = pull.blue

    return red_max, green_max, blue_max


if __name__ == "__main__":
    main()
