TimeHours = input("What is the current time in hours: ")
TimeWait = input("How long do I wait: ")
#Here is a little bit I added to make sure I could track AM and PM on the clock. Still new so I had it ask for 0 or 1 to determine AM/PM.
AMPM = input ("AM (0) or PM (1): ")
AMPM = int(AMPM)
#This next bit is to check if someone puts in a number bigger than 12. If they do, it reduces it until it is less than 12 and changes the AM/PM variable accordingly.
TimeHours = int(TimeHours)
if TimeHours > 12:
    TimeHours = TimeHours-12
    AMPM = AMPM + 1
TimeHours = str(TimeHours)
#This part just confirms the current time.
if AMPM % 2 == 0:
    print("The current time is: " + TimeHours + "AM")
else:
    print("The current time is: " + TimeHours + "PM")
TimeWait = int(TimeWait)
while TimeWait > 12:
    TimeWait = TimeWait - 12
    AMPM=AMPM + 1
TimeWait = str(TimeWait)
TimeTotal = int(TimeWait) + int(TimeHours)
TimeTotal = str(TimeTotal)
#This last part shows what time it will be.
if AMPM % 2 == 0:
    print ("The time will be: " + TimeTotal + "AM")
else:
    print ("The time will be: " + TimeTotal + "PM")