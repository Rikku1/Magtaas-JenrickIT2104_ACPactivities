from Capybara import Capybara

def testcase():
    choice = input("Enter the test case number: ")
    if choice == "1":
        capyy1 = Capybara('Biscoff','M',5)
        print(f'Test case 1: Name: {capyy1.name}, Gender: {capyy1.gender}, Age: {capyy1.age} years old')
    elif choice == "2":
        capyy2 = Capybara('Jenrick', 'M', 2)
        print(f'Test case 2: Name: {capyy2.name}, Gender: {capyy2.gender}, Age: {capyy2.age} yeras old')
    else:
        print('Invalid testcase')

testcase()