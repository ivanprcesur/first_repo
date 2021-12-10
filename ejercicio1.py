numero_introducido = int(input ("introduce numero: "))
num_elegido=int(5)
print (numero_introducido)

while numero_introducido!=num_elegido:

  if (numero_introducido > num_elegido):
    numero_introducido=int(input ("el numero introducido es mayor "))
  else:
      numero_introducido=int(input ("el numero introducido es menor "))

  
print ("acertaste")