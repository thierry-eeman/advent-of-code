# Imports
import os
from dotenv import load_dotenv
from pathlib import Path
from itertools import pairwise

# Path variables
dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)
YEAR = 2024
DAY = '02'
PUZZLE_TITLE = 'rednosedreports'
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"
PART = os.environ.get("PART", "A")


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    lines = [list(map(int, line.strip().split())) for line in file.readlines()]
    print(lines)

# Variables


# Class


# Helper functions
def line_reverser(number_list: list):
    if number_list[0] > number_list[-1]:
        return list(reversed(number_list))
    else:
        return number_list

def check_strict_sequence(number_list: list):
    line_reverser(number_list)
    if all(a<b for a,b in pairwise(number_list)):
        return True
    else:
        return False
    
def is_valid(number_list: list):
    if check_strict_sequence(number_list):
        for i in range(1, len(number_list)):
            difference = number_list[i] - number_list[i-1]
            if difference < 1 or difference > 3:
                return False
        return True
    return False
    
def is_valid_with_one_removal(number_list: list):
    for i in range(len(number_list)):
        modified_list = number_list[:i] + number_list[i+1:]
        if check_strict_sequence(modified_list):
            if is_valid(modified_list):
                return True
    return False
    

# Main function
def main():
    safe_by_default_counter = 0
    safe_after_removal_counter = 0
    for line in lines:
        ascending_line = line_reverser(line)
        print(ascending_line, check_strict_sequence(ascending_line))
        if is_valid(ascending_line):
            safe_by_default_counter += 1
        else:
            if is_valid_with_one_removal(ascending_line):
                safe_after_removal_counter += 1

    print(f"Number of default safe reports: {safe_by_default_counter}")
    print(f"Number of modified safe reports: {safe_after_removal_counter}")
    print(f"Total number of safe reports: {safe_by_default_counter + safe_after_removal_counter}")


# Main program
if __name__ == "__main__":
    main()