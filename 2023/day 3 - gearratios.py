# Imports


# Path variables
YEAR = 2023
DAY = 3
PUZZLE_TITLE = 'gearratios'
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    data = [i.strip() for i in file.readlines()]
    symbols = [[*i] for i in data]
    print(symbols)

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
            'x': self.x,
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
                    part_number += 1
                    start = True
            else:
                engine.symbol_dict[f"Symbol {symbol_number}"] = {'symbol': character, 'x': x, 'y': y}
                symbol_number += 1
    return engine.part_dict, engine.symbol_dict

# Main function
def main():
    engine_parts, symbol_list = map_information(data)
    print(engine_parts)
    print(symbol_list)
    for ydex, y in enumerate(symbols):
        for xdex, x in enumerate(y):
            if not x.isdigit() and x != '.':
                square = symbols[ydex-1][xdex-1:xdex+2] + symbols[ydex][xdex-1:xdex+2] + symbols[ydex+1][xdex-1:xdex+2]
                digit_present = True in (ele.isdigit() for ele in square)
                if digit_present:
                    print(ydex, xdex, x)
                    print(square)
                

# Main program
if __name__ == "__main__":
    main()