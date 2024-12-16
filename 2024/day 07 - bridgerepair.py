# Imports
import os
from itertools import product, islice
from collections import defaultdict
from dotenv import load_dotenv
from pathlib import Path

# Path variables
dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)
YEAR = 2024
DAY = '07'
PUZZLE_TITLE = 'debug'
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"
PART = os.environ.get("PART", "B")


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    number_dict = {}
    overlap_dict = {}
    for line in lines:
        key, values = line.split(":")
        if int(key) in number_dict.keys():
            print(f"this number is already in there...: {key}")
            overlap_dict[int(key)] = list(map(int, values.split()))
        else: number_dict[int(key)] = list(map(int, values.split()))
    input = [number_dict, overlap_dict]

# Variables
correct_operations = defaultdict(list)
overlap_buffer = defaultdict(list)
secound_round_sum = 0

# Class


# Helper functions
def collect_true_equations(key_outcome: int, value_list: list, operators=[]):
    if not operators:
        # All operator combo's for the full list of numbers
        if len(value_list) > 1:
            operators = list(product(["+", "*"], repeat=len(value_list)-1))
        else:
            operators = []
    
    # Calculate the default correct equations
    outcome, expression = calculate_result(key_outcome, value_list, operators)
    
    return correct_operations[key_outcome], expression

def concatenate_numbers(number_list: list):
    results = set()

    def helper(current_list, start_index = 0):
        results.add(tuple(current_list))

        for i in range(start_index, len(current_list) -1):
            new_list = current_list[:i] + [int(str(current_list[i])+ str(current_list[i + 1]))] + current_list[i + 2:]
            helper(new_list, i)
        
    helper(number_list)

    return [list(result) for result in results]

def calculate_result(target: int, number_list: list, operators: list):
    result = number_list[0]
    expression = str(number_list[0])
    
    if len(number_list) == 1 and target == result:
        print(f"TRUE for {target} --> {expression}")
        correct_operations[target].append(expression)

    else:
        for op_set in operators:
            expression = str(number_list[0])
            result = number_list[0]
            for number, operator in zip(number_list[1:], op_set):
                expression += f" {operator} {number}"
                if operator == "+":
                    result += number
                elif operator == "*":
                    result *= number

            if result == target and expression not in correct_operations[target]:
                print(f"TRUE for {target} --> {expression}")
                correct_operations[target].append(expression)
    
    return correct_operations[target], expression

# Main function
def main():
    correct_operations_sum = 0
    global secound_round_sum
    for dict in input:
        for number, number_list in dict.items():
            collect_true_equations(number, number_list)
            if PART == "B":       
                # Check if a correct equation for this number has already been found.
                found_previous_run =  len(correct_operations[number])
                if found_previous_run == None:
                    found_previous_run = 0
                
                # create all alternative lists and iterate through those for correct equations.
                concatenated_alternative_lists = concatenate_numbers(number_list)
                                
                for alt_number_list in concatenated_alternative_lists:
                    a, expression_1 = collect_true_equations(number, alt_number_list)
                    if len(correct_operations[number]) > found_previous_run:
                        found_previous_run = len(correct_operations[number])
                        secound_round_sum += number
                        print(f"Found this result after concatenation: {number} - Original List {number_list} - {expression_1}")

        correct_operations_sum += sum(int(key) for key, value in correct_operations.items() if value)

        correct_operations.clear()
    
    print(f"The sum of all the true equations equals {correct_operations_sum}")
    print(f"The numbers found after concatenation add up to: {secound_round_sum}")


# Main program
if __name__ == "__main__":
    main()