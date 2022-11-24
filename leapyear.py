
import datetime
today=datetime.date.today()
currentyear=today.year
print(currentyear)
print("enter last year")
endYear=int(input())
print("List of leap years:");
for year in range(currentyear ,endYear):
        if (0 == year % 4 )and(0 != year % 100) or (0 == year % 400):
         print(year)
