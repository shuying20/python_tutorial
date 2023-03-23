import math
# 1. Input
x1= input("enter x1: ")
x2= input("enter x2: ")
x3= input("enter x3: ")

#HW
# CALC MEAN x1=5, x2=10, x3=11
while True:
    mean= (int(x1) + int(x2) + int(x3))/3
    a = int(x1)-mean
    b = int(x2)-mean
    c = int(x3)-mean
    sq= (int(a)**2)+(int(b)**2)+(int(c)**2)
    d= int(sq)/3
    sum= math.sqrt(d)
#3. output
    print (f"sum: {sum}")
    res = input("Continue? (Y/N) ")
    if res.upper()[0] == "N":
        break;