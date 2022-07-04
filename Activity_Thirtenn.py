#Escriba un programa que dados n números enteros determine cual de
# los n-1 números es el más cercano al primero.


def closestNumber(list):
    first = list[0]
    closest = list[1]
    for i in range(1,len(list)):
        number = list[i]
        restOfClosest = abs(first - closest)
        restOfNumber = abs(first - number)
        closest = number if(restOfNumber < restOfClosest) else closest
    return closest

list = [1,100, 6,20,10]
print(closestNumber(list))