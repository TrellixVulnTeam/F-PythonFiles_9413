from datetime import datetime, time

dt = datetime.now()  # Fecha y hora actual

print(dt)
print(dt.year)  # año
print(dt.month)  # mes
print(dt.day)  # día

print(dt.hour)  # hora
print(dt.minute)  # minutos
print(dt.second)  # segundos
print(dt.microsecond)  # microsegundos

print("{}:{}:{}".format(dt.hour, dt.minute, dt.second))
print("{}/{}/{}".format(dt.day, dt.month, dt.year))

dt1 = time(10, 30)

print("{}:{}".format(dt1.hour, dt1.minute))


class dateTime():
    def __init__(self, time):
        self.__time = time

    def __str__(self):
        return ("The selected time is {}:{}").format(str(self.__time.hour), str(self.__time.minute))

print(dateTime(time(10,30)))