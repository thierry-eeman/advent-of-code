# Import
import re
import math

# Path variables
YEAR = 2023
DAY = "04"
PUZZLE_TITLE = "scratchcards"
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    data = [line.strip() for line in file.readlines()]
    # print(data)

# Variables
NUMBER_REGEX = r'\d+'
scratch_cards = {}

# Class
class ScratchCard:
    def __init__(self) -> None:
        self.id = int
        self.instance = 1
        self.overlap = int
        self.numbers = set()
        self.winning = set()
        self.score = int

# Helper functions
def add_card_info(line: str, card: ScratchCard):
    winning_numbers = list()
    card_numbers = list()
    for number in re.findall(NUMBER_REGEX, line.split("|")[0]):
        winning_numbers.append(int(number))
        card.winning = set(winning_numbers[1:])
        card.id = winning_numbers[0]
    for number in re.findall(NUMBER_REGEX, line.split("|")[1]):
        card_numbers.append(int(number))
        card.numbers = set(card_numbers)
    return card

def calculate_card_score(card: ScratchCard):
    overlap_amount = len(card.numbers & card.winning)
    card.overlap = overlap_amount
    score = math.pow(2, overlap_amount-1)
    return int(score)

def total_score(scratch_cards: dict):
    total_score = 0
    for card in scratch_cards.values():
        total_score += card.score
    return total_score

# Main function
def main():
    for line in data:
        new_card = ScratchCard()
        card = add_card_info(line, new_card)
        card.score = calculate_card_score(card)
        scratch_cards[f"Card {card.id}"] = card
    # print(scratch_cards)
    
    pile_worth = total_score(scratch_cards)
    print(f"Your pile is worth {pile_worth} points.")
    
    for card, card_details in scratch_cards.items():
        for i in range(1, card_details.overlap+1):
            card_to_update = scratch_cards[f"Card {card_details.id+i}"]
            card_to_update.instance += 1*card_details.instance
            # print(card_to_update.id, card_to_update.instance)
    
    total_amount_of_cards = 0
    for card_details in scratch_cards.values():
        total_amount_of_cards += card_details.instance
    
    print(f"You now own {total_amount_of_cards} cards.")
        

# Main program
if __name__ == "__main__":
    main()