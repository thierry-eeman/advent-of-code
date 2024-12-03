# Imports
import os
import re
from dotenv import load_dotenv
from pathlib import Path

# Path variables
dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)
YEAR = 2024
DAY = '03'
PUZZLE_TITLE = 'mullitover'
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"
PART = os.environ.get("PART", "A")


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    instructions = "".join(file.readlines())
    print(instructions)
    print(len(instructions))

# Variables


# Class


# Helper functions
def extract_mul_instructions(input_string: str):
    loose_mul_pattern = r'mul\([^)]*\)'
    strict_mul_pattern = r'mul\((\d+),(\d+)\)'
    valid_mul_digit_pairs = re.findall(strict_mul_pattern, input_string)
    valid_mul_instructions = [f"mul({num1},{num2})" for num1, num2 in valid_mul_digit_pairs]
    print(valid_mul_instructions)
    return list(valid_mul_digit_pairs)

def instruction_product_sum(instructions: list):
    products = [int(num1) * int(num2) for num1, num2 in instructions]
    print(products)
    sum_of_products = sum(products)
    return sum_of_products


# Main function
def main():
    correct_instructions = extract_mul_instructions(instructions)
    print(correct_instructions)
    all_product_sum = instruction_product_sum(correct_instructions)
    print(f"The total sum of all correction intruction products equals {all_product_sum}")

# Main program
if __name__ == "__main__":
    main()