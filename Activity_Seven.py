#Diseñe un programa que, dada una lista x, sustituya cualquier elemento
# negativo por cero.

list = [0,1,2,3,-4, 300, 0,-94]

def replace_negatves(list):

    for i in range(0,len(list)):
        element = list[i]
        list[i] = 0 if element <0 else element

replace_negatves(list)
print(list)