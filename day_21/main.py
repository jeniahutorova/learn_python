# import csv
# with open("day_21\weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     next(data)
#     for row in data:
#       print(row)
#       temperatures.append(int(row[1]))
#     print(temperatures)

import pandas 

# data = pandas.read_csv("day_21\weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# temp_average = sum(temp_list)/ len(temp_list)
# print(temp_average)

# We're finding an average number
# print(data["temp"].mean())

# Looking for max number in the column
# print(data["temp"].max())

# Print a row with max temperature
# print(data[data.temp == data.temp.max()])

# Get a monday temperature in Fahrenhight
# monday = data[data.day == "Monday"]
# monday_temp_f = monday.temp * (9/5) + 32
# print(monday_temp_f)


# data_dict = {
#     "students": ["Ammy", "Nicol", "James"],
#     "scores" : [100, 95, 70]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# Count how many squirrels with each fur color
squirrel_data = pandas.read_csv(r"C:\Users\jenia\Desktop\learn_python\day_21\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240926.csv")
main_colors = squirrel_data["Primary Fur Color"].value_counts()

df = pandas.DataFrame(main_colors)
df.to_csv("squirrel_count.csv")