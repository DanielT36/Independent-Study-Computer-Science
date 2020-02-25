def Character_Input():
    name = raw_input("What is your name? ")
    age = input("what is your age? ")
    age = int(age)
    year = input("Enter the current year: ")
    year = int(year)
    future = str(((year - age) + 100))
    print(name + " will be 100 years old in the year " + future +".")
Character_Input()