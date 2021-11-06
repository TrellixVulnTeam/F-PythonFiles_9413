#números prímos
a = input(('Cual es el número que quieres comprobar   '))
a = int(a)
def primo(n):
        resultado = True
        for i in range( n,2,-1 ):
                if (n % i == 0):
                        resultado = False
                        break
        return resultado


print ((primo(a)))
