# The sharp icon allows you to create comments, the green text won't be executed

# This file contains two main sections, first one is the data of the actor, second one is the behavior


class Ropa:
    
    def __init__(self, nombre, talla, precio): # los nombres de los argumentos van con camelCase
        ### ---- DATA ---- ###
        self.Nombre = nombre
        self.Talla = talla # los nombres de los atributos (propiedades, caracteristicas) de la clase van con PascalCase
        self.Precio = precio

class Gloria:
    
    # input -> proceso de esa informacion -> output
    def __init__(self): 
        ### ---- DATA ---- ###
        remeraS = Ropa("una remera", "S", "10")
        remeraL = Ropa("una remera", "L", "20")
        self.Stock = [remeraS,  remeraL]  # [un objeto Ropa, otro objeto Ropa]
        self.Revendedoras = []
    
     ### ---- BEHAVIOR ---- ###
    def AddToStock(self, unaRopa):  ### TAREAAAAAAAAAA ###### 
        self.Stock.append(unaRopa)
    
    def RemoveFromStock(self, ciertaRopa):
        quitarEstaRopa = next(ropa for ropa in self.Stock if ropa.Nombre == ciertaRopa)
        self.Stock.remove(quitarEstaRopa)
    
    def ShowStock(self):
        for itemRopa in self.Stock:
            print(itemRopa.Nombre)
        
    def CountStock(self, consultaRopa):        
        return sum(ropa.Nombre == consultaRopa for ropa in self.Stock)
      

        
class Revendedora:
    def __init__(self, nombre, categoria, almacen):
         ### ---- DATA ---- ###
        self.Pedidos = []
        self.Clientes = []
        self.Nombre = nombre    
        self.Categoría = categoria
        self.Gloria = almacen
        
    
    ### ---- BEHAVIOR ---- ###
    def Vender(self, vendeEstaRopa):
        if self.Gloria.CountStock(vendeEstaRopa) > 0:
            self.Gloria.RemoveFromStock(vendeEstaRopa)
            print("Se vendio la ropa {}".format(vendeEstaRopa))
        else:
            print("No hay mas de este producto: {}".format(vendeEstaRopa))
            
    
    
## Notas

# Siempre que creemos una clase, vamos a crear el metodo __init__ con el argumento (o parametro) self como PRIMER argumento, y luego (OPCIONALMENTE) un parametro por propiedad, ejemplo def __init__(self, primerParametro): self.PrimerParametro = primerParametro

# Las propiedades (self.<nombre de la propiedad> dentro del metodo __init__ de una clase) son informacion inherente al objeto, como tambien relaciones con otros objetos
# si un almacen tiene muchas revendedoras, la popiedad va a ser una lista de objetos ->  self.Revendedoras = []
# si una revendedora tiene un (1) almacen, la popiedad va a ser un (1) objeto -> self.Gloria = Gloria()
                

# DEMO

# gloria = Gloria()
# print("--- vamos a revisar el stock del almacen primero ---")
# gloria.ShowStock()
# gloria.RemoveFromStock("una remera")
# print("--- vamos a revisar el stock del almacen de nuevo ---")
# gloria.ShowStock()

print("--- Setup ---")
gloria = Gloria()
silvinaRevendedora = Revendedora("Silvina", "A", gloria)
print("--- vamos a revisar el stock del almacen primero ---")
gloria.ShowStock()
print("--- Silvina vende una remera ---")
silvinaRevendedora.Vender("una remera")
print("--- vamos a revisar el stock del almacen de nuevo ---")
gloria.ShowStock()


# print("------ Creo una Gloria y muestro el stock, tiene que comenzar con dos remeras ---------")
# gloria = Gloria()
# gloria.ShowStock()
# print(" ----- Busco una remera ------")
# cantidadDeremeras = gloria.FindStock("una remera")
# print(" ----- resultado = {} ------".format(cantidadDeremeras))


# gloria = Gloria()
# print("El stock cuando creas la primer Gloria")
# gloria.ShowStock()

# print("Agrego una remera en la primer Gloria")
# gloria.AddToStock("una remera")
# print("Nuevo stock")
# gloria.ShowStock()

# print("qué estás buscando?")
# gloria.FindStock("una remera")




# print("Quito una remera")
# print("Nuevo stock")
# gloria.RemoveFromStock("una remera")
# gloria.ShowStock()




