https://replit.com/join/svirhdnohv-sol-veronicaver

from random import randint

random = randint(1,10)
intentos=0
xos=3
numero=0
print("Adivina el número del 1-10. Recuerda que tienes 3 intentos")
while intentos<xos:
  intentos=int(input("Trata de adivinar"))
  intentos+=1

if intentos == numero:
  print(f"Haz adivinado en {intentos}")
elif intentos != numero:
  print("Numero equivocado, intenta de nuevo")
else:
  print("Incorrecto.")

if intentos == xos:
  print("No has conseguido adivinar y tus intentos han terminado")
