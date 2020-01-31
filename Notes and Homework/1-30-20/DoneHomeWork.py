

# Inciso 1

print("creo una lista del 1 al 5")

listaincisouno = [1,2,3,4,5]

print(listaincisouno)

print("ahora le agrego un numero")

listaincisouno.append(6)

print(listaincisouno)

print("ahora le quito un numero")

listaincisouno.remove(1)

print(listaincisouno)

print("Ahora quito los numeros pares de la lista que me quedó")

for x in listaincisouno:
    if x%2 != 0:
        print(x)
    else:
        pass
        
print("Listo, ya me merezco una birra (? ")



# Inciso 2

class Persona:
    def __init__(self, nombre , dni):
        self.Nombre = nombre
        self.Dni = dni
    
    
listaincisodos = [Persona("Gervasio", "10759330"), Persona("Hermenegildo", "3250174")]
    
print("Acá va la lista de personas")

print(listaincisodos)

listaincisodos.append(Persona("Hortensia", "12121210"))
    
print("Acá va la lista de personas con una agregada")
    
print(listaincisodos)

print("Finalmente le quito una persona")

chautefuiste = next(Persona for Persona in listaincisodos if Persona.Nombre == "Gervasio")

listaincisodos.remove(chautefuiste)

print(listaincisodos)

final = "TERMINADO"

for x in final:
    print(x)
    
    

    

    
