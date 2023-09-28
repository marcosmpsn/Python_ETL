def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resuldado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)

op = somar
print(op(10,12))

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500)
print(salario)
print (salario_com_bonus)

salario = 2000

def salario_bonus(bonus):
    salario1 = salario
    salario1 += bonus
    return salario1

salario_com_bonus = salario_bonus(500)
print(salario)
print (salario_com_bonus)


