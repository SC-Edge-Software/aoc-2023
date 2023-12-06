from typing import List

INPUT_FILE = "input.txt"


class Race:
    def __init__(self, time: int, record: int):
        self.time = time
        self.record = record

    def get_num_ways_to_win(self) -> int:
        """Computes the number of ways that the race's record can be beaten.

        Returns:
            int: The number of ways the reace's record can be beaten.
        """

        return self.get_max_button_time_for_win() - self.get_min_button_time_for_win() + 1

    def get_min_button_time_for_win(self) -> int:
        """Determines the minimum time in ms that the button must be held down for to beat
        this race's record.

        Returns:
            int: The minimum amount of time in ms the button must be held down for.
        """

        button_time = 1
        while not self.get_boat_distance(button_time) > self.record:
            button_time += 1
        return button_time
    
    def get_max_button_time_for_win(self) -> int:
        """Determines the maximum time in ms that the button must be held down for to beat
        this race's record.

        Returns:
            int: The maximum amount of time in ms the button must be held down for.
        """

        button_time = self.time - 1
        while not self.get_boat_distance(button_time) > self.record:
            button_time -= 1
        return button_time

    def get_boat_distance(self, button_time: int) -> int:
        """Determines the distance a boat will travel in mm in this race given an amount of time in
        ms that the button was held down for.

        Args:
            button_time (int): The amount of time in ms that the button was held down for.

        Returns:
            int: The distance traveled in mm by the boat.
        """

        return button_time * (self.time - button_time)


def main():
    with open(INPUT_FILE, "r") as f:
        inp = f.read()
        f.close()
    races = parse_input(inp)
    answer = 1
    for race in races:
        answer *= race.get_num_ways_to_win()
    print(f"(Part 1) Answer: {answer}")


def parse_input(inp: str) -> List[Race]:
    """Parses the input to retrieve a list of races.

    Args:
        inp (str): The input string to parse.

    Returns:
        List[Race]: A list of the parsed races.
    """

    times_str, distances_str = inp.split("\n")
    times = [int(x) for x in (times_str.split(":")[1]).split()]
    distances = [int(x) for x in (distances_str.split(":")[1]).split()]
    races = []
    for time, distance in zip(times, distances):
        races.append(Race(time, distance))
    return races


if __name__ == "__main__":
    main()
