import json
import sys
import os

formatted_dict = {}  # Initialize an empty dictionary to store city names and their temperatures
average_temperature_dict = {}  # Initialize an empty dictionary to store average temperatures of cities

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
# Use an absolute path to the weather.json file
weather_file_path = os.path.join(current_dir, "weather.json")

#______________________________________________________________________________________________________________________
# Open the 'weather.json' file in read mode
try:
    with open(weather_file_path, 'r') as file: 
        json_file_data = json.load(file)

except FileNotFoundError:
    print("Error: 'weather.json' file not found.")
    sys.exit(1)

except json.JSONDecodeError:
    print("Error: Failed to decode JSON. Please check the file format.")
    sys.exit(1)


for data in json_file_data:
    # Check if the city is not already in the dictionary
    if data["city"] not in formatted_dict:
        #If the city is not in the dictionary, create a new entry with the city name as the key
        # and initialize its value as a list containing the first temperature
        formatted_dict[data["city"]] = [data["temperature"]]
    else:
        # If the city already exists in the dictionary, append the new temperature to the city's list
        formatted_dict[data["city"]].append(data["temperature"]) 


#______________________________________________________________________________________________________________________
# Formatting average temperature and adding the values into the average_temperature dictionary
for each_city , temperature in formatted_dict.items():
    average_temperature = sum(temperature) / len(temperature)
    average_temperature_dict[each_city] = average_temperature

#______________________________________________________________________________________________________________________
#Default Output: Display average temperatures for all cities in Celsius
if len(sys.argv) <= 1:
    print("Average Temperatures:")

    # Open the file in write mode (this will clear the file if it exists)
    with open("Average Temperatures.json", 'w') as new_file:
        json.dump(average_temperature_dict, new_file, indent=4)  # Save as dictionary

    # Iterate through the dictionary containing average temperatures for each city
    for each_city , temperature in average_temperature_dict.items():
        print (f"{each_city}: {temperature}")  # Print the city and its average temperature to the console
        #new_file.write(f"{each_city}: {temperature}\n")  # Write the city and temperature to the file
    sys.exit(1)

#______________________________________________________________________________________________________________________

first_arg = sys.argv[1]

#______________________________________________________________________________________________________________________
#List Cities: to display all available cities in the dataset.
if len(sys.argv) == 2:
    if first_arg == "--list":
        print("Available Cities:")
        for each_cities , temperature in formatted_dict.items():
            print (f"-{each_cities}")
        
        sys.exit(1)

#______________________________________________________________________________________________________________________
#help section writing
if len(sys.argv) == 2:
    if first_arg == "--help":
        print("""
    Weather CLI Tool Usage:

    python weather_cli.py [OPTIONS]

    This CLI tool reads weather data from a JSON file, calculates the average temperature for each city, writes the results to a new JSON file, and prints the average temperatures in the terminal with colored
    output.

    Arguments:
    --help Show this help message and exit.
    --city CITY_NAME Calculate and display the average temperature for the specified city only.
    --convert UNIT Convert temperatures to 'fahrenheit' or 'celsius' (default is Celsius).

    Examples:
    python weather_cli.py
    python weather_cli.py --list
    python weather_cli.py --city New York
    python weather_cli.py --convert fahrenheit
    """)
        sys.exit(1)

#______________________________________________________________________________________________________________________
if len(sys.argv) == 3:
    second_arg = sys.argv[2]
    if first_arg == "--city":
        if second_arg in average_temperature_dict.keys():
            print(f"Average Temperatures:\n{second_arg}: {average_temperature_dict[second_arg]}")
        
            specific_city_data = {second_arg: average_temperature_dict[second_arg]}
            
            # Open the file in write mode (this will clear the file if it exists)
            with open("Average Temperatures.json", 'w') as new_file:
                json.dump(specific_city_data, new_file, indent=4)  # Save as dictionary    
            sys.exit(1)

        # Handle edge cases where user input does not match any of the valid choices Print a message indicating that the input is invalid or not recognized
        else:
            print("Input city is not available.\nPlease refer to the command <--list> to check available cities")
            sys.exit(1)

#______________________________________________________________________________________________________________________
if len(sys.argv) == 3:
    second_arg = sys.argv[2]
    if first_arg == "--convert" and second_arg == "fahrenheit":
        print("Average Temperatures:")
        fahrenheit_temperatures = {}  # Dictionary to store temperatures in Fahrenheit

        for each_city , temperature in average_temperature_dict.items():
            fahrenheit_temperature = (temperature * 1.8) + 32
            formatted_fahrenheit_temperature = "{:.1f}".format(fahrenheit_temperature)
            print (f"{each_city}: {formatted_fahrenheit_temperature}")

            # Save the Fahrenheit temperature in the new dictionary
            fahrenheit_temperatures[each_city] = fahrenheit_temperature

        # Open the file in write mode (this will clear the file if it exists)
        with open("Average Temperatures.json", 'w') as new_file:
            json.dump(fahrenheit_temperatures, new_file, indent=4)  # Save as dictionary
        sys.exit(1)



#______________________________________________________________________________________________________________________
if len(sys.argv) > 2 :
    print("input is invalid or not recognized\nUse the --help command to see how to use this tool.")
    sys.exit(1)


#____________________________________________________________________________________________________________________
# Handle edge cases where user input does not match any of the valid choices Print a message indicating that the input is invalid or not recognized
else:
    print("input is invalid or not recognized\nUse the --help command to see how to use this tool.")
    sys.exit(1)