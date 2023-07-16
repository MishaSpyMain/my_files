# asking user for 2 numbers then dividing them.

def dividing_numbers():
    x = input("What is your first number?: ")  # requesting first number
    y = input("What is your second number?: ")  # requesting second number

    if y != "0":
        result = float(x) / float(y)
        print("Answer is:", result)
    else:
        print("Can't use zeros sorry :( ")

dividing_numbers()



