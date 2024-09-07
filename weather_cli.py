import json
import sys


first_arg = sys.argv[1]



new_dict = {}

with open("weather.json", 'r') as file:
    json_file_data = json.load(file)

    for data in json_file_data:
        if data["city"] not in new_dict:
            new_dict[data["city"]] = [data["temperature"]]
        else:
            new_dict[data["city"]].append(data["temperature"]) 




if first_arg == "--list":
    for each_cities , temperature in new_dict.items():
        print (each_cities)

elif first_arg == "--help":
    print("Weather Analysis Tool - Help Section\n")
    print("This tool reads weather data from a JSON file, calculates average temperatures for each city, and provides various functionalities for analyzing and displaying the data.")
    print("Below is an overview of the available commands and features:\n")
    print("Default Output: Display average temperatures for all cities in Celsius.") 
    print("Filter by City: Use the --city CITY_NAME argument to display the average temperature for a specific city.")
    print("Convert Temperatures: Use the --convert fahrenheit argument to display temperatures in Fahrenheit.")
    print("List Cities: Use the --list argument to display all available cities in the dataset.")
    print("Help: Use the --help argument to display information about how to use the CLI tool.")

else:
    print("use -- help command and this will show you how to use this tool.")
