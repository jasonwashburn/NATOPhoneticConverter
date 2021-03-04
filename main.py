import pandas as pd

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')  # Read in CSV using Pandas
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}  # Create a dict of letters and codes

user_word = input("What is the word you want to convert? ")  # Prompt user for word
result = [nato_dict[letter] for letter in user_word.upper()]  # Convert user's word into NATO phonetic alphabet
print(result)