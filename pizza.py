print("python pizza")
size = input("size of pizza S,M,L")
pepperoni = input("want pepproni or not Y or N")
extra_cheese =input("want extra cheese or not Y or N")

if(size =='S'):
    if(pepperoni=='Y'):
        if(extra_cheese=='Y'):
            print("pay $10")
        else:
            print("pay $8")
    else:
        if(extra_cheese=='Y'):
            print("pay $10")
        else:
            print("pay $5")
        
elif(size=='M'):
    if(pepperoni=='Y'):
        if(extra_cheese=='Y'):
            print("pay $15")
        else:
            
            print("pay $12")
    else:
        if(extra_cheese=='Y'):
            print("pay $13")
        else:
            print("pay $10")
        
elif(size=='L'):
    if(pepperoni=='Y'):
        if(extra_cheese=='Y'):
            print("pay $20")
        else:
            print("pay $18")
    else:
        if(extra_cheese=='Y'):
            print("pay $18")
        else:
            print("pay $15")
        
else:
    print("wrong choice ")