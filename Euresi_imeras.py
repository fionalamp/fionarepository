from datetime import date, datetime
countDays = 0
currentyear = date.today().year
futureyear = date.today().year + 10
print(datetime(2018, 2, date.today().day))
for year in range(currentyear, futureyear):
    for month in range (1,13):
        if datetime(year, month, date.today().day).weekday() == True  :
            countDays += 1
print(countDays)

