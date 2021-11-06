import math


def  squareRoot(num):
    if num <0:
        return ("It is not possible to do a negative numbers square root")
    else:
        return math.sqrt(num)

answer1 = squareRoot(4)
answer2 = squareRoot(-4)


print(answer1)
print(answer2)