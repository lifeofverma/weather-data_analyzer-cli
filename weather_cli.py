import json

with open("weather.json", 'r') as file:
    file_data = json.load(file)

    new_dict = {}

    for entries in file_data:
        for key , value in entries.items():
            print(type(x))





"""
    for cities in data:
        total_cities.append(cities["city"])
  
    for i in data:
        if i["city"] in total_cities:
            print(i)

        if i in new_dict:
        new_dict[i] += 1
    else:
        new_dict[i] = 1
    print(list(y))
    celsius = (Los_Angeles - 32) * 5/9
    print (celsius)
    y = set(x)
            for b in data:
            if b["city"] in a:
    print(list(y))

            x.append(i["city"])

        y = set(x)
        a = list(y)

        print(city , temp )
"""

