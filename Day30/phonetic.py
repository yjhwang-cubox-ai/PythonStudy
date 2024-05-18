import pandas as pd

df = pd.read_csv("Day26/nato_phonetic_alphabet.csv")
nato_list = {info[1].letter:info[1].code for info in df.iterrows()}

def generate_phonetic():
    word = input("Enter a Word: \n")
    try:
        output = [nato_list[text.upper()] for text in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)

generate_phonetic()