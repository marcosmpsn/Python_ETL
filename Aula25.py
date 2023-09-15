lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

lista.clear()
print(lista)

lista = [1, 'Python', [40, 30, 20]]
l2 = lista.copy()
print(l2)

cores = ["vermelho", "azul", "verde", "azul"]
print(cores.count("vermelho"))
print(cores.count("verde"))
print(cores.count("azul"))

lista.extend(["java", "csharp"])
print(lista)

lista.extend(l2)
print(lista)

print(lista.index("Python"))
print(lista.index("java"))
print(lista.index(1))

lista.pop()
print(lista)

lista.pop(2)
print(lista)

lista.remove("java")
print(lista)

lista.remove("Python")
print(lista)

lista.reverse()
print(lista)

linguagens = ["python", "js", "c", "java", "csharp"]
numeros = [1, 45, 32, 98, 65, 48, 27]

linguagens.sort()
print(linguagens)

numeros.sort()
print(numeros)

linguagens.sort(reverse=True)
print(linguagens)

numeros.sort(reverse=True)
print(numeros)

linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)
