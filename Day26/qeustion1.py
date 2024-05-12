sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

dictionary = {word:len(word) for word in sentence.split()}

print(dictionary)

example = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
temp = [example.items()]
print(example.items())
temp_f = {day:(celcious * 9/5) + 32 for (day,celcious) in example.items()}

print(temp_f)