import time

from part_1 import Game, parse_input, sort_games, get_card_strength, get_total_winnings_from_sorted_games

CARD_STRENGTH_DICT = {
    "A": 13,
    "K": 12, 
    "Q": 11, 
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1
}


def main():
    start = time.perf_counter()
    games = parse_input()
    games = sort_games(games, key=wildcard_games_sorting_key, use_wildcards=True)
    total_winnings = get_total_winnings_from_sorted_games(games)
    end = time.perf_counter()
    print(f"(Part 2) Total Winnings: {total_winnings} | Time: {end - start}s")


def wildcard_games_sorting_key(game: Game):
    return (
        get_card_strength(game.hand[0], CARD_STRENGTH_DICT),
        get_card_strength(game.hand[1], CARD_STRENGTH_DICT),
        get_card_strength(game.hand[2], CARD_STRENGTH_DICT),
        get_card_strength(game.hand[3], CARD_STRENGTH_DICT),
        get_card_strength(game.hand[4], CARD_STRENGTH_DICT)
    )


if __name__ == "__main__":
    main()
