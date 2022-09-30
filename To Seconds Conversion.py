def To_Secs(hr, min, sec):
    print(hr*(60**2) + min*60 + sec)
    return(hr*(60**2) + min*60 + sec)
hours = int(input("How many hours? ", ))
minutes = int(input("How many minutes? ", ))
seconds = int(input("How many seconds? ",))
To_Secs(hours, minutes, seconds)

print("Test cases:")
assert(To_Secs(2, 30, 10) == 9010)
assert(To_Secs(2, 0, 0) == 7200)
assert(To_Secs(0, 2, 0) == 120)
assert(To_Secs(0, 0, 42) == 42)
assert(To_Secs(0, -10, 10) == -590)