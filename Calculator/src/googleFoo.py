import math
import random

def solution(n):
    poneleNombreYaquin = set()
    commLambdaPrimeList = []

    poneleNombreYaquin.add(2)
    commLambdaPrimeList.append(2)

    for num in range(3,25000):
        is_prime(num, commLambdaPrimeList, poneleNombreYaquin)      

    commLambdaPrimeList[n:n+5]

    primosComoTexto = ''.join([str(num) for num in commLambdaPrimeList])

    return primosComoTexto[n:n+5]

def is_prime(n, commLambdaPrimeList, poneleNombreYaquin):
    max_divisor = math.floor(math.sqrt(n))
    isPrime = True
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            isPrime = False
            break
    exists = n in poneleNombreYaquin 
    if (not exists and isPrime):
        poneleNombreYaquin.add(n)
        commLambdaPrimeList.append(n)


## Test de funcion solution
## Python cases
# Input:
# Output:
print('funciono? {}'.format("23571" == solution(0)))

# Input:
solution(3)
# Output:
#    71113
print('funciono? {}'.format("71113" == solution(3)))



## Tests de Range

# print('primero')
# lista = range(3,1)
# for n in lista:
#     print(n)
# print('segundo')
# lista2 = range(3,3)
# for m in lista2:
#     print(m)
# print('tercero')
# lista3 = range(3,4)
# for x in lista3:
#     print(x)


# Test
# commLambdaPrimeList[2,3,5,7,11,13]
# hatNumber = 0
# esto significa que queremos ir de commLambdaPrimeList[0] = 2 a commLambdaPrimeList[5] = 13
# los numeros que vamos a obtener son 2,3,5,7,11,13



