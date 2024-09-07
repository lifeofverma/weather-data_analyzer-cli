import json
import sys


first_arg = sys.argv[1]


new_dict = {}  # Initialize an empty dictionary to store city names and their temperatures

# Open the 'weather.json' file in read mode
with open("weather.json", 'r') as file: 
    json_file_data = json.load(file)

    for data in json_file_data:
        # Check if the city is not already in the dictionary
        if data["city"] not in new_dict:
            #If the city is not in the dictionary, create a new entry with the city name as the key
            # and initialize its value as a list containing the first temperature
            new_dict[data["city"]] = [data["temperature"]]
        else:
            # If the city already exists in the dictionary, append the new temperature to the city's list
            new_dict[data["city"]].append(data["temperature"]) 


#list of all cities avaialble 

if first_arg == "--list":
    for each_cities , temperature in new_dict.items():
        print (each_cities)

#help section writing
elif first_arg == "--help":
    print("""
Weather Analysis Tool - Help Section

This CLI tool reads weather data from a JSON file, calculates average temperatures for each city, and provides various functionalities for analyzing and displaying the data.

Usage:
    weather_tool [OPTIONS]

Options:
    --city CITY_NAME           Display the average temperature for the specified city.
                               Example: --city "New York"
    
    --convert fahrenheit       Convert temperatures from Celsius to Fahrenheit for all displayed cities.
                               Example: --convert fahrenheit
    
    --list                     List all available cities in the dataset.
    
    --help                     Show this help message and exit.
    
Default Behavior:
    If no options are specified, the tool will display the average temperatures for all cities in Celsius.
    
Additional Information:
    The tool automatically calculates average temperatures if multiple entries exist for the same city. 
    Temperature conversion applies globally to all cities when specified.
    
For more detailed documentation, visit the user guide or contact support.
""")

# Handle edge cases where user input does not match any of the valid choices Print a message indicating that the input is invalid or not recognized
else:
    print("input is invalid or not recognized\nuse -- help command and this will show you how to use this tool.")
