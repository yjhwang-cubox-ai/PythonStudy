import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

scores = {name:random.randint(1,100) for name in names}

passed_students = {name: score for (name, score) in scores.items() if score > 80}

print(scores)
print(passed_students)