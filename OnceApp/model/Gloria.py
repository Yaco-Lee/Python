# The sharp icon allows you to create comments, the green text won't be executed

# This file contains two main sections, first one is the data of the actor, second one is the behavior

class Gloria:
    
    # input -> proceso de esa informacion -> output
    def __init__(self): 
        ### ---- DATA ---- ###
        self.Stock = []
        self.Revendedoras = []
    
     ### ---- BEHAVIOR ---- ###
    def AddToStock(self, unaRopa):
        self.Stock.append(unaRopa)
    
    def RemoveFromStock(self, ciertaRopa):
        self.Stock.remove(ciertaRopa)
    
    def ShowStock(self):
        print(self.Stock)
        
    def FindStock(self, consultaRopa):
        if consultaRopa in self.Stock:
            txt = "Si, tenemos {} en stock wachina"
            print(txt.format(consultaRopa))


        
        

# DEMO

gloria = Gloria()
print("El stock cuando creas la primer Gloria")
gloria.ShowStock()

print("Agrego una remera en la primer Gloria")
gloria.AddToStock("una remera")
print("Nuevo stock")
gloria.ShowStock()

print("qué estás buscando?")
gloria.FindStock("una remera")




# print("Quito una remera")
# print("Nuevo stock")
# gloria.RemoveFromStock("una remera")
# gloria.ShowStock()




