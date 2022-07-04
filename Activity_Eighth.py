#Escriba un  programa que pida de forma aleatoria un alista de valores numéricos.
#A partir de esta lista dse deben generar dos listas más una con los valores de
# índice par y otra con los valores de índice inpar. Mustre las 3 listas

import random

n = random.randint(1,50)
randomlist = random.sample(range(1, 100), n)
pairIndexes = []
oddIndexes = []
for i in range(0, n):
    if(i % 2 == 0):
        pairIndexes.append(randomlist[i])
    else:
        oddIndexes.append(randomlist[i])

print(f'Lista Original: {randomlist}')
print(f'Lista de indices pares: {pairIndexes}')
print(f'Lista de indices impares: {oddIndexes}')