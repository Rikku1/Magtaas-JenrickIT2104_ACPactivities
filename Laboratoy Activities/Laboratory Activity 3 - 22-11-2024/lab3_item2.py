try:
    number = int(input("Enter a number: "))
    
    if number <= 1:
        print(f"{number} is not a perfect number.")
    else:
        sum_of_divisors = 0
        for i in range(1, number):
            if number % i == 0:
                sum_of_divisors += i

        if sum_of_divisors == number:
            print(f"{number} is a perfect number.")
        else:
            print(f"{number} is not a perfect number.")
except ValueError:
    print("Please enter a valid integer.")