import json


new_dict = {}

with open("weather.json", 'r') as file:
    json_file_data = json.load(file)

    for data in json_file_data:
        if data["city"] not in new_dict:
            new_dict[data["city"]] = [data["temperature"]]
        else:
            new_dict[data["city"]].append(data["temperature"]) 

    
for each_cities , temperature in new_dict.items():
    print (each_cities , average =  sum(temperature))
            
        



"""
else:
            print("test")
            
    print(new_dict)
"""






