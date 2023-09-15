frutas = ["laranja", "maca", "uva"]

print(frutas[0])
print(frutas[1])
print(frutas[2])

print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"],
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

lista = list("python")
print(lista)

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")