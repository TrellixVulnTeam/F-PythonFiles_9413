from Heritage.Car import Car
import pickle

def loadall(filename):
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break

c1 = Car("Mazda","CX5",5)
c2 = Car("BMW","M3",4)
c3 = Car("Peugeot","307",3)

coches = [c1,c2,c3]

file = open("cars","wb")

items = loadall(file)

for i in items:
    print(i)
