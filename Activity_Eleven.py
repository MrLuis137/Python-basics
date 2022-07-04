#Escriba una función llamada sumaEnt que reciba una lista
# de números y devuelva el resultado de sumarlos todos

def sumaEnt(list):
    sum = 0
    for number in list:
        sum += number
    return sum

list = [1,100, 6,20,10]
print(sumaEnt(list))