
#month_winter = ('dec', 'jan', 'feb')
#month_spring = ('mar', 'apr', 'may')
#month_summer = ('jun', 'jul', 'aug')
#month_fall = ('sep', 'oct', 'nov')


def what_season_list(month):
    seasons = ['Winter', 'Spring', 'Summer', 'Fall'] #explains what seasons is
    if 1 <= month <= 2 or month == 12:
        return seasons[0] #that's winter
    elif 3 <= month <=5:
        return seasons[1] #that's spring
    elif 6 <= month <=8:
        return seasons[2] #thats summer
    elif 9 <=month <= 11:
        return seasons[3] #thats fall
    else:
        return"Wrong month number, please provide number 1=12." #if number is not 1-12 or isnt a number at all

month = int(input("What is the month number?: "))
season = what_season_list(month)
print(f"Month {month} is in the {season} season.")
