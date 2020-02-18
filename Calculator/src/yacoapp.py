# ACA ES DONDE VAMOS A DEFINIR LAS COSAS
def main():
  operaciones = getOperaciones()
  
  print("tenemos por ahora")
  devuelveListaDeOperaciones(operaciones)

  print("que deseas?")
  accion = getAccion() 
  # print("poné el primer numero wacheen")
  # primernumero = input()
  # print("ahora el segundo")
  # segundonumero = input()
  # x = int(primernumero)
  # y = int(segundonumero)
  numerosACalcular = TomarNumeros()
  busquedaEnOperaciones = operaciones.get(accion)
  if numerosACalcular.len() < 2:
    print("Tenias que poner dos numeros!, ahora se rompe todo")
  result = busquedaEnOperaciones(numerosACalcular[0], numerosACalcular[1])

  print(result)

def TomarNumeros():
  numerosQuePusoElUsuario = []
  print("Pone un numero")
  loquepusoelusuario = input()
  if type(loquepusoelusuario) == int:
    numerosQuePusoElUsuario.append(int(loquepusoelusuario))
  else:
    print("flashaste cualca, no podes poner más numeros")
  print("calculando...")
  return numerosQuePusoElUsuario

def getOperaciones():
  return {
    "sumar": sumar,
    "restar": restar,
    "multiplicar": multiplicar,
    "dividir": dividir,
  }

def getAccion():
  return input()

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


