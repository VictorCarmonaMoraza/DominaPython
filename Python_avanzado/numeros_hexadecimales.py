hex_1997 = 0x7CD
hex_2023 = 0x7E7


resultado_int = hex_2023 - hex_1997

print(hex_1997)
print(hex_2023)
print(resultado_int)


#Verlos en hexadecimal
print(hex(hex_1997))
print(hex(hex_2023))
print(hex(resultado_int))


print('-------Numeros hexadecimales en formato string----------')

#numeros hexadecimales en formato string
hex_15_string = '0xF'
hex_10_string = '0xa'
resultado_int_string = int(hex_15_string, 16) + int(hex_10_string, 16)
print(int(hex_15_string,16))
print(int(hex_10_string,16))
print(f'El resultado de la suma es: {resultado_int_string}')