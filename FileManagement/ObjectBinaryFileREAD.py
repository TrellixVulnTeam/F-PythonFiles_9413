import pickle

file = open("cars","rb")

carArray = pickle.load(file)

file.close()

for i in carArray:
    print(i)

