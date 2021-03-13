import pandas as pd

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')  # Read in CSV using Pandas
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}  # Create a dict of letters and codes


def convert_word():

    user_word = input("What is the word you want to convert? ")  # Prompt user for word
    try:
        result = [nato_dict[letter] for letter in user_word.upper()]
    except KeyError:
        print("Please enter only letters of the alphabet.")  # Let use know to enter letters only and run it again
        convert_word()
    else:
        print(result)


convert_word()
