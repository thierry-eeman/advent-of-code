# Imports
import string

# Read Puzzle input
with open("inputs/day3 - rucksack.txt", 'r') as file:
    rucksack = [i.strip() for i in file.readlines()]
    elf_groups = [rucksack[x:x+3] for x in range(0, len(rucksack), 3)]

# Variables

# Class


# Independent functions
def split_string_in_half(original_string, parts=2):
    first_part, second_part = original_string[:len(original_string)//parts], original_string[len(original_string)//parts:]
    return first_part, second_part


def assign_value_to_letter(letter, alphabet):
    score = alphabet[letter]
    return score


# Main program
def main(part):
    alphabet = dict(zip(string.ascii_lowercase, range(1, 27))) | dict(zip(string.ascii_uppercase, range(27, 53)))
    total_priority = 0
    if part == "part A":
        for sack in rucksack:
            first_compartment, second_compartment = split_string_in_half(sack)
            common_letter = list(set(first_compartment) & set(second_compartment))[0]
            priority = assign_value_to_letter(common_letter, alphabet)
            total_priority += priority
    if part == "part B":
        for group in elf_groups:
            common_letter = list(set.intersection(*map(set, group)))[0]
            priority = assign_value_to_letter(common_letter, alphabet)
            total_priority += priority
    print(total_priority)


if __name__ == "__main__":
    main("part B")
