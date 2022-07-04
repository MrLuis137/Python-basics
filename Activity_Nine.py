#Escriba un programa que almacene, en una variable x la lista obtenida con
# la función range(1,4), a continuación, la modifique para que cada
# componente sea igual al cuadrado del componente original. El programa
#debe mostrar la lista original.

random_list = list(range(1,4))

for i in range(0,len(random_list)):
    random_list[i] = pow(random_list[i], 2)
print(random_list)