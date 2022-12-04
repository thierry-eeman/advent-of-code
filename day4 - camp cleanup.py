# Imports

# Read Puzzle input
with open("inputs/day4 - section assignments.txt", 'r') as file:
    camp_assignment_pairs = [[[eval(k) for k in j.split('-')] for j in i.strip().split(",")] for i in file.readlines()]
    camp_assignment_section_ranges = [[range(a, b+1) for a, b in i] for i in camp_assignment_pairs]
    
# Variables

# Class


# Independent functions
def range_within_range(first_range, second_range):
    return (first_range.start in second_range and first_range[-1] in second_range) or\
        (second_range.start in first_range and second_range[-1] in first_range)


def range_overlapping(first_range, second_range):
    return set(first_range).intersection(second_range) or set(second_range).intersection(first_range)


# Main program
def main(part):
    full_overlap = 0
    if part == "part A":
        for camp_assignment_pair in camp_assignment_section_ranges:
            if range_within_range(camp_assignment_pair[0], camp_assignment_pair[1]):
                full_overlap += 1
    if part == "part B":
        for camp_assignment_pair in camp_assignment_section_ranges:
            if range_overlapping(camp_assignment_pair[0], camp_assignment_pair[1]):
                full_overlap += 1

    print(camp_assignment_section_ranges)
    print(full_overlap)


if __name__ == "__main__":
    main("part B")
