# The sharp icon allows you to create comments, the green text won't be executed

# This file contains two main sections, first one is the data of the actor, second one is the behavior


from flask import Flask
from flask_restful import Resource, Api
from dataclasses import dataclass
import json


app = Flask(__name__)
api = Api(app)


@dataclass  
class Ropa:
    nombre: str
    talla: str  
    codigodebarra: str
    precio: float = 0.0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


    

    # def __init__(self, nombre : str, talla : str, precio : int, codigoDeBarra : str): # los nombres de los argumentos van con camelCase
    #     ### ---- DATA ---- ###
    #     self.Nombre = nombre
    #     self.Talla = talla # los nombres de los atributos (propiedades, caracteristicas) de la clase van con PascalCase
    #     self.Precio = precio
    #     self.CodigoDeBarra = codigoDeBarra

class Gloria(Resource):
    
    stock = [] # static variable as an empty list

    # input -> proceso de esa informacion -> output
    def __init__(self): 
        ### ---- DATA ---- ###
        #self.Stock = []  # [un objeto Ropa, otro objeto Ropa]
        self.Revendedoras = []
    
     ### ---- BEHAVIOR ---- ###

    def get(self):
        stockAsJson = []
        for ropa in Gloria.stock:
            stockAsJson.append(ropa.  ())
        return {"stock" : stockAsJson}     

    def post(self):
        ropacreada = Ropa("buzo", "L", "B1231", 1300.5)
        self.AddToStock(ropacreada)
        self.ShowStock()
        return {"codigoDeBarra" : ropacreada.toJSON()}

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def AddToStock(self, unaRopa: "Ropa"):
        Gloria.stock.append(unaRopa)
    
    def RemoveFromStock(self, ciertaRopa : "Ropa"):
        quitarEstaRopa = next(ropa for ropa in Gloria.stock if ropa.CodigoDeBarra == ciertaRopa.CodigoDeBarra) # a partir de la funcion next estamos haciendo una busqueda en el stock por una ropa con el mismo codigo de barra
        Gloria.stock.remove(quitarEstaRopa)
    
    def ShowStock(self):
        if len(Gloria.stock) == 0:
            print("Nada por aquí")
        else: 
            print(Gloria.stock)


        # else:
        #     for itemRopa in self.Stock: 
        #         print("Tenemos {} con el codigo {}".format(itemRopa.Nombre, itemRopa.CodigoDeBarra))
    




    # TODO please, do not use for the moment    
    def CountStock(self, consultaRopa: "Ropa"):        
        return sum(ropa.Nombre == consultaRopa.Nombre and ropa.Talla == ropa.Talla for ropa in Gloria.stock)
      
    # revendedora le pide al almacen que busque una determinada ropa y se la de
    def SearchRopa(self, searchRopa: "Ropa") -> "Ropa":
        ropaEncontrada = next(ropa for ropa in Gloria.stock if ropa.Nombre == searchRopa.Nombre and ropa.Talla == searchRopa.Talla)
        return ropaEncontrada



class Revendedora:
    def __init__(self, nombre: str, categoria: str, almacen):
         ### ---- DATA ---- ###
        self.Pedidos = []
        self.Clientes = []
        self.Nombre = nombre    
        self.Categoría = categoria
        self.Gloria = almacen
        
    ### ---- BEHAVIOR ---- ###
    def Vender(self, vendeEstaRopa: "Ropa"):
        if self.Gloria.SearchRopa(vendeEstaRopa) > 0:
            self.Gloria.RemoveFromStock(vendeEstaRopa)
            print("Se vendio la ropa {}, en talle {}, con codigo de barra {}".format(vendeEstaRopa.Nombre, vendeEstaRopa.Talla, vendeEstaRopa.CodigoDeBarra))
        else:
            print("No hay mas de este producto: {}".format(vendeEstaRopa.Nombre))
            print("queres realizar un pedido de {}? si/no".format(vendeEstaRopa.Nombre))
            if input().lower() == "si":
                self.Pedidos.append(vendeEstaRopa)
                print("Se realizó exitosamente el pedido")
            else:
                print("No se realizó ningun pedido")
    
    def ShowPedidos(self):
        if len(self.Pedidos) == 0:
            print("Nada por aquí")
        else:
            for itemRopa in self.Pedidos: 
                print("Tenes pedido {} en talle {}".format(itemRopa.Nombre, itemRopa.Talla))        
            
            
    
    
## Notas

# Siempre que creemos una clase, vamos a crear el metodo __init__ con el argumento (o parametro) self como PRIMER argumento, y luego (OPCIONALMENTE) un parametro por propiedad, ejemplo def __init__(self, primerParametro): self.PrimerParametro = primerParametro

# Las propiedades (self.<nombre de la propiedad> dentro del metodo __init__ de una clase) son informacion inherente al objeto, como tambien relaciones con otros objetos
# si un almacen tiene muchas revendedoras, la popiedad va a ser una lista de objetos ->  self.Revendedoras = []
# si una revendedora tiene un (1) almacen, la popiedad va a ser un (1) objeto -> self.Gloria = Gloria()

# API
# A partir de aca definimos nuestra API
# api.add_resource(User, '/users')

api.add_resource(Gloria, "/stock")

app.run(debug=True)

# Tests

#gloria = Gloria()

#remera = Ropa("remera", "S", "AAAA1111", 15.5)

#gloria.AddToStock(remera)
#print(gloria.ShowStock())