#saldo = 2000.0
#saque = float(input("Informe o valor do saque: "))

#if saldo >= saque:
 #   print("Realizando saque!")
#else:
#    print("Saldo insuficiente!")

opcao = int(input("Informe uma opção: \n [1] Sacar \n [2] Extrato"))

if opcao == 1:
    valor = float(input("Informe o valor do saque: "))
    # Continua o código como no exemplo anterior
elif opcao == 2:
    print("Exibindo o extrato ...")
else:
    print("Opção inválida")
