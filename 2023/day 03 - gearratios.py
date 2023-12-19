# Imports


# Path variables
YEAR = 2023
DAY = "03"
PUZZLE_TITLE = 'gearratios'
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    data = [i.strip() for i in file.readlines()]
    symbols = [[*i] for i in data]
    # print(symbols)

# Variables


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
            'y': self.y
            }

# Helper functions
def map_information(data):
    engine = Engine()
    part_number = 1
    symbol_number = 1
    for y, line in enumerate(data):
        start = True
        number = ''
        sybmol = ''
        for x, character in enumerate(line):
            if character.isdigit():
                if not start:
                    number += character
                if start:
                    part = Part()
                    part.x = x
                    part.y = y
                    number = character
                    start = False
            elif character == '.':
                if not start:
                    part.number = int(number)
                    engine.part_dict[f'Part {part_number}'] = part.create_part()
                    adjacent_items = create_adjacent_list(symbols, engine.part_dict[f'Part {part_number}']['x'], y)
                    
                    print(f"{engine.part_dict[f'Part {part_number}']} - {adjacent_items}")
                    part_number += 1
                    start = True
            else:
                if not start:
                    part.number = int(number)
                    engine.part_dict[f'Part {part_number}'] = part.create_part()
                    adjacent_items = create_adjacent_list(symbols, engine.part_dict[f'Part {part_number}']['x'], y)
                    print(f"{engine.part_dict[f'Part {part_number}']} - {adjacent_items}")
                    part_number += 1
                    start = True
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

# Main function
def main():
    engine_parts, symbol_list = map_information(data)
    # print(engine_parts)
    # print(symbol_list)
    for ydex, y in enumerate(symbols):
        for xdex, x in enumerate(y):
            if not x.isdigit() and x != '.':
                square = symbols[ydex-1][xdex-1:xdex+2] + symbols[ydex][xdex-1:xdex+2] + symbols[ydex+1][xdex-1:xdex+2]
                digit_present = True in (ele.isdigit() for ele in square)
                if digit_present:
                    pass
                    # print(ydex, xdex, x)
                    # print(square)
                

# Main program
if __name__ == "__main__":
    main()