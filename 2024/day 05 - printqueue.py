# Imports
import os
import collections
from collections import defaultdict, deque
from dotenv import load_dotenv
from pathlib import Path

# Path variables
dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)
YEAR = 2024
DAY = '05'
PUZZLE_TITLE = 'printqueue'
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"
PART = os.environ.get("PART", "A")


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    lines = [line.rstrip() for line in file.readlines()]
    split_point = lines.index("")
    page_order_rules = lines[:split_point]
    page_update_numbers = [line.split(",") for line in lines[split_point+1:]]

# Variables


# Class



# Helper functions
def define_dependencies(rules: list):
    # Creates a dictionary with pages keys and all the values that should appear before that page
    dependencies = {}
    for rule in rules:
        before, after = rule.split("|")
        if after not in dependencies:
            dependencies[after] = []
        dependencies[after].append(before)
        dependencies[after].sort()
    sorted_dependencies = collections.OrderedDict(sorted(dependencies.items()))    
    return sorted_dependencies

def is_valid_update_sequence(sequence: list, dependencies: dict):
    for page_number in range(len(sequence)-1):
        current_page = sequence[page_number]
        should_be_in_front_of_current_page = dependencies.get(current_page, [])

        for page_found_after_current_page in sequence[page_number+1:]:
            if page_found_after_current_page in should_be_in_front_of_current_page:
                return False
    return True

def fix_incorrect_sequence(sequence: list, dependencies: dict):
    fixed_sequence = []
    must_come_before = lambda a, b: b in dependencies.get(a, [])

    def insert_number(number: str, ordered_list: list):
        if not ordered_list:
            return [number]
        if must_come_before(number, ordered_list[0]):
            return [number] + ordered_list
        # elif must_come_before(ordered_list[0], number):
        #     return [ordered_list[0]] + insert_number(number, ordered_list[1:])
        else:
            return [ordered_list[0]] + insert_number(number, ordered_list[1:])
    
    for number in sequence:
        fixed_sequence = insert_number(number, fixed_sequence)
    
    return fixed_sequence


def middle_page_sum(page_number_list: list):
    all_middle_pages = [int(sequence[int((len(sequence)-1)/2)]) for sequence in page_number_list]
    middle_page_sum = sum(all_middle_pages)
    return middle_page_sum

# Main function
def main():
    # Part One - Correct sequences
    page_order_dependencies = define_dependencies(page_order_rules)
    correct_page_update_sequence = []
    incorrect_page_update_sequence = []
    fixed_page_update_sequence = []
    for sequence in page_update_numbers:
        if is_valid_update_sequence(sequence, page_order_dependencies):
            correct_page_update_sequence.append(sequence)
        else:
            incorrect_page_update_sequence.append(sequence)
    
    # Part Two - Fixed sequences
    for sequence in incorrect_page_update_sequence:
        print(sequence)
        fixed_sequence = fix_incorrect_sequence(sequence, page_order_dependencies)
        if not is_valid_update_sequence(fixed_sequence, page_order_dependencies):
            print(f"Sequence Fixed: {fixed_sequence}")
        fixed_page_update_sequence.append(fixed_sequence)
    
    correct_sequence_middle_page_sum = middle_page_sum(correct_page_update_sequence)
    print(f"There were {len(correct_page_update_sequence)} initial correct page update sequences.")
    print(f"Their sum is {correct_sequence_middle_page_sum}")

    fixed_sequence_middle_page_sum = middle_page_sum(fixed_page_update_sequence)
    print(f"There were {len(incorrect_page_update_sequence)} initial incorrect page update sequences.")
    print(f"After fixing their order, their sum is {fixed_sequence_middle_page_sum}")


# Main program
if __name__ == "__main__":
    main()