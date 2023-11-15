https://replit.com/join/fapicmxxfj-sol-veronicaver
boletos=0 
clientes=0

while True:
  boletos2=0
  clientes+=1
  nombre= input("Cual es tu nombre?")
  print(""" Zona 1 - $ 2000, 
  Zona 2 - $ 1000  
  Zona 3 - $ 700 """)
  zona=input(f"en que zona estas,{nombre}? (1,2,3)")
 
  if zona== "1":
    boletos2+=2000
    print("Son $2000")
  elif zona=="2":
    boletos2+=1000
    print("Son $1000")
  elif zona=="3":
    boletos2+=700
    print("Son $700")
  boletos+=boletos2 
  
  dia=input("Que dia es el concierto?").lower()

  if dia in ["viernes","sabado","domingo"]: 
    print("No aplica")
  elif dia in ["lunes","martes","miercoles","jueves"]:
    cupones=input("Cupones? (si/no)").lower()
    if cupones=="si":
      cupo_v=input("Cuales tienes? (1.Platino 500, 2.Oro 300 y 3.Plata 200)")
      if cupo_v=="1":
        boletos-=500
      elif cupo_v=="2":
        boletos-=300
      elif cupo_v=="3":
        boletos-=200
      else:
        print("No hay")
    else:
      print("va")
  else: 
    print("No existe")
  print(f"nombre:{nombre}, su total el:{boletos}")   
  x=input("Hay otro cliente?: ").lower()
  if x !="si":
    break 
  else: 
    print("")
print(f"reporte:total{clientes}")  
print(f"total ganancias:{boletos}")
