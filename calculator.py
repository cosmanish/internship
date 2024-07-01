a = float(input("Enter your first number:"))
b = float(input("Enter your second number:"))
print("Press 1 for addition \nPress 2 for Subtration \nPress 3 for multiplier \nPress 4 for divission")
Choice = int(input("Enter from 1to4:"))
if Choice == 1 :
    print(a+b)
elif Choice == 2:
    print(a-b)
elif Choice == 3:
    print(a*b)
elif Choice ==4:
    print(a/b)
else:
    print("Invalid")

