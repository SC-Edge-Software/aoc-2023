import re
from typing import List

INPUT_FILE = "input.txt"
NUM_REGEX = r"\d+"

class Card:
    def __init__(self, id: int, winning_nums: List[int], current_nums: List[int]):
        self.id: int = id
        self.winning_nums: List[int] = winning_nums
        self.current_nums: List[int] = current_nums

    def __str__(self) -> str:
        return f"Card {self.id}: {self.winning_nums} | {self.current_nums}" 

    def num_matches(self) -> int:
        """Determines the number of current numbers that match the winning numbers.

        Returns:
            int: The number of current numbers that match the winning numbers.
        """

        num_matches = 0
        for num in self.current_nums:
            if num in self.winning_nums:
                num_matches += 1
        
        return num_matches

    def points(self) -> int:
        """Determines the number of points that the card is worth.

        Returns:
            int: The number of points that the card is worth.
        """

        num_matches = self.num_matches()
        if num_matches == 0:
            return 0

        return 2 ** (num_matches - 1)


def main():
    with open(INPUT_FILE, "r") as f:
        total_points = 0
        for line in f.readlines():
            card = parse_line(line)
            total_points += card.points()
        f.close()
    
    print(f"(Part 1) Total Points: {total_points}")


def parse_line(line: str) -> Card:
    """Parses a line of input and uses the information to construct a card object.

    Args:
        line (str): The line of input to parse.

    Returns:
        Card: The card object constructed from the information parsed from the given line of input.
    """

    card_id_str, card_info_str = line.split(":")
    card_id = int(card_id_str.split()[1])
    winning_nums_str, current_nums_str = card_info_str.split("|")
    winning_nums = [int(x) for x in re.findall(NUM_REGEX, winning_nums_str)]
    current_nums = [int(x) for x in re.findall(NUM_REGEX, current_nums_str)]

    return Card(card_id, winning_nums, current_nums)


if __name__ == "__main__":
    main()
