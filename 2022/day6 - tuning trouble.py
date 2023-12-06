# Imports
import sys

# Read Puzzle input
with open("inputs/day6 - datastream.txt", 'r') as file:
    datastream_characters = list(file.readlines()[0])

# Variables


# Independent Functions
def is_unique(sublist, expected_length):
    return len(set(sublist)) == expected_length


# Main program
def main(part, min_processed):
    for index, letter in enumerate(datastream_characters[min_processed-1:]):
        sublist = datastream_characters[index:index+min_processed]
        if is_unique(sublist, min_processed):
            if part == "Part A":
                print(f"Start of packet after {index + min_processed}th character")
            elif part == "Part B":
                print(f"Start of message after {index + min_processed}th character")
            sys.exit()


if __name__ == "__main__":
    main("Part B", 14)
