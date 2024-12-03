# Imports
import os
from dotenv import load_dotenv
from pathlib import Path

# Path variables
dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)
YEAR = 2024
DAY = '01'
PUZZLE_TITLE = 'historianhysteria'
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"
PART = os.environ.get("PART", "A")


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    lines = [line.rstrip().split() for line in file.readlines()]


# Variables
sorted_column_1 = sorted([int(line[0]) for line in lines])
sorted_column_2 = sorted([int(line[1]) for line in lines])

# Class


# Helper functions
def difference_counter(list_a: list, list_b: list):
    difference_list = []
    for i, number in enumerate(list_a):
        difference_list.append(abs(number - list_b[i]))
    print(difference_list)
    print(sum(difference_list))

def similarity(list_a: list, list_b: list):
    similarity_score_list = []
    for i, number in enumerate(list_a):
        similarity_score = number*list_b.count(number)
        similarity_score_list.append(similarity_score)
    print(sum(similarity_score_list))


        


# Main function
def main():
    difference_counter(sorted_column_1, sorted_column_2)
    similarity(sorted_column_1, sorted_column_2)

# Main program
if __name__ == "__main__":
    main()