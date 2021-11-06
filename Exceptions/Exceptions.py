
def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):
    # TRYCATCH DE DIVISIÓN POR CERO
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Los números divididos entre cero son infinito"


# TRYCATCH DEL PRIMER NÚMERO
try:
    op1 = (int(input("Introduce el primer número: ")))
except:
    ValueErrorBoolean = True
    while ValueErrorBoolean:
        try:
            op1 = (int(input("Introduce el primer número: ")))
            ValueErrorBoolean = False
        except:
            pass
# TRYCATCH DEL SEGUNDO NÚMERO
try:
    op2 = (int(input("Introduce el segundo número: ")))
except:
    ValueErrorBoolean = True
    while ValueErrorBoolean:
        try:
            op2 = (int(input("Introduce el segundo número: ")))
            ValueErrorBoolean = False
        except:
            pass

operacion = input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa ")

