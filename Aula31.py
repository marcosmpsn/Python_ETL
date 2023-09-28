pessoa = {"nome": "Marcos", "idade": 33}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "98765-4321"
print(pessoa)

print(pessoa["nome"])

pessoa["nome"] = "Maria"
pessoa["idade"] = 18
pessoa["telefone"] = "12345-6789"
print(pessoa)

contatos = {
    "marcos@xpto.com": {"nome": "Marcos", "telefone": "3333-2222"},
    "thais@xpto.com": {"nome": "Thais", "telefone": "3333-1111"},
    "miuxa@xpto.com": {"nome": "Miúxa", "telefone": "3333-4444"},
    "enzo@xpto.com": {"Nome": "Enzo", "telefone": "3333-3333"}
}

print(contatos["enzo@xpto.com"]["telefone"])

for chave in contatos:
    print(chave, contatos[chave])
