# Imports
import re

# Path variables
YEAR = 2023
DAY = "05"
PUZZLE_TITLE = "seedtofertilizer"
INPUT_PATH = f"./{YEAR}/inputs/day {DAY} - {PUZZLE_TITLE}.txt"


# Read Puzzle input
with open(INPUT_PATH, 'r') as file:
    data = [i.strip() for i in file.readlines()]
    # print(data)

# Variables
NUMBER_REGEX = r'\d+'
seed_dict = {}

# Class
class Almanac:
    def __init__(self) -> None:
        self.seed_dict = dict()
        self.seed_to_soil_map = dict()
        self.soil_to_fertilizer_map = dict()
        self.fertilizer_to_water_map = dict()
        self.water_to_light_map = dict()
        self.light_to_temperature_map = dict()
        self.temperature_to_humidity_map = dict()
        self.humidity_to_location_map = dict()

class Seed:
    def __init__(self) -> None:
        self.number = int
        self.soil = int
        self.fertilizer = int
        self.water = int
        self.light = int
        self.temperature = int
        self.humidity = int
        self.location = int

# Helper functions
def map_numbers(number_list: list):
    number_dict = {}
    for idx, line in enumerate(number_list):
        mapping_definition = [eval(i) for i in re.findall(NUMBER_REGEX, line)]
        destination_start = mapping_definition[0]
        source_start = mapping_definition[1]
        mapping_range = mapping_definition[2]
        number_dict[(source_start, source_start+mapping_range)] = (destination_start, destination_start+mapping_range)
    return number_dict

def assign_destination_to_seed(almanac_map: dict, current_locator: int):
    destination = current_locator
    for source_range, destination_range in almanac_map.items():
        if current_locator in range(*source_range):
            offset = current_locator - source_range[0]
            destination = destination_range[0] + offset
    return destination

# Main function
def main():
    # Create the Almanac mappings
    almanac = Almanac()
    seed_to_soil = map_numbers(data[3:18])
    soil_to_fertilizer = map_numbers(data[20:33])
    fertilizer_to_water = map_numbers(data[35:66])
    water_to_light = map_numbers(data[68:90])
    light_to_temperature = map_numbers(data[92:125])
    temperature_to_humidity = map_numbers(data[127:171])
    humidity_to_location = map_numbers(data[173:])
    almanac.seed_to_soil_map = seed_to_soil
    almanac.soil_to_fertilizer_map = soil_to_fertilizer
    almanac.fertilizer_to_water_map = fertilizer_to_water
    almanac.water_to_light_map = water_to_light
    almanac.light_to_temperature_map = light_to_temperature
    almanac.temperature_to_humidity_map = temperature_to_humidity
    almanac.humidity_to_location_map = humidity_to_location
    
    seed_numbers = [eval(i) for i in re.findall(NUMBER_REGEX, data[0])]
    for number in seed_numbers:
        seed = Seed()
        seed.number = number
        seed_dict[f"Seed {number}"] = seed
        seed.soil = assign_destination_to_seed(almanac.seed_to_soil_map, seed.number)
        seed.fertilizer = assign_destination_to_seed(almanac.soil_to_fertilizer_map, seed.soil)
        seed.water = assign_destination_to_seed(almanac.fertilizer_to_water_map, seed.fertilizer)
        seed.light = assign_destination_to_seed(almanac.water_to_light_map, seed.water)
        seed.temperature = assign_destination_to_seed(almanac.light_to_temperature_map, seed.light)
        seed.humidity = assign_destination_to_seed(almanac.temperature_to_humidity_map, seed.temperature)
        seed.location = assign_destination_to_seed(almanac.humidity_to_location_map, seed.humidity)
                
                
    almanac.seed_dict = seed_dict
    print(seed_numbers)
    seed_locations = [i.location for i in almanac.seed_dict.values()]
    print(seed_locations)
    print(f"The lowest seed location for the initial batch of seeds is: {min(seed_locations)}")

# Main program
if __name__ == "__main__":
    main()