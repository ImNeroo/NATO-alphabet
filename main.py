import pandas

phonetic_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row.letter: row.code for (index, row) in phonetic_dataframe.iterrows()}
print(alphabet)
#error = True Yo lo hice con un bucle while pero tambien se puede hacer con una funcion
#while error:
def generate_phonetic():
    user_word = input("Enter a word: ").upper()

    try:
        output = [alphabet[letter] for letter in user_word]
    except KeyError:
        print("Sorry only letters in the Alphabet please.")
        generate_phonetic()
    else:
        print(output)
        error = False

generate_phonetic()

