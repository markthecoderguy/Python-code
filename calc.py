#if 5,6,7 used it will work with the first number and wont ask for a second
#made by markthecoderguy on github
import math
num1 = int(input("number:\n  "))
option = int(input("operation:\n1 for +\n2 for -\n3 for *\n4 for /\n5 for ²(square) \n6 for √(square root)\n7 for circumference of a circle(will work with diameter if chosen)\n    "))
if option == 5:
    print( float(num1 * num1) )
elif option == 6:
    print(math.sqrt(num1))
elif option == 7:
    print (float(num1) * (3.141592653589793238462643))

else:
    num2 = int(input("number:\n  "))

    if option == 1:
        print(num1 + num2)
    
    elif option == 2:
        print (float(num1 - num2))

    elif option == 3:
        print (float(num1 * num2))

    elif option == 4:
        print (float(num1 / num2))
    
    else:
        print("error")


    
