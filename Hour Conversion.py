TimeHours = input("What is the current time in hours: ")
TimeWait = input("How long do I wait: ")
AM = 0
PM = 1
AMPM = input ("AM(0) or PM(1): ")
AMPM = int(AMPM)
TimeHours = int(TimeHours)
if TimeHours > 12:
    TimeHours = TimeHours-12
    AMPM = AMPM + 1
TimeHours = str(TimeHours)
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
if AMPM % 2 == 0:
    print ("The time will be: " + TimeTotal + "AM")
else:
    print ("The time will be: " + TimeTotal + "PM")