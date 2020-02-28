def Fibonacci():
    sequence = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if sequence == 0:
        numbers = []
    elif sequence == 1:
        numbers = [1]
    elif sequence == 2:
        numbers = [1,1]
    elif sequence > 2:
        numbers = [1,1]
        while i < (sequence - 1):
            numbers.append(numbers[i] + numbers[i-1])
            i += 1
    return numbers