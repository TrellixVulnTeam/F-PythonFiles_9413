class Car():
    def __str__(self):
        return "I'm a car and I have 4 weels"

class Bike():
    def __str__(self):
        return "I'm a bike and I have 3 weels"

class Tram():
    def __str__(self):
        return "I'm a tram and I don't have weels"

print(Car().__str__())
print(Bike().__str__())
print(Tram().__str__())