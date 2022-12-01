# Imports

# Read Puzzle input
with open("inputs/day1 - calories.txt", 'r') as file:
    elf_calories_list = [{f'Elf {index+1}': [int(i) for i in group.split("\n")]} for index, group in enumerate(file.read().split("\n\n"))]
# Variables

# Class

# Independent functions


# Main program
def main():
    totals = []
    for elf in elf_calories_list:
        calories = next(iter(elf.values()))
        sum_calories = sum(calories)
        totals.append(sum_calories)
    top_three = sorted(totals)[-3:]
    print(sum(top_three))


if __name__ == "__main__":
    main()
