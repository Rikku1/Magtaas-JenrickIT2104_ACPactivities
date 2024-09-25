number = int(input("Enter an integer: "))
n_str = str(number)
pal_ = n_str[::-1] 

if pal_ == n_str:
    print("Palindrome")
else:
    print("Not a Palindrome")