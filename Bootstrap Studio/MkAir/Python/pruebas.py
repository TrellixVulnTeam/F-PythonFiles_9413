import string
from random import randint, choice


def rdmGate():

    return str(choice(string.ascii_uppercase)) + str(randint(10, 99))

print(rdmGate())