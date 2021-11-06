#mostrar número de consonantes en un array.py
b = 0

a = str(input('Introduzca una frase:\t'))

for i in range (0,len(a)):
      if a[i] == 'a':
            b = b + 1
      elif a[i] == 'e':
            b = b + 1
      elif a[i] == 'i':
            b = b + 1
      elif a[i] == 'o':
            b = b + 1
      elif a[i] == 'u':
            b = b + 1
            
print(int(len(a))-int(b))
