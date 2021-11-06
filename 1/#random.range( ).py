'''#random.randrange( )

import random
c = []
d = 0 
a = int(input('Cual es la longitúd de la contraseña que quiere crear?\t'))

al_azar = random.randrange(0, 9)
if len(c[0]) < a:
      c[0].append(al_azar)

print(c)
'''

#random.randrange( )

import random
#import string

LenPassword = int(input('Cual es la longitúd de la contraseña que quiere crear?\t'))
PasswordUpperLimit = pow(10, LenPassword)-1
Password = random.randrange(0, PasswordUpperLimit)
PasswordStr = str(Password).zfill(LenPassword) #pone '0' a la izquierda en caso de que sea ese el número al azar

print(PasswordStr)
