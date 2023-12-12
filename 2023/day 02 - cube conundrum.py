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
PART = 'B'
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
        self.cube_dict = {
            'green': self.green_cube.values,
            'blue': self.blue_cube.values,
            'red': self.red_cube.values
            }

        self.green_cube.color = 'green'
        self.blue_cube.color = 'blue'
        self.red_cube.color = 'red'
                        
    def print_game(self):
        print(f"Game {self.id}: {self.assert_possibility()}! {self.green_cube.values} green, {self.blue_cube.values} blue, {self.red_cube.values} red")
    
    def assert_possibility(self):
        if max(self.blue_cube.values) > MAX_BLUE:
            return False
        elif max(self.green_cube.values) > MAX_GREEN:
            return False
        elif max(self.red_cube.values) > MAX_RED:
            return False
        else:
            return True
    
    def cube_power(self):
        return max(self.green_cube.values) * max(self.red_cube.values) * max(self.blue_cube.values)

class Cube:
    def __init__(self) -> None:
        self.color = str
        self.amount = int
        self.values = []
    

# Helper functions


# Main function
def main():
    possible_game_count = 0
    id_sum = 0
    powers = []
    games = [re.split('; ', i.split(':')[1].strip()) for i in data]
    for index, game in enumerate(games):
        new_game = Game()
        new_game.id = index + 1
        for turn in game:
            balls = turn.split(', ')
            for idx, grab in enumerate(balls):
                ball  = grab.split(' ')
                amount = int(ball[0])
                color = ball[1]
                match color:
                    case 'blue':
                        new_game.blue_cube.values.append(amount)
                    case 'green':
                        new_game.green_cube.values.append(amount)
                    case 'red':
                        new_game.red_cube.values.append(amount)
        new_game.print_game()
        powers.append(new_game.cube_power())
        if new_game.assert_possibility():
            possible_game_count += 1
            id_sum += new_game.id

    print(possible_game_count)
    print(id_sum)
    print(powers)
    print(sum(powers))
    
# Main program
if __name__ == "__main__":
    main()