from datetime import date, datetime
year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
x = date(year, month, day)
print(x)
def week(x):
    week_number = date.isocalendar(x).week
    print("Current Week No Is ", week_number)
week(x)