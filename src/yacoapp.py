# ACA ES DONDE VAMOS A DEFINIR LAS COSAS
def main():
  print("que deseas?")
  accion = input()
  primernumero = input()
  segundonumero = input()
  x = int(primernumero)
  y = int(segundonumero)
  result = 0

  if accion == "sumar":
   result = sumar(x,y)
  elif accion == "restar":
   result = restar(x,y)
  else:
   print("Por ahora solo sumo y resto wacho, awantia")

  print(result)
  
def restar (x,y):
  return x-y

def sumar(x, y):
  return x + y


################################################

# ACA ES DONDE VAMOS A EJECUTAR LAS COSAS
main()


