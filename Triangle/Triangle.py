#Reilly Prescott
#This is a program to find the area and perimeter of a triangle given three sides as well as to determine if it is actually a triangle

import math
side1 = float(input("What is the length of the first side? "))      #Asking the user for the sides
side2 = float(input("What is the length of the second side? "))
side3 = float(input("What is the length of the first side? "))
perimeter = side1 + side2 + side3
#converting sides to variables for easy use in Heron's formula 
a = float(side1)
b = float(side2)
c = float(side3)
p = float(perimeter/2)
print("The perimeter of the triangle is: ", perimeter) #display the perimeter
# Heron's formula
area = p*(p-a)*(p-b)*(p-c)
if area > 0: #Check the area to make sure it is a real number and we won't get an error when running
    print("The area of the triangle is: ", math.sqrt(area)) #printing the actual area of the triangle once we've established that it is, in fact, a triangle.
    if a + b > c and a + c > b and b + c > a: #checking the requirements for a real triangle again
        print("This is a real triangle! :D")
else:
    print("This is not a real triangle :(") #showing if it is not a real triangle