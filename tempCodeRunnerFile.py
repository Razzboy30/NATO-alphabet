 input("Enter Word:")
lett = [n.capitalize() for n in user]
# print(lett)
user_dict = [dict_w[letter] for letter in lett]
print(user_dict)