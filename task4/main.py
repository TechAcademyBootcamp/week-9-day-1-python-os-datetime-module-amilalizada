import datetime
from datetime import date
def addYears(d, years):
    try:
     
        return d.replace(year = d.year + years)
    except ValueError:
      
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

print(addYears(datetime.date(2015,1,1), -1))
print(addYears(datetime.date(2015,1,1), 0))
print(addYears(datetime.date(2015,1,1), 2))
print(addYears(datetime.date(2000,2,29),1))