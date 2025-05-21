lista_append = [1,2,3]
lista_extend = [4,5,6]
lista_insert =[7,8,9]

lista_letras = ['a','b','c']

print(f'----------APPEND------------')
# Append: perimte agregar elementos en la ultima posicion de la lista
lista_append.append(lista_letras)
print(lista_append)

print(f'----------EXTEND------------')
#extend: permite agregar elementos de una lista a otra lista
lista_extend.extend(lista_letras)
print(lista_extend)

print(f'----------INSERT------------')
#insert: permite agregar elementos en una posicion especifica de la lista
lista_insert.insert(1, lista_letras)
print(lista_insert)