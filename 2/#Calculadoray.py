#calculadora con funciones

respuesta = 0 

def sumar(op1,op2):
        respuesta = op1 + op2
        return respuesta

def restar(op1,op2):
        respuesta = op1 - op2
        return respuesta

def multiplicar(op1,op2):
        respuesta = op1 * op2
        return respuesta

def dividir(op1,op2):
        respuesta = op1 / op2
        return respuesta


print("\n\nElige una de estas opciones: \n")
print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicación")
print("4 - División")
print("5 - Salir")

a = 0

while a != 5:

        a = input('¿Que desea hacer?')

        op1 = (int)(input('¿Cual es el primer número con el que desea operar?\t'))

        op2 = (int)(input('¿Cual es el primer número con el que desea operar?\t'))
        
        if a == 1:
                respuesta = sumar(op1, op2)
        elif a == 2:
                respuesta = restar(op2, op2)
        elif a == 3:
                respuesta = multiplicar(op2, op2)
        elif a == 4:
                respuesta = dividir(op2, op2)
        elif a == 5:
                exit

        print (respuesta) 
        

        
