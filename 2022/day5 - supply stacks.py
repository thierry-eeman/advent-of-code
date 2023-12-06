# Imports

# Read Puzzle input
with open("inputs/day5 - containers.txt", 'r') as file:
    # Create list of container stacks, keep the spaces as indicator for container stack
    containers = [list(i.strip().replace("    ", " [ ]").replace("] [", "")[1:-1]) for i in file.readlines()[:8]]
    file.seek(0)
    # Create list of instruction, keep only numbers
    instructions = [i.strip().split() for i in file.readlines()[10:]]
    for instruction in instructions:
        del instruction[0::2]

# Variables
stacks = {f"Stack {index + 1}": [] for index, container in enumerate(range(len(containers[0])))}
# Turn vertical stacks into a horizontal list (first item is the top container)
for row in containers:
    for index, container in enumerate(row):
        if container != " ":
            stacks[f"Stack {index + 1}"].append(container)


# Independent Functions
def container_move(amount, origin, destination, crane="9000"):
    for index in range(int(amount)):
        stack = stacks[f"Stack {origin}"]
        container = stack.pop(0)
        if crane == "9000":
            # Insert at the start
            stacks[f"Stack {destination}"].insert(0, container)
        if crane == "9001":
            # Insert at the iterated index
            stacks[f"Stack {destination}"].insert(index, container)
    return stacks


def print_top_containers(final_stacks):
    message = "".join([value[0] for key, value in final_stacks.items()])
    return message


# Main program
def main(crane_type):
    for instruction in instructions:
        container_move(instruction[0], instruction[1], instruction[2], crane_type)
    print(print_top_containers(stacks))
    print(stacks)


if __name__ == "__main__":
    main("9001")
