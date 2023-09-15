saldo = 1000
saque = 200
limite = 100
conta_especial = True

op_e = saldo >= saque and saque <= limite
#print(op_e)
#print(not op_e)

op_ou = saldo >= saque or saque <= limite
#print(op_ou)
#print(not op_ou)

a = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
b = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(a)
print(b)