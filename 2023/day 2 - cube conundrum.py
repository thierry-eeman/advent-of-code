# Imports
import re

# Path variables
YEAR = 2023
DAY = 2
PUZZLE_TITLE = 'cubeconundrum'
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    print(INPUT_PATH)
    data = [i.strip() for i in file.readlines()]
    # print(data)

# Variables
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

# Class
class Game:
    def __init__(self) -> None:
        # Game init
        self.id = int
        self.green_cube = Cube()
        self.red_cube = Cube()
        self.blue_cube = Cube()
        
        self.green_cube.color = 'green'
        self.green_cube.amount = 0
        self.blue_cube.color = 'blue'
        self.blue_cube.amount = 0
        self.red_cube.color = 'red'
        self.red_cube.amount = 0
                        
    def print_game(self):
        print(f"Game: {self.green_cube.amount} green, {self.blue_cube.amount} blue, {self.red_cube.amount} red")
    
    def assert_possibility(self):
        if self.blue_cube.amount > MAX_BLUE:
            return False
        elif self.green_cube.amount > MAX_GREEN:
            return False
        elif self.red_cube.amount > MAX_RED:
            return False
        else:
            return True

class Cube:
    def __init__(self) -> None:
        self.color = str
        self.amount = int
    

# Helper functions


# Main function
def main():
    possible_game_count = 0
    id_sum = 0
    games = [re.split('; |, ', i.split(':')[1].strip()) for i in data]
    print(games)
    for index, game in enumerate(games):
        new_game = Game()
        new_game.id = index + 1
        for grab in game:
            turn = grab.split(' ')
            amount = int(turn[0])
            color = turn[1]
            match color:
                case 'blue':
                    new_game.blue_cube.amount += amount
                case 'green':
                    new_game.green_cube.amount += amount
                case 'red':
                    new_game.red_cube.amount += amount
        new_game.print_game()
        if new_game.assert_possibility():
            possible_game_count += 1
            id_sum += new_game.id
    print(possible_game_count)
    print(id_sum)
    
# Main program
if __name__ == "__main__":
    main()