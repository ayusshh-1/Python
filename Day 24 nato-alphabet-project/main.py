import pandas
user = input("Enter Your Name: ").upper()
with open("nato_phonetic_alphabet.csv") as file:
    data = pandas.read_csv(file)

dict = {row.letter:row.code for (index,row) in data.iterrows()}
#now we want list of that
list = [dict[letter]  for letter in user]
print(list)