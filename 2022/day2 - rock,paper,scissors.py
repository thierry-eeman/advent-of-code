# Imports

# Read Puzzle input
with open("inputs/day2 - rps strategy.txt", 'r') as file:
    strategy_guide = [i.strip().split(" ") for i in file.readlines()]

# Variables
score_A = ["", "BX", "CY", "AZ", "AX", "BY", "CZ", "CX", "AY", "BZ"]
score_B = ["", "BX", "CX", "AX", "AY", "BY", "CY", "CZ", "AZ", "BZ"]

# Class

# Independent functions

# Main program
def main():
    total_score = 0
    for turn in strategy_guide:
        round_score = score_B.index("".join(turn))
        print(round_score)
        total_score += round_score
    print(total_score)


if __name__ == "__main__":
    main()
