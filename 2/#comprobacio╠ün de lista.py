#comrobación de una lista

c = []

b = 0

while b != '+' :
        b = int(b)
        
        c.append(b)
        
        b = (input('Introduzca un número\t'))

a = c[1:]

def comprobar (a):
        for i in range(0,len(a)):
                hayDos = False
                hayCuatro = False
                if a[i] == 2:
                        hayDos = True
                elif a[i] == 4:
                        hayCuatro = True

        print(hayDos)
        print(hayCuatro)
        if hayDos and hayCuatro:
                return False
        elif hayDos or hayCuatro:
                return True
        else:
                return False


print(a)

print(comprobar(a))
