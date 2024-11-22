def roman_to_integer(roman):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    integer_value = 0
    length = len(roman)

    for i in range(length):
        current_value = roman_values[roman[i]]
        if i < length - 1 and current_value < roman_values[roman[i + 1]]:
            integer_value -= current_value
        else:
            integer_value += current_value
    return integer_value

roman = input("Enter a Roman Numeral: ").strip().upper()
integer_value = roman_to_integer(roman)
print(f"The integer value of '{roman}' is: {integer_value}")
