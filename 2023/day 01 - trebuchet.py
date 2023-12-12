# Imports
import re

# Path variables
YEAR = 2023
DAY = "01"
PUZZLE_TITLE = "trebuchet"
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"
PART = 'B'

# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    print(INPUT_PATH)
    data = [line.strip() for line in file.readlines()]

# Variables
STRING_DICT = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
PATTERN = '|'.join(STRING_DICT.keys())
CORRECTIONS = {
    'zerone': 'zeroone',
    'oneight': 'oneeight',
    'eightwo': 'eighttwo',
    'eighthree': 'eightthree',
    'twone': 'twoone',
    'fiveight': 'fiveeight',
    'sevenine': 'sevennine'
}
CORRECTION_PATTERN = '|'.join(CORRECTIONS.keys())



# Class
class Trebuchet:
    instances = 0
    def __init__(self) -> None:
        type(self).instances += 1
        self.calibration_list = list
        
    def transform_string_to_digit(self, string):
        corrected_string = re.sub(CORRECTION_PATTERN, lambda m: CORRECTIONS.get(m.group(0)), string, flags=re.IGNORECASE)
        print(corrected_string)
        digit_string = re.sub(PATTERN, lambda m: STRING_DICT.get(m.group(0)), corrected_string, flags=re.IGNORECASE)
        return digit_string
        
    def extract_digits(self, list):
        number_list = []
        for string in list:
            print(string)
            if PART == 'B':
                string = self.transform_string_to_digit(string)
            numbers = [x for x in ''.join(re.findall(r'\d+', string))]
            number_list.append(numbers)
        return number_list
            
    def create_numbers(self, list):
        digit_list = []
        number = int
        for item in list:
            if len(item) == 1:
                number = int(item[0]+item[0])
            else:
                number = int(item[0]+item[-1])
            digit_list.append(number)
        return digit_list
    
    def summarize(self, list):
        return sum(list)


# Helper functions


# Main function
def main():
    trebuchet = Trebuchet()
    trebuchet.calibration_list = data
    digits = trebuchet.extract_digits(trebuchet.calibration_list)
    numbers = trebuchet.create_numbers(digits)
    sum = trebuchet.summarize(numbers)
    print(numbers)
    print(sum)

# Main program
if __name__ == "__main__":
    main()