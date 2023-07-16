# profit or loss??? let's find out :)



income = float(input("How much did you make?: "))
rent = float(input("How much was rent?: "))
expenses = float(input("How much expenses?: "))
workers = float(input("How many people worked?: "))

loss = (rent + expenses)
outcome = income - loss

if outcome > 0:
    print(f"Good job! The company made ${outcome} dollars!")
    salary = outcome / workers
    print(f"Each person made ${salary} dollars!")
else:
    print("You are broke!")
