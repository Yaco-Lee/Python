# Python

## Variables

- Declarar una variable
  - simplemente se escribe el nombre de la variable, por ej: soyUnaVariable
- Asignarle un valor a una variable
  - soyUnaVariable = 1 + 1 // un integer
  - soyUnaVariable = "Hola Yaco!" // un string
  - soyUnaVariable = true // un bolean
  - soyUnaVariable = [] // una lista vacia

## Listas

- Crear una lista
  - Necesitas una varible donde se guarde esa lista
    - Ej: miLista = [] // una lista vacia
  - Tambien podes iniciar la lista con valores
    - Ej: miLista = [1,2,3,4] // lista de numeros
    - Ej: miLista = ["Lunes", "Martes", "Miercoles"] // lista de strings
  - La lista puede contener objetos que vos hallas definido
    - Ej: primero defino el objeto creando una clase
      - class Persona(): def __init__(self, nombre, dni) self.Nombre = nombre self.DNI = dni // aca hago todo en una linea pero para que lo leas no mas, se hace con enter
      - luego podes crear la lista con objetos o instancias que parten de la clase Persona
      - miLista = [Persona("Yaco", 34056789), Persona("Bichim", 35032310)]
  - Agregar un item a una lista
    - Primero creas la lista guardandola en una variable, luego usas esa variable para agregar items a la lista
    - miLista = [1,2,3]
    - miLista.append(4) // miLista ahora va a quedar asi [1,2,3,4]
    - Si quiero agregar un objeto a una lista
    - miLista = [Persona("Yaco", 34056789), Persona("Bichim", 35032310)]
    - miLista.append(Persona("Lucas", 35708456))
  - Obtener un item de la lista
    - Hay un par de formas, pero nos interesa esta en particular
    - miItemDeLaLista = next(persona for persona in miLista if persona.Nombre == "Bichim") // basicamente itera por cada item en la lista y devuelve el primero que cumple la condicion, desp hablamos bien de condiciones porque podemos agregar varias condiciones.
  - Remover un item de una lista
    - Lo podes hacer pasando el valor exacto, esto funciona bien cuando la lista es de numeros, strings, boolean, o valores basicos (con los objetos que definimos nosotros es mejor hacerlo de otra forma)
    - miLista = [1,2,3,4]
    - miLista.remove(4) // miLista ahora va a quedar asi [1,2,3] 
    - miLista = ["Lunes", "Martes", "Miercoles"]
    - miLista.remove("Lunes") // miLista ahora va a quedar asi  ["Martes", "Miercoles"]
  - Remover un item de una lista cuando el item es un objeto que nosotros definimos
    - miLista = [Persona("Yaco", 34056789), Persona("Bichim", 35032310)]
    - Primero guardamos en una variable el objeto que queremos quitar de la lista
    - Para eso usamos el next
    - personaAQuitar = next(persona for persona in miLista if persona.Nombre == "Bichim")
    - miLista.remove(personaAQuitar)
