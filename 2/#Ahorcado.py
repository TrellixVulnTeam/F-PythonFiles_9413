#ahorcado

import random

a = ['hola', 'que', 'tal']

def palabraAleatoria(a):

        b = random.randrange(len(a))

        palabra = a[b]
                
        return palabra

def letra():
        
        
        b = input('Introduzca la letra deseada\t')

        while not (b >= 'a' and not b <= 'Z' and len(letra) == 1):

                b = False
                
        if b == True: 
                
                return b

def comprobarLetra(palabra, letra):
        return letra in palabra


        
palabra = palabraAleatoria(a)

letra = letra()

if coprobarLetra == True:
        print (comprobarLetra)
