import csv

with open("Day25/weather_data.csv") as file:
    content = csv.reader(file)
    temperature = []
    for row in content:
        if row[1] == "temp":
            continue
        temperature.append(int(row[1]))

print(temperature)