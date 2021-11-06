#cambio de monedas

   
#entrada de datos 

compra = input('\n¿Cual es el precio final de la compra?\t')

#boton de exit
while compra != '+':
   
   compra = float(compra)
   pagado = float(input('\n¿Cual es el la cantidad de dinero abonada?\t'))

#primera salida de datos, dinero a devolver
   cambio = round((pagado-compra),2)
   print('A devolver\t' + str(cambio))

#declaración de variables

   b_500 =  int(cambio/500)         #monedas de 500$
   resto = cambio % 500
   b_200 =  int(resto/200)          #monedas de 200$
   resto = resto % 200
   b_100 =  int(resto/100)          #monedas de 100$
   resto = resto % 100
   b_50 =   int(resto/50)           #monedas de 50$
   resto = resto % 50
   b_20 =   int(resto/20)           #monedas de 20$
   resto = resto % 20
   b_10 =   int(resto/10)           #monedas de 10$
   resto = resto % 10
   b_5 =    int(resto/5)            #monedas de 5$
   resto = resto % 5
   m_2 =    int(resto/2)            #monedas de 2$
   resto = resto % 2
   m_1 =    int(resto/1)            #monedas de 1$
   resto = resto % 1
   m_05 =   int(resto/0.5)          #monedas de 50 cent
   resto = resto % 0.5          
   m_02 =   int(resto/0.2)          #monedas de 20 cent
   resto = resto % 0.2             
   m_01 =   int(resto/0.1)          #monedas de 10 cent
   resto = resto % 0.1             
   m_005 =  int(resto/0.05)         #monedas de 5 cent
   resto = resto % 0.05            
   m_002 =  int(resto/0.02)         #monedas de 2 cent
   resto = resto % 0.02             
   m_001 =  int(resto/0.01)         #monedas de 1 cent
   resto = resto % 0.01             

#en caso de que el importe sea exacto
   if str(cambio) == '0.0':
      print ('No hay cambio que devolver ')
   elif str(cambio) < '0':
      print('No dispones de saldo suficiente, prueba mas adelante')
   else:

#billete 500
      if str(b_500) == '0':                               #no hay billetes
         pass
      elif str(b_500) == '1':                             #1 billete
         print ('1 billete de 500€')
      else:                                               #resto
         print (str(b_500)+' billetes de 500€')
   
#billete 200
      if str(b_200) == '0':                               #no hay billetes 
         pass
      elif str(b_200) == '1':                             #1 billete
         print ('1 billete de 200€')
      else:                                               #resto
            print (str(b_200)+' billetes de 200€')
   
#billete 100
      if str(b_100) == '0':                               #no hay billetes 
         pass
      elif str(b_100) == '1':                             #1 billete
         print ('1 billete de 100€')
      else:                                               #resto
         print (str(b_100)+' billetes de 100€')
   
#billete 50
      if str(b_50) == '0':                                #no hay billetes 
         pass
      elif str(b_50) == '1':                              #1 billete
         print ('1 billete de 50€')
      else:                                               #resto
         print (str(b_500)+' billetes de 50€')
   
#billete 20
      if str(b_20) == '0':                                #no hay billetes 
         pass
      elif str(b_20) == '1':                              #1 billete
         print ('1 billete de 20€')
      else:                                               #resto
         print (str(b_20)+' billetes de 20€')
   
#billete 10
      if str(b_10) == '0':                                #no hay billetes 
         pass
      elif str(b_10) == '1':                              #1 billete
         print ('1 billete de 10€')
      else:
         print (str(b_10)+' billetes de 10€')
   
#billete 5
      if str(b_5) == '0':                                 #no hay billetes 
         pass
      elif str(b_5) == '1':                               #1 billete
         print ('1 billete de 5€')
      else:                                               #resto
         print (str(b_5)+' billetes de 5€')
   
#moneda 2 
      if str(m_2) == '0':                                 #no hay monedas
         pass
      elif str(m_2) == '1':                               #1 moneda
         print ('1 moneda de 2€')
      else:                                               #resto
         print (str(m_2)+' monedas de 2€')

#moneda 1 
      if str(m_1) == '0':                                 #no hay monedas
         pass
      elif str(m_1) == '1':                               #1 moneda
         print ('1 moneda de 1€')
      else:                                               #resto
         print (str(m_1)+' monedas de 1€')

#moneda 50 
      if str(m_05) == '0':                                #no hay monedas
         pass
      elif str(m_05) == '1':                              #1 moneda
         print ('1 moneda de 50 centimos')
      else:
         print (str(m_05)+' monedas de 50 centimos')

#moneda 20  
      if str(m_02) == '0':                                #no hay monedas
         pass
      elif str(m_02) == '1':                              #1 moneda
         print ('1 moneda de 20 centimos')
      else:                                               #resto
         print (str(m_02)+' monedas de 20 centimos')

#moneda 10 
      if str(m_01) == '0':                                #no hay monedas
         pass
      elif str(m_01) == '1':                              #1 moneda
         print ('1 moneda de 10 centimos')
      else:                                               #resto
         print (str(m_01)+' monedas de 10 centimos')

#moneda 5 
      if str(m_005) == '0':                               #no hay monedas
         pass
      elif str(m_005) == '1':                             #1 moneda
         print ('1 moneda de 5 centimos')
      else:                                               #resto
         print (str(m_005)+' monedas de 5 centimos')
   
#moneda 2 
      if str(m_002) == '0':                               #no hay monedas
         pass
      elif str(m_002) == '1':                             #1 moneda
         print ('1 moneda de 2 centimos')
      else:                                               #resto
         print (str(m_002)+' monedas de 2 centimos')

#moneda 1 
      if str(m_001) == '0':                               #no hay monedas
         pass
      elif str(m_02) == '1':                              #1 moneda
         print ('1 moneda de 1 centimo')
      else:                                               #resto
         print (str(m_001)+' monedas de 1 centimo')
   


