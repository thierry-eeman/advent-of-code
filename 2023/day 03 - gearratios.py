# Imports
import json
import re
from functools import reduce

# Path variables
YEAR = 2023
DAY = "03"
PUZZLE_TITLE = 'gearratios'
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"

# Variables
SYMBOL_OPTIONS = ["*"]
REGEX_GEAR = r'\*'
REGEX_NUMBERS = r'\d+'

# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    data = [i.strip() for i in file.readlines()]
    print(data)
    symbols = [[*i] for i in data]

# Class
class Engine:
    def __init__(self) -> None:
        self.part_dict = {}
        self.symbol_dict = {}

class Part:
    def __init__(self) -> None:
        self.number = int
        self.x = int
        self.y = int
        
    def create_part(self):
        return {
            'part': self.number,
            'x': [self.x+i for i in range(len(str(self.number)))],
            'y': self.y,
            }

class Gear:
    def __init__(self) -> None:
        self.teeth = []
        self.x = int
        self.y = int
    
    def ratio(self):
        return reduce((lambda x, y: x * y), self.teeth) if len(self.teeth) == 2 else 0

# Helper functions
def map_information(data):
    engine = Engine()
    part_number = 1
    symbol_number = 1
    for y, line in enumerate(data):
        start = True
        number = ''
        symbol = ''
        for x, character in enumerate(line):
            if x == 0:
                start = True
            if character.isdigit():
                if not start:
                    number += character
                    if x == 139:
                        add_engine_part(part, engine, part_number, number, symbols, y)
                        part_number += 1
                if start:
                    part = Part()
                    part.x = x
                    part.y = y
                    number = character
                    start = False
            elif character == '.':
                if not start:
                    add_engine_part(part, engine, part_number, number, symbols, y)
                    part_number += 1
                    start = True
            else:
                if not start:
                    add_engine_part(part, engine, part_number, number, symbols, y)
                    part_number += 1
                    start = True
                if character in SYMBOL_OPTIONS:
                    engine.symbol_dict[f"Symbol {symbol_number}"] = {'symbol': character, 'x': x, 'y': y}
                symbol_number += 1
    return engine.part_dict, engine.symbol_dict

def create_adjacent_list(symbol_list, x_list, y):
    adjacent_list = []
    if y > 0:
        if x_list[0] == 0:
            row_above = symbol_list[y-1][x_list[0]:x_list[-1]+2]
        else:
            row_above = symbol_list[y-1][x_list[0]-1:x_list[-1]+2]
        adjacent_list.append(row_above)
    if y < 139:
        if x_list[0] == 0:
            row_below = symbol_list[y+1][x_list[0]:x_list[-1]+2]
        else:
            row_below = symbol_list[y+1][x_list[0]-1:x_list[-1]+2]
        adjacent_list.append(row_below)
    if x_list[0] > 0:
        left = symbol_list[y][x_list[0]-1]
        adjacent_list.append(left)
    if x_list[-1] < 139:
        right = symbol_list[y][x_list[-1]+1]
        adjacent_list.append(right)
    return adjacent_list

def unique_symbols(symbol_list):
    flattened_list = [item for sublist in symbol_list for item in sublist]
    unique_list = list(set(flattened_list))
    return unique_list

def add_engine_part(part:Part, engine:Engine, part_number, number:int, symbols:list, y:int):
    part.number = int(number)
    engine.part_dict[f'Part {part_number}'] = part.create_part()
    adjacent_items = create_adjacent_list(symbols, engine.part_dict[f'Part {part_number}']['x'], y)
    engine.part_dict[f'Part {part_number}']["Adjacent"] = adjacent_items
    engine.part_dict[f'Part {part_number}']["Unique"] = unique_symbols(adjacent_items)

def find_possible_gears(input_data):
    gears = dict()
    for row, line in enumerate(input_data):
        for symbol in re.finditer(REGEX_GEAR, line):
            gears[(row, symbol.start())] = []
    
    for index, line in enumerate(input_data):
        for number in re.finditer(REGEX_NUMBERS, line):
            for row in range(index-1, index+2):
                for column in range(number.start()-1, number.end()+1):
                    if (row, column) in gears:
                        gears[(row, column)].append(int(number.group()))
    return gears

def calculate_gear_ratios(gear_dict):
    gear_ratio_sum = 0
    for nums in gear_dict.values():
        gear = Gear()
        gear.teeth = nums
        ratio = gear.ratio()
        print(ratio)
        gear_ratio_sum += ratio
    return gear_ratio_sum

# Main Function
def main():
    engine_parts, symbol_list = map_information(data)
    
    for k,v in engine_parts.items():
        if len(v["Unique"]) > 1:
            engine_parts[k]["Engine_Part"] = True
        else: 
            engine_parts[k]["Engine_Part"] = False
    
    part_values = []
                
    for k,v in engine_parts.items():
        if v["Engine_Part"]:
            part_values.append(v["part"])
    
    print(f"Total sum of all parts: {sum(part_values)}")
    # Print statements for more in depth information
    # print(engine_parts)
    
    gears = find_possible_gears(data)
    print(gears)
    ratios = calculate_gear_ratios(gears)
    print(ratios)
                
# Main program
if __name__ == "__main__":
    main()