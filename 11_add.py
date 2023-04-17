def my_add (input):
    sum = 0
    for x in input:
        sum += int(x)
    return sum

# 1. input
input = [10,20,30]

#2. process
answer = my_add(input)

#3. output
print(f'Answer: {answer}')