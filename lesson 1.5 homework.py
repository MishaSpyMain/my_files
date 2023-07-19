def what_day(a,b):
    current_distance = a
    day = 1

    while current_distance < b:
        current_distance *= 1.1
        day += 1

    return day

a = float(input("What is the km for first day?: "))
b = float(input("How many km do you want to reach?: "))

if b <= a:
    print("Error.")
else:
    result_day = what_day(a,b)
    print(result_day)