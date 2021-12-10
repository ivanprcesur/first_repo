num_elegido=int(input ("numero adivinar: "))
intentos=int(input ("introduce numero de intentos maximos: "))
numero_introducido = int(input ("introduce numero que crees que es: "))

while intentos > 1 :
  intentos= intentos-1
  
  if (numero_introducido > num_elegido):
    print ("te quedan ", intentos, "intentos") 
    numero_introducido=int(input ("el numero introducido es mayor "))
    

  elif (numero_introducido < num_elegido):
    print ("te quedan ", intentos, "intentos") 
    numero_introducido=int(input ("el numero introducido es menor "))

  else:
    print ("ACERTASTE EL NUMERO")
    break

print ("se acabaron tus intentos")