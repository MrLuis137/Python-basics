#Escriba un programa que pida de forma aleatoria 20 números (entre el
# 1 y el 10), y los almacene en una lista. El programa debe mostrar
# la lista original y la lista en orden inverso

import random

randomlist = []
for i in range(0,20):
    randomlist.append(random.randint(1,10))
reverseList = randomlist.copy()
reverseList.reverse()
print(f'lista random original: {randomlist}')
print(f'lista en orden inverso: {reverseList}')