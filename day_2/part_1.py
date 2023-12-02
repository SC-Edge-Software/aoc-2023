from typing import List

INPUT_FILE = "input.txt"
MAX_RED = 12 
MAX_GREEN = 13
MAX_BLUE = 14


class Pull:
    """Encapsulates the information from a single bag pull regarding the number of cubes of each color that were revealed.
    """

    def __init__(self, red: int, green: int, blue: int) -> None:
        self.red: int = red
        self.green: int = green
        self.blue: int = blue
    
    def is_possible(self) -> bool:
        return self.red <= MAX_RED and self.green <= MAX_GREEN and self.blue <= MAX_BLUE


class GameInfo:
    """Encapsulates all information within a given game.
    """

    def __init__(self, id: int):
        self.id: int = id
        self.pulls: List[Pull] = []
    
    def add_pull(self, pull: Pull):
        self.pulls.append(pull)
    
    def is_possible(self) -> bool:
        for pull in self.pulls:
            if not pull.is_possible():
                return False
        
        return True


def main():
    with open(INPUT_FILE, "r") as f:
        game_id_sum = 0
        for line in f.readlines():
            game_id_sum += process_line(line)

        f.close()
    
    print(f"(Part 1) Game ID Sum: {game_id_sum}")


def process_line(line: str) -> int:
    """Processes a single line of input and returns the integer associated with it
    to be added to the running sum. This integer will be the ID of the game if it's
    deemed possible, or 0 otherwise.

    Args:
        line (str): The line of input to process.

    Returns:
        int: The integer associcated with the given line.
    """

    game_info = parse_line(line)
    if game_info.is_possible():
        print(f"{game_info.id} is possible")
        return game_info.id

    return 0


def parse_line(line: str) -> GameInfo:
    # Parse the game ID
    game_id_str, pull_info_str = line.split(": ")
    game_id = int(game_id_str.split("Game ")[1])
    game_info = GameInfo(game_id) 

    # Parse the pull info
    pull_info = pull_info_str.split("; ")
    for pulls in pull_info:
        red = 0
        green = 0
        blue = 0
        for pull in pulls.split(", "):
            num, color = pull.split(" ") 
            num = int(num)
            color = color.strip()
            if color == "red":
                red = num
            elif color == "green":
                green = num
            elif color == "blue":
                blue = num
            else:
                raise RuntimeError("Received unrecognized color")

        game_info.add_pull(Pull(red, green, blue))

    return game_info


if __name__ == "__main__":
    main()
