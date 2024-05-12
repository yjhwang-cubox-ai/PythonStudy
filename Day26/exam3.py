import pandas as pd

data = {
    "name": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

student_data_frame = pd.DataFrame(data)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row)