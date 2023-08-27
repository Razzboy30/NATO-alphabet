import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_w = {row.letter:row.code for (index,row) in df.iterrows()}

def main():
    pp = True
    while pp:
        try:
            user = input("Enter Word:")
            lett = [n.capitalize() for n in user]
            # print(lett)
            user_dict = [dict_w[letter] for letter in lett]
            print(user_dict)
            pp = False
        except KeyError:
            print("Please enter a alphabet")
            

main()
