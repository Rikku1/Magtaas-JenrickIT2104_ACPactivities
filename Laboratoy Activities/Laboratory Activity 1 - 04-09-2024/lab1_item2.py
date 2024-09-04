chr_1, chr_2 = input("Enter two-seperated characters: ").split()

print(f"--------------------------------")
print(f"Character with the greater value is: {max(chr_1, chr_2)}")
print(f"--------------------------------")

print(f"Showing ACII Values: ")
asciiVal1 = ord(chr_1)
asciiVal2 = ord(chr_2)
print(f"{chr_1} : {asciiVal1} ")
print(f"{chr_2} : {asciiVal2}")