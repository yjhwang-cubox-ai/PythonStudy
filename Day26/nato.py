import pandas as pd

df = pd.read_csv("Day26/nato_phonetic_alphabet.csv")
phonentic_dict = {row.letter:row.code for (index, row) in df.iterrows()}

word = input("Enter a word: \n")
output = [phonentic_dict[text.upper()] for text in word]
print(output)