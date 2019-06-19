# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
mon, date, year = map(int, input().split())
print(calendar.day_name[calendar.weekday(year, mon, date)].upper()) 
