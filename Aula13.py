conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Saldo insuficente")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado!")
    else:
        print("Saldo insuficiente")
else:
    print("conta não reconhecida!")
