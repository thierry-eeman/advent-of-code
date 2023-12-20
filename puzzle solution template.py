# Imports
import os
from dotenv import load_dotenv
from pathlib import Path

# Path variables
dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)
YEAR = int
DAY = int
PUZZLE_TITLE = str
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"
PART = os.environ.get("PART", "A")


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    pass

# Variables


# Class


# Helper functions


# Main function
def main():
    pass

# Main program
if __name__ == "__main__":
    main()