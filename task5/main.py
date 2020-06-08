from datetime import datetime
# today = "Feb 1 2019"
# new_day = datetime.strptime(today , '%b  %d  %Y')
def compaire(first,second):
    first_date = datetime.strptime(first, '%b  %d  %Y')
    second_date= datetime.strptime(second, '%b  %d  %Y')

    if first_date.year==second_date.year and first_date.month==second_date.month and first_date.day==second_date.day:
        return 'Today'
    s = second_date - first_date
    return f'{s.days} days ago' 
    
   
    


print(compaire('Feb 1 2019','Feb 2 2019'))