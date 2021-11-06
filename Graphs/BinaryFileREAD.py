import pickle
from MkAir.Person import Person

binaryFile = open("binaryFile","rb")

data = pickle.load(binaryFile)

for i in data:
    print(i)