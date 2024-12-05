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
PART = os.environ.get("PART", "B")


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    instructions = "".join(file.readlines())
    # print(instructions)
    # print(len(instructions))

# Variables


# Class


# Helper functions
def extract_mul_instructions(input_string: str):
    flag_pattern = r'do\(\)|don\'t\(\)'
    
    strict_mul_pattern = r'mul\((\d+),(\d+)\)'
    valid_mul_digit_pairs = re.findall(strict_mul_pattern, input_string)
    
    if PART == "A":
        print("through A")
        # return list(valid_mul_digit_pairs)
    else:
        print("through B")
        flags_with_location = [(match.start(), match.group()) for match in re.finditer(flag_pattern, input_string)]
        flags_with_location.insert(0, (0, "do()"))

        valid_mul_pairs_with_location = [(match.start(), match.end(), match.group()) for match in re.finditer(strict_mul_pattern, input_string)]
        # valid_mul_instructions = [f"mul({num1},{num2})" for num1, num2 in valid_mul_digit_pairs]
        valid_mul_digit_pairs = []

        for i in range(len(flags_with_location) - 1):
            flag_start, flag_type = flags_with_location[i]
            next_flag_start, next_flag_type = flags_with_location[i+1]

            if flag_type == "do()" and next_flag_type in {"do()", "don't()"}:
                valid_mul_digit_pairs += [
                    re.findall(strict_mul_pattern, match[2])[0]
                    for match in valid_mul_pairs_with_location
                    if flag_start <= match[0] < next_flag_start]
            elif flag_type == "don't()" and next_flag_type in {"do()", "don't()"}:
                pass
    print(valid_mul_digit_pairs)
    print(len(valid_mul_digit_pairs))
    return list(valid_mul_digit_pairs)

def instruction_product_sum(instructions: list):
    products = [int(num1) * int(num2) for num1, num2 in instructions]
    # print(products)
    sum_of_products = sum(products)
    return sum_of_products


# Main function
def main():
    try:
        correct_instructions = extract_mul_instructions(instructions)
        print(correct_instructions)
        all_product_sum = instruction_product_sum(correct_instructions)
        print(f"The total sum of all correction intruction products equals {all_product_sum}")
    
    except FileNotFoundError:
        print(f"The file cannot be found at {INPUT_PATH}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
if __name__ == "__main__":
    main()