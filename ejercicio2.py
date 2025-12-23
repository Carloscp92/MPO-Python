
"""
Escribe un programa en Python que pida al usuario dos números y luego imprima la suma, resta, 
multiplicación y división de ambos números.
"""
numero = int(input("introduce el primer numero:"))
numero2 = int(input("introduce el segundo numero:"))


opcion = -1
while opcion != 0:
 print("==MENU==")
 print("1-Sumar")
 print("2-Restar")
 print("3-Multiplicar")
 print("4-Dividir")
 print("0-Salir")

 opcion = int(input("Introduce una opcion:"))

 match opcion:
  case 1:
   suma = numero + numero2
   print(f"La suma de {numero} y {numero2} es {suma}")

  case 2:
   resta = numero - numero2
   print(f"La resta de {numero} y {numero2} es {resta}")

  case 3:
   multiplicacion = numero * numero2
   print(f"La multiplicacion de {numero} y {numero2} es {multiplicacion}")

  case 4: 
   division = numero/numero2
   print(f"la division de {numero} y {numero2} es {division}")
 
  case 0: 
   print("fin del programa") 

  case _: 
   print("Entrada no valida, elige una opcion")

