import json
import sys

new_dict = {}  # Initialize an empty dictionary to store city names and their temperatures


#______________________________________________________________________________________________________________________
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


#______________________________________________________________________________________________________________________
#Default Output: Display average temperatures for all cities in Celsius
if len(sys.argv) <= 1:
    print("Average Temperatures:")
    for each_city , temperature in new_dict.items():
        average_temperature = sum(temperature)
        celsius_temprature = (average_temperature - 32) * 5/9
        formatted_celsius_temprature = "{:.1f}".format(celsius_temprature)
        print (f"{each_city}: {formatted_celsius_temprature}")
    sys.exit(1)


#______________________________________________________________________________________________________________________
first_arg = sys.argv[1]



#______________________________________________________________________________________________________________________
#List Cities: to display all available cities in the dataset.
if first_arg == "--list":
    print("Available Cities:")
    for each_cities , temperature in new_dict.items():
        print (f"-{each_cities}")
    sys.exit(1)


#______________________________________________________________________________________________________________________
#help section writing
elif first_arg == "--help":
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
# Handle edge cases where user input does not match any of the valid choices Print a message indicating that the input is invalid or not recognized
else:
    print("input is invalid or not recognized\nUse the --help command to see how to use this tool.")
    sys.exit(1)


