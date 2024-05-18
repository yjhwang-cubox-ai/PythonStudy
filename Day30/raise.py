
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Not Human Height!")

bmi = weight / height ** 2
print(bmi)