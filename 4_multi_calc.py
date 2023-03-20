# 1. Input
x1= input("enter x1: ")
x2= input("enter x2: ")
x3= input("enter x3: ")
op = input("enter operator: ")

#2. Process
if op == "+":
    sum= int(x1) + int(x2)
if op == "-":
    sum= int(x1) - int(x2)
if op == "*":
    sum= int(x1) * int(x2)
if op == "/":
    sum= int(x1) / int(x2)
elif op == "avg":
    sum= (int(x1) + int(x2) + int(x3))/2


#HW
# CALC MEAN x1=5, x2=10, x3=11
1. tmp1 = mean - x1
2. tmp2 = mean - x2
3. tmp3 = mean - x3
4. (tmp1+tmp2)**2
5.#3/m
6. sqrt (#4)
import math
elif op == "sd":
    sd= (int(avg-x1)) + int(avg-x2) + int(avg-x3)**2)

#3. output
print (f"sum: {sum}")