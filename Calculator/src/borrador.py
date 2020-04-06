import math
import random

def solution(i):
    primeSet = set()
    commLambdaPrimeList = []

    primeSet.add(2)
    commLambdaPrimeList.append(2)

    for num in range(3,25000):
        is_prime(num, commLambdaPrimeList, primeSet)      

    commLambdaPrimeList[i:i+5]

    strPrimes = ''.join([str(num) for num in commLambdaPrimeList])

    return strPrimes[i:i+5]

def is_prime(i, commLambdaPrimeList, primeSet):
    max_divisor = math.floor(math.sqrt(i))
    isPrime = True
    for d in range(2, 1 + max_divisor):
        if i % d == 0:
            isPrime = False
            break
    exists = i in primeSet
    if (not exists and isPrime):
        primeSet.add(i)
        commLambdaPrimeList.append(i)

