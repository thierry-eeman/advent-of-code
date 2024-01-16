# Import
import re

# Path variables
YEAR = 2023
DAY = "04"
PUZZLE_TITLE = "scratchcards"
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    data = [line.strip() for line in file.readlines()]
    print(data)

# Variables
NUMBER_REGEX = r'\d+'

# Class
class ScratchCard:
    def __init__(self) -> None:
        self.instance = int
        self.numbers = set()
        self.winning = set()

# Helper functions
def winning_numbers(line):
    winning_numbers = []
    for number in re.findall(NUMBER_REGEX, line.split("|")[0]):
        winning_numbers.append(int(number))
    return winning_numbers[1:]
    

# Main function
def main():
    for card in data:
        winners = winning_numbers(card)
        print(winners)

# Main program
if __name__ == "__main__":
    main()