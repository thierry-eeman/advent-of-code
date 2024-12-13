# Imports
import os
from dotenv import load_dotenv
from pathlib import Path

# Path variables
dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)
YEAR = 2024
DAY = '06'
PUZZLE_TITLE = 'guardgallivant'
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"
PART = os.environ.get("PART", "A")


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    # print(lines)

# Variables
DIRECTION_DELTAS = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}
DIRECTION_ORDER = [key for key, value in DIRECTION_DELTAS.items()]
visited_tiles = set()

# Class


# Helper functions
def coordinate_mapper(line_list: list):
    coordinates = {}
    for row, line in enumerate(line_list):
        for col, char in enumerate(line):
            if char in [".", "#"]:
                coordinates[(row,col)] = char
            else:
                coordinates[(row,col)] = char
                startpoint = ((row, col), char)
    return coordinates, startpoint

def switch_direction(current_symbol: str):
    symbol_index = DIRECTION_ORDER.index(current_symbol)
    next_symbol_index = symbol_index + 1
    
    if symbol_index == 3:
        next_symbol_index = 0
    next_symbol = DIRECTION_ORDER[next_symbol_index]
    next_symbol_vector = DIRECTION_DELTAS[next_symbol]
    
    return next_symbol_vector, next_symbol

def move_guard_until_obstacle(grid_copy: dict, direction_symbol: str, start_vector: tuple):
    direction_vector_x, direction_vector_y =DIRECTION_DELTAS[direction_symbol][0], DIRECTION_DELTAS[direction_symbol][1]
    next_position = tuple(a + b for a, b in zip(start_vector, (direction_vector_x, direction_vector_y)))
    if next_position not in grid_copy.keys():
        print(f"The guard has left the grid at location {next_position}.")
    else:
        while grid_copy[next_position] != "#":
            grid_copy[next_position] = direction_symbol
            print(f'guard moved to position {next_position}')
            last_valid_position = next_position
            next_position = tuple(a + b for a, b in zip(next_position, (direction_vector_x, direction_vector_y)))
            if next_position not in grid_copy.keys():
                print(f"The guard has left the grid at location {next_position}.")
                return grid_copy, next_position
    
    print(f"Obstacle {grid_copy[next_position]} located at {next_position}")
    
    return grid_copy, last_valid_position

def count_values_with_filter(grid_dict: dict, filter_out: set):
    count_value = sum(1 for value in grid_dict.values() if value not in {".", "#"})
    return count_value

# Main function
def main():
    original_coordinates, startpoint = coordinate_mapper(lines)
    print(original_coordinates)
    result_grid = original_coordinates.copy()
    current_symbol = startpoint[1]
    print(f"Original Startpoint: {startpoint}")
    print(f"Start symbol: {current_symbol}")
    visited = set()
    visited.add(startpoint[0])

    last_valid_position = startpoint[0]
    while last_valid_position in result_grid.keys():
        result_grid, last_valid_position = move_guard_until_obstacle(result_grid, current_symbol, last_valid_position)
        current_symbol_vector, current_symbol = switch_direction(current_symbol)
        print(last_valid_position)
        with open("./2024/inputs/guard_movement.txt", 'a') as guard_file:
            for k,v in result_grid.items():
                if k[1] == 129:
                    guard_file.writelines(v+"\n")
                else:
                    guard_file.writelines(v)
            guard_file.writelines("\n")
    
    visited_locations_count = count_values_with_filter(result_grid, {".", "#"})
    print(f"The guard has visited {visited_locations_count} locations before he left the grid.")


# Main program
if __name__ == "__main__":
    main()