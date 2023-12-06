# Imports


# Path variables
YEAR = 2023
DAY = 1
PUZZLE_TITLE = "trebuchet"
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    print(INPUT_PATH)
    data = [line.strip() for line in file.readlines()]

# Variables


# Class
class Trebuchet:
    instances = 0
    def __init__(self) -> None:
        type(self).instances += 1
        self.calibration_list = list
    
    
        

# Helper functions


# Main function
def main():
    trebuchet = Trebuchet()
    trebuchet.calibration_list = data
    print(trebuchet.calibration_list)

# Main program
if __name__ == "__main__":
    main()