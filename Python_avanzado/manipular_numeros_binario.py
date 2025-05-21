

#Creacion ce numeros binarios
bin_5 = 0b101
bin_10 = 0b1010


resultado_int = bin_5 + bin_10

#eprsentacion en modno normla
print(bin_5)
print(bin_10)
print(resultado_int)


#Reprentacion en modo binario
print(f'Est es el numero { bin_5} en numero binario: {bin(bin_5)}')
print(f'Est es el numero { bin_10} en numero binario: {bin(bin_10)}')
print(f'Est es el numero { resultado_int} en numero binario: {bin(resultado_int)}')

print('-------Numeros binarios en formato string----------')
#Numeros binarios en formato string
binario_7_string = '0b111'
binario_12_string = '0b1100'
#El nuemro es la base 2 ya que asi es en binario
resultado_int_string = int(binario_7_string, 2) + int(binario_12_string, 2)

print(binario_7_string)
print(binario_12_string)
print(f'El resultado de la suma es: {resultado_int_string}')
print(f'El resultado de la suma es: {bin(resultado_int_string)}')

