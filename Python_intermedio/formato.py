
numeroA = "{:.0f}".format(2.4)
print(numeroA)

numeroB = "{:.2f}".format(2.8)
print(numeroB)

numeroC = "{:.2f}".format(2.888)
print(numeroC)

numeroD = "{:0>5}".format(2.5)
print(numeroD)

numeroE = "{:0<5}".format(2.5)
print(numeroE)

# Cambia el separador de miles
numeroF = "{:,}".format(1000)
print(numeroF)


print(f"{2.5:.2f}")