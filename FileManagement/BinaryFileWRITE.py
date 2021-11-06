import pickle
from MkAir.Person import Person

p1 = Person("Oier","Mentxaka")
p2 = Person("Iker","Gomez")
p3 = Person("Joseba","Martinez")
p4 = Person("Kerman","Rodriguez")

data = [p1,p2,p3,p4]

binaryFile = open("binaryFile","wb")

pickle.dump(data,binaryFile)

binaryFile.close()
del binaryFile

for i in data:
    print(i)