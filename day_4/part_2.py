from typing import Dict, List

from part_1 import INPUT_FILE, Card, parse_line


def main():
    cards: List[Card] = []
    card_dict: Dict[int, int] = {}

    with open(INPUT_FILE, "r") as f:
        for line in f.readlines():
            card = parse_line(line)
            cards.append(card)
            card_dict[card.id] = 1
        f.close()
    
    for card in cards:
        for i in range(card.num_matches()):
            id = card.id + i + 1 
            if id > cards[-1].id:
                break
            card_dict[id] += card_dict[card.id]
        
    total_cards = sum(card_dict.values())
    print(f"(Part 2) Total Cards: {total_cards}")


if __name__ == "__main__":
    main()
