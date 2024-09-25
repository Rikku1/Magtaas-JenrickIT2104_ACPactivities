def discount(amount):
    if amount < 5000:
        discount_ = amount * (5 / 100)
    else:
        discount_ = amount * (10 / 100)
    return discount_

try_again = "yes"
while try_again =="yes":
    amount = int(input("Enter the total purchase amount: "))
    final_price = amount - discount(amount)
    print(f"Initial purchase amount: {amount: .2f}")
    print(f"Discount: {discount(amount): .2f}")
    print(f"Final price: {final_price: .2f}")
    try_again = input("Do you want to try again? (yes/no): ")
print("Thank you!")