age=int(input("enter the age"))
height=int(input("enter your height"))
if(height >= 120):
    print("you can ride rollercoaster")
    if(age>18):
        if age >45 and age < 55:
            
            bill =0
        else:
            bill = 12
        
    elif(age>=12):
        bill =7
    else:
        bill =5
else:
    print("you cannot ride")  

photo = input("you want photo").lower()
if photo == "yes":
    if age >45 and age <55:
        print("your ride on us ")
        print("$",bill)
    else:
        bill = bill +3
        print("$",bill)