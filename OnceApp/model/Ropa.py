class Ropa:
    
    def __init__(self, nombre, talla, precio): # los nombres de los argumentos van con camelCase
        ### ---- DATA ---- ###
        self.Nombre = nombre
        self.Talla = talla # los nombres de los atributos (propiedades, caracteristicas) de la clase van con PascalCase
        self.Precio = precio
        
        
# demo

print("Queremos crear una remera")
unaRemeraTalleS = Ropa("una remera", "S", "10")
print("Se creo una ropa, es esta: {} con talle {}".format(unaRemeraTalleS.Nombre, unaRemeraTalleS.Talla))
