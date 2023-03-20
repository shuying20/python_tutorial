# 1. Input
x1= input("enter x1: ")
x2= input("enter x2: ")
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
    sum= (int(x1) + int(x2))/2
elif op == "sd":
    sum= (int(x1) + int(x2))/2

#HW
# CALC MEAN
1. tmp1 = mean - x1
2. tmp2 = mean - x2
3. (tmp1+tmp2)**2
4.#3/m
5. sqrt (#4)

#3. output
print (f"sum: {sum}")