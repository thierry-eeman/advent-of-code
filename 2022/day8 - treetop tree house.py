# Imports
from more_itertools import locate
import pandas as pd

# Read Puzzle input
with open("inputs/day8 - forest.txt", 'r') as file:
    forest_dict = {f"Row {index+1}": list(map(int, line.strip())) for index, line in enumerate(file.readlines())}
    forest_df = pd.DataFrame(data=forest_dict)
    forest_columns = forest_df.to_numpy().tolist()
    forest_rows = forest_df.transpose().values.tolist()


# Independent functions
# Count the trees at the edge of the forest (always visible)
def perimeter(dataframe: pd.DataFrame):
    return (2 * dataframe.shape[0] + 2 * dataframe.shape[1]) - 4


# Reusable function to check if a tree can be seen from an edge
# It checks whether the tree to the edge is the largest and unique and thus visible
def boolean_visibility_check(checklist: dict):
    observe_dict = {"left": False, "right": False, "top": False, "bottom": False}
    for direction, value in checklist.items():
        observe_dict[direction] = bool(checklist[direction][-1] == max(checklist[direction]) and max(checklist[direction]) not in checklist[direction][:-1])
    is_visible = any(observe_dict.values())
    return is_visible


# takes a dictionary describing all the paths to the edge in every direction for a given tree
# reversing the lists allows the easier use of indexing
def assign_scenic_score(checklist: dict):
    checklist = {key: list(reversed(value)) for key, value in checklist.items()}
    scenic_score = 1
    for direction, value in checklist.items():
        equal_height_indexes = list(locate(value, lambda x: x >= value[0]))
        if len(equal_height_indexes) == 1:
            line_of_sight = len(value)-1
        else:
            line_of_sight = equal_height_indexes[1] - equal_height_indexes[0]
        scenic_score *= line_of_sight
    return scenic_score


# Main program
def main(part):
    visible_trees = 0
    scenic_scores = []
    for row_index, row in enumerate(forest_rows[1:-1]):
        for index, tree in enumerate(row[1:-1]):
            row_sublist_left = row[:index+2]
            row_sublist_right = list(reversed(row[index+1:]))
            column_sublist_top = forest_columns[index+1][:row_index+2]
            column_sublist_bottom = list(reversed(forest_columns[index+1][row_index+1:]))

            observation_checklist = {
                "left": row_sublist_left,
                "right": row_sublist_right,
                "top": column_sublist_top,
                "bottom": column_sublist_bottom}

            if part == "Part A":
                visible_trees += 1 if boolean_visibility_check(observation_checklist) else 0
                print(f"{tree} --> {boolean_visibility_check(observation_checklist)}")
            if part == "Part B":
                scenic_scores.append(assign_scenic_score(observation_checklist))

    if part == "Part A":
        print(visible_trees + perimeter(forest_df))
    if part == "Part B":
        print(max(scenic_scores))


if __name__ == "__main__":
    main("Part A")
