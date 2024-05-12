import pandas as pd

df = pd.read_csv("Day26/nato_phonetic_alphabet.csv")
nato_list = {row.letter:row.code for (index, row) in df.iterrows()}

word = input("Enter a word: \n")
output = [nato_list[text.upper()] for text in word]
print(output)