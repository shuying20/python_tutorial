import statistics, math

def my_add (input):
    sum = 0
    for x in input:
        sum += int(x)
    return sum

input = [10,20,30]

#2. process
answer = my_add(input)

#3. output
print(f'Answer: {answer}')

#MULTIPLY
def my_multiply (input):
    sum = 1
    for x in input:
        sum *= int(x)
    return sum

input = [20,23,18]
answer = my_multiply(input)
print(f'Answer: {answer}')

#STAND DEV
def my_sd (input):
    print(f'Input : {input}')
    lenght = len(input)
    sum = 0
    mean = statistics.mean(input)
    print(f'Mean : {mean}')
    for x in input:
        sum += (int(x)-mean)**2
    sum = sum / lenght
    output = math.sqrt(sum)
    return output

input = [20,23,18]
answer = my_sd (input)
answer = round(answer, 2)
print(f'Answer: {answer}')

