conjunto1 = set([1, 2, 3, 1, 2, 3])
print(conjunto1)

conjunto2 = set("abacaxi")
print(conjunto2)

conjunto3 = set(("palio", "gol", "celta", "palio"))
print(conjunto3)

conjunto4 = {"python", "java", "python"}
print(conjunto4)

conjunto5 = {1, 2, 1, 4, 2, 4, 6, 3, 5, 6}
print(conjunto5)

numeros = {1, 2, 3, 2}

numeros = list(numeros)
print(numeros)

print(numeros[0])

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")