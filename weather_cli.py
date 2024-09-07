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






#print(new_dict.keys())


"""
if list_cities == "--list":
    

for each_cities , temperature in new_dict.items():
    print (each_cities , sum(temperature))

"""     

