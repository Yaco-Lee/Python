# The sharp icon allows you to create comments, the green text won't be executed

# This file contains two main sections, first one is the data of the actor, second one is the behavior

class Gloria:
    ### ---- DATA ---- ###
    
    ### ---- BEHAVIOR ---- ###
    # input -> proceso de esa informacion -> output
    def __init__(self): 
        self.Stock = []
    
    def AddToStock(self, unaRopa):
        self.Stock.append(unaRopa)
    
    def RemoveFromStock(self, ciertaRopa):
        self.Stock.remove(ciertaRopa)
    
    def MostrarStock(self):
        print(self.Stock)
    


# DEMO

gloria = Gloria()
print("El stock cuando creas Gloria")
gloria.MostrarStock()

print("Agrego una remera")
gloria.AddToStock("una remera")
print("Nuevo stock")
gloria.MostrarStock()

print("Quito una remera")
print("Nuevo stock")
gloria.RemoveFromStock("una remera")
gloria.MostrarStock()


