#calculadora

def factorial(n):
      if (n == 0):
            1
      else:
            n * factorial(n - 1)

x = ''
print("·····Calculadora·····")
while x != 'no':
      print("\n\nElige una de estas opciones: ")
      print("1 - Suma")
      print("2 - Resta")
      print("3 - Multiplicación")
      print("4 - División")
      print("5 - Factorial")
      x = input("\t")
      x = float(x)

      if(x==1):
            a = float(input("Introduce el primer número:\t"))
            b = float(input("Introduce el segundo número:\t"))
            resultado = a+b
            print("El resultado de la suma es: \t"+ str(resultado))
      elif(x==2):
            a = float(input("Introduce el primer número:\t"))
            b = float(input("Introduce el segundo número:\t"))
            resultado= a-b
            print("El resultado de la resta es: \t"+ str(resultado))
      elif(x==3):
            a = float(input("Introduce el primer número:\t"))
            b = float(input("Introduce el segundo número:\t"))
            resultado= a*b
            print("El resultado de la multiplicación es: \t"+ str(resultado))
      elif(x==4):
            a = float(input("Introduce el primer número:\t"))
            b = float(input("Introduce el segundo número:\t"))
            resultado= a/b
            print("El resultado de la división es: \t"+ str(resultado))
      elif(x==5):
            c= ''
            n = int(input('Introduce el número del que quiera el factorial sin el signo "!"\t'))
            f=1
            while(n >= 0):
                  if (n == 0):
                        print(f)
                  else:
                        f = f * n
                  n = n - 1 
            # print(factorial(a))
      else:
            print("Número invalido")
            
      x = input('¿Quiere seguir calculando?')

