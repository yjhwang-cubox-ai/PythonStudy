with open('Day26/file1.txt', "r", encoding="utf8") as file:
    file1 = file.readlines()
with open('Day26/file2.txt', "r", encoding="utf8") as file:
    file2 = file.readlines()
    
sorted_file1 = [int(num) for num in file1 if num in file2]

print(sorted_file1)