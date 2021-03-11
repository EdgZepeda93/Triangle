#Edgar Zepeda
#00265678
#CIS153

from math import sqrt #imports the square root function from math
print("Input lengths of shorter triangle sides:")  #It tells you to input both your measurements
a = float(input("Enter the first side: ")) #input first side of triangle
b = float(input("Enter the second side: ")) #input second side of triangle
c = sqrt(a**2 + b**2)  #combines both inputs of the triangle and assigns them to the third side
print("The length of the hypotenuse is: ", c ) #prints out your third length
input("Press Enter to escape")
