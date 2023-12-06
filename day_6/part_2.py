from part_1 import INPUT_FILE, Race


def main():
    with open(INPUT_FILE, "r") as f:
        inp = f.read()
        f.close()
    race = parse_input(inp)

    print(f"(Part 2) Number of Ways to Win: {race.get_num_ways_to_win()}")


def parse_input(inp: str) -> Race:
    time_str, distance_str = inp.split("\n")
    time = int((time_str.split(":")[1]).replace(" ", ""))
    distance = int((distance_str.split(":")[1]).replace(" ", ""))
    return Race(time, distance)


if __name__ == "__main__":
    main()
