#List of the vowels in the string
string_ = input("Enter a string: ")
vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowels = []
for pick in string_:
    if pick in vowels_list:
        vowels += pick
print(vowels)