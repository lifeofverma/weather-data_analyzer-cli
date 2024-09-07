import json
import sys

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



#average temp

if len(sys.argv) <= 1:
    for each_city , temperature in new_dict.items():
        average_temperature = sum(temperature)
        celsius_temprature = (average_temperature - 32) * 5/9
        print (f"{each_city}{celsius_temprature} celsius")

sys.exit(1)
first_arg = sys.argv[1]
#print(new_dict)



