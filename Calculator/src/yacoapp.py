# ACA ES DONDE VAMOS A DEFINIR LAS COSAS
def main():
  operaciones = {
    "sumar": sumar,
    "restar": restar,
    "multiplicar": multiplicar,
    "dividir": dividir
  }
  print("tenemos por ahora")
  devuelveListaDeOperaciones(operaciones)


  print("que deseas?")
  accion = input()
  print("poné el primer numero wacheen")
  primernumero = input()
  print("ahora el segundo")
  segundonumero = input()
  x = int(primernumero)
  y = int(segundonumero)
  busquedaEnOperaciones = operaciones.get(accion)
 
  result = busquedaEnOperaciones(x,y)

  print(result)



  
def restar(x,y):
  return x-y

def sumar(x, y):
  return x + y

def multiplicar(x,y):
  return x * y

def dividir(x,y):
  if y == 0:
    print("no se puede dividir por cero... aún... ¬¬")
    return 0
  else:
    return  x / y
   

def devuelveListaDeOperaciones(listaDeOperaciones):
  for a in listaDeOperaciones:
   print(a)


################################################

# ACA ES DONDE VAMOS A EJECUTAR LAS COSAS
main()


