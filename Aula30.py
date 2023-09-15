conjunto_a = {1, 2}
conjunto_b = {3, 4}

uniao = conjunto_a.union(conjunto_b)
print(uniao)

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao)

diferenca1 = conjunto_a.difference(conjunto_b)
print(diferenca1)

diferenca2 = conjunto_b.difference(conjunto_a)
print(diferenca2)

diferenca_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print(diferenca_simetrica)

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

a_contido_em_b = conjunto_a.issubset(conjunto_b)
print(a_contido_em_b)

b_contido_em_a = conjunto_b.issubset(conjunto_a)
print(b_contido_em_a)

a_contem_b = conjunto_a.issuperset(conjunto_b)
print(a_contem_b)

b_contem_a = conjunto_b.issuperset(conjunto_a)
print(b_contem_a)

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

a_distinto_b = conjunto_a.isdisjoint(conjunto_b)
print(a_distinto_b)

a_distinto_c = conjunto_a.isdisjoint(conjunto_c)
print(a_distinto_c)

sorteio = {1, 23}

sorteio.add(25)
print(sorteio)

sorteio.add(42)
print(sorteio)

sorteio.add(25)
print(sorteio)

sorteio = {1, 23}

sorteio.clear()
print(sorteio)

sorteio = {1, 23}
sorteio1 = sorteio.copy()

print(sorteio1)

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)

numeros.discard(1)
print(numeros)

numeros.discard(45)
print(numeros)

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)

numeros.pop()
print(numeros)

numeros.pop()
print(numeros)

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)

numeros.remove(0)
print(numeros)

numeros.remove(5)
print(numeros)

#numeros.remove(38)
print(numeros)

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(numeros)
print(len(numeros))

print(1 in numeros)
print(10 in numeros)