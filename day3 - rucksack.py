# Imports
import string

# Read Puzzle input
with open("inputs/day3 - rucksack.txt", 'r') as file:
    rucksack = [i.strip() for i in file.readlines()]

# Variables

# Class


# Independent functions
def split_string_in_half(original_string, parts=2):
    first_part, second_part = original_string[:len(original_string)//parts], original_string[len(original_string)//parts:]
    return first_part, second_part


def assign_value_to_letter(letter):
    alphabet = dict(zip(string.ascii_lowercase, range(1, 27))) | dict(zip(string.ascii_uppercase, range(27, 53)))
    score = alphabet[letter]
    print(alphabet)
    return score


# Main program
def main():
    total_priority = 0
    for sack in rucksack:
        first_compartment, second_compartment = split_string_in_half(sack)
        common_letter = list(set(first_compartment) & set(second_compartment))[0]
        priority = assign_value_to_letter(common_letter)
        total_priority += priority
    print(total_priority)


if __name__ == "__main__":
    main()
