# Imports
import os
import re
from dotenv import load_dotenv
from pathlib import Path

# Path variables
dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)
YEAR = 2024
DAY = '04'
PUZZLE_TITLE = 'ceressearch'
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"
PART = os.environ.get("PART", "A")


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    lines = [line for line in file.readlines()]


# Variables
word = "XMAS"

# Class


# Helper functions
def reverse_strings(string_grid: list):
    reversed_string_list = [string[::-1] for string in string_grid]
    return reversed_string_list

def get_diagonals(string_grid: list, start_points: list, direction: tuple, word_length: int):
    # Extracts diagonals from the grid based on starting point and end point
    rows, cols = len(string_grid), len(string_grid[0])
    diagonals = []

    for start_row, start_col in start_points:
        diagonal = []
        while 0 <= start_row < rows and 0 <= start_col < cols:
            diagonal.append(string_grid[start_row][start_col])
            start_row += direction[0]
            start_col += direction[1]
        # if len(diagonal) >= word_length:
        #     diagonals.append(''.join(diagonal))
        diagonals.append(''.join(diagonal))
    
    return diagonals

def extract_diagonals_with_filter(string_grid: list, word: str):
    # Extracts all primary and secondary diagonals from a grid and filters them by word length.
    rows, cols = len(string_grid), len(string_grid[0])
    word_length = len(word)

    # Top-left to bottom-right
    tl_br_primary_starts = [(row, 0) for row in reversed(range(rows))] + [(0, col) for col in range(1, cols)]
    tl_br_primary_direction = (1,1)

    # Bottom-left to top-right
    bl_tr_secondary_starts = [(row, 0) for row in range(rows)] + [(rows-1, col) for col in range(1, cols)]
    bl_tr_secondary_direction = (-1,1)

    # Extract all diagionals that are the minimum length of the word
    tl_br_primary_diagonals = get_diagonals(string_grid, tl_br_primary_starts, tl_br_primary_direction, word_length)
    bl_tr_secondary_diagonals = get_diagonals(string_grid, bl_tr_secondary_starts, bl_tr_secondary_direction, word_length)

    return tl_br_primary_diagonals, bl_tr_secondary_diagonals

def search_word_in_grid(word: str, grid_lines: list):
    occurrence_counter = 0
    found_positions = []
    for line in grid_lines:
        word_positions = [found.start() for found in re.finditer(word, line)]
        occurrence_counter += len(word_positions)
        found_positions.append(word_positions)
    return occurrence_counter, found_positions

def find_x_shape(grid_lines: list):
    rows, cols = len(grid_lines), len(grid_lines[0])
    results = []
    patterns = [
        {"TL": "M", "TR": "M", "BL": "S", "BR": "S"},
        {"TL": "M", "TR": "S", "BL": "M", "BR": "S"},
        {"TL": "S", "TR": "S", "BL": "M", "BR": "M"},
        {"TL": "S", "TR": "M", "BL": "S", "BR": "M"}
    ]

    for row in range(1, rows-1):
        for col in range(1, cols-1):
            if grid_lines[row][col] == "A":
                for pattern in patterns:
                    if (
                        grid_lines[row-1][col-1] == pattern["TL"] and
                        grid_lines[row-1][col+1] == pattern["TR"] and
                        grid_lines[row+1][col-1] == pattern["BL"] and
                        grid_lines[row+1][col+1] == pattern["BR"]
                    ):
                        results.append(((row,col), pattern))
    
    return results


# Main function
def main():
    horizontal_lines = [line.rstrip()for line in lines]
    reversed_horizontal_lines = reverse_strings(horizontal_lines)
    vertical_lines = [''.join(col) for col in zip(*horizontal_lines)]
    reversed_vertical_lines = reverse_strings(vertical_lines)
    primary_diagonals, secondary_diagonals = extract_diagonals_with_filter(horizontal_lines, word)
    reversed_primary_diagonals = reverse_strings(primary_diagonals)
    reversed_secondary_diagonals = reverse_strings(secondary_diagonals)

    full_grid_lines = [
        *horizontal_lines,
        *reversed_horizontal_lines,
        *vertical_lines,
        *reversed_vertical_lines,
        *primary_diagonals,
        *reversed_primary_diagonals,
        *secondary_diagonals,
        *reversed_secondary_diagonals
    ]

    # Part 1 - Finding the word XMAS in all directions
    word_count_result, word_positions = search_word_in_grid(word, full_grid_lines)
    print(f"Total number of the given word {word} in the grid is: {word_count_result}")
    
    # Part 2 - Finding all the MAS in the shape of a cross (X) in the grid.

    word_x_shape_occurrences = find_x_shape(horizontal_lines)
    print(f"The word MAS in the shape of an X is found {len(word_x_shape_occurrences)} times in this grid.")

# Main program
if __name__ == "__main__":
    main()