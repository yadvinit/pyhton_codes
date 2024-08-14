print("the tip calculator")
bill = float(input("the amount of bill\n"))
tip = float(input("the amount of tip you want to give\n"))
cost = bill + tip
member = float(input("the total members are\n"))
per_cost= cost/member
print("Each person should pay",round((bill + tip)/member))

# print(type(True))
# print("enter number of letters in your name" + int(input("enter your name")))