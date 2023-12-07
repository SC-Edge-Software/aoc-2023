from enum import Enum
import time
from typing import Any, Dict, List, Tuple

INPUT_FILE = "input.txt"
CARD_STRENGTH_DICT = {
    "A": 13,
    "K": 12, 
    "Q": 11, 
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


class HandType(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_KIND = 5
    FIVE_OF_KIND = 6


class Game:
    def __init__(self, hand: str, bid: int):
        self.hand: str = hand 
        self.bid: int = bid
        self.hand_type: HandType = get_hand_type(self.hand)
        self.hand_type_wildcard: HandType = get_hand_type_wildcard(self.hand)


def main():
    start = time.perf_counter()
    games = parse_input()
    games = sort_games(games, games_sorting_key)
    total_winnings = get_total_winnings_from_sorted_games(games)
    end = time.perf_counter()
    print(f"(Part 1) Total Winnings: {total_winnings} | Time: {end - start}s")


def parse_input() -> List[Game]: 
    with open(INPUT_FILE, "r") as f:
        inp = f.read()
        f.close()
    games: List[Game] = []
    games_strs = inp.split("\n")
    for game_str in games_strs:
        hand, bid_str = game_str.split()
        bid = int(bid_str)
        games.append(Game(hand, bid))
    return games


def sort_games(games: List[Game], key: Any, use_wildcards: bool = False) -> List[Game]:
    games_dict: Dict[HandType, List[Game]] = {}
    for game in games:
        if use_wildcards:
            hand_type = game.hand_type_wildcard
        else:
            hand_type = game.hand_type
        if hand_type not in games_dict:
            games_dict[hand_type] = [game]
        else:
            games_dict[hand_type].append(game)
    ret: List[Game] = []
    for hand_type in HandType:
        if hand_type not in games_dict:
            continue
        ret.extend(sorted(games_dict[hand_type], key=key))
    return ret


def get_total_winnings_from_sorted_games(sorted_games: List[Game]) -> int:
    total_winnings = 0
    for i, game in enumerate(sorted_games):
        rank = i + 1
        winnings = game.bid * rank
        total_winnings += winnings
    return total_winnings


def get_hand_type(hand: str) -> HandType:
    card_dict = {}
    for card in hand:
        if card not in card_dict:
            card_dict[card] = 1
        else:
            card_dict[card] += 1
    return get_hand_type_from_card_dict(card_dict)


def get_hand_type_wildcard(hand: str) -> HandType:
    card_dict = {}
    num_jokers = 0
    for card in hand:
        if card == "J":
            num_jokers += 1
            # Don't add the Jokers to the dictionary
            continue
        if card not in card_dict:
            card_dict[card] = 1
        else:
            card_dict[card] += 1
    ret = HandType.HIGH_CARD
    if num_jokers == 0:
        ret = get_hand_type_from_card_dict(card_dict)
    elif num_jokers == 1:
        if 4 in card_dict.values():                     # JAAAA
            ret = HandType.FIVE_OF_KIND
        elif 3 in card_dict.values():                   # JAAAK
            ret = HandType.FOUR_OF_KIND
        elif list(card_dict.values()).count(2) == 2:    # JAAKK
            ret = HandType.FULL_HOUSE
        elif 2 in card_dict.values():                   # JAAKQ
            ret = HandType.THREE_OF_KIND
        else:                                           # JAKQT
            ret = HandType.ONE_PAIR
    elif num_jokers == 2:
        if 3 in card_dict.values():                     # JJAAA
            ret = HandType.FIVE_OF_KIND
        elif 2 in card_dict.values():                   # JJAAK
            ret = HandType.FOUR_OF_KIND
        else:                                           # JJAKQ
            ret = HandType.THREE_OF_KIND
    elif num_jokers == 3:
        if 2 in card_dict.values():                     # JJJAA
            ret = HandType.FIVE_OF_KIND
        else:                                           # JJJAK
            ret = HandType.FOUR_OF_KIND
    else:                                               # JJJJA or JJJJJ
        ret = HandType.FIVE_OF_KIND
    return ret


def get_hand_type_from_card_dict(card_dict: Dict[str, int]) -> HandType:
    ret = HandType.HIGH_CARD
    if 5 in card_dict.values():
        ret = HandType.FIVE_OF_KIND
    elif 4 in card_dict.values():
        ret = HandType.FOUR_OF_KIND
    elif 3 in card_dict.values() and 2 in card_dict.values():
        ret = HandType.FULL_HOUSE
    elif 3 in card_dict.values():
        ret = HandType.THREE_OF_KIND
    elif list(card_dict.values()).count(2) == 2:
        ret = HandType.TWO_PAIR
    elif 2 in card_dict.values():
        ret = HandType.ONE_PAIR
    return ret


def get_card_strength(card: str, card_strength_dict: Dict[str, int]) -> int:
    if card not in card_strength_dict:
        raise RuntimeError("Received unrecognized card")
    return card_strength_dict[card]


def games_sorting_key(game: Game) -> Tuple[int, int, int, int, int]:
    return (
        get_card_strength(game.hand[0], CARD_STRENGTH_DICT),
        get_card_strength(game.hand[1], CARD_STRENGTH_DICT),
        get_card_strength(game.hand[2], CARD_STRENGTH_DICT),
        get_card_strength(game.hand[3], CARD_STRENGTH_DICT),
        get_card_strength(game.hand[4], CARD_STRENGTH_DICT)
    )


if __name__ == "__main__":
    main()
