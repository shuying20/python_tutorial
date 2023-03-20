# 1. Input
sum=0
#loop HAVE to put indentation to show its a part of the loop
while True:
    #loop while "true"=continous, if specific do while "..."
    x1= input("enter x1: ")
    x2= input("enter x2: ")
    op = input("enter operator: ")

    #2. Process
    if op == "+":
        sum= int(x1) + int(x2)
    if op == "-":
        sum= int(x1) - int(x2)

    #3. output
    print (f"sum: {sum}")
    res = input("Continue? (Y/N) ")
    if res.upper()[0] == "N":
        break;