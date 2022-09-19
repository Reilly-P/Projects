# Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday. Write a function which is given the day number, and it returns the day name (a string).
week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
Day = input('Give a number from 0-6, each number corresponds to a weekday, starting with Sunday and ending with Saturday ')
Day = int(Day)
for x in range (7):
    if Day == x-1:
        print(week[Day]) 