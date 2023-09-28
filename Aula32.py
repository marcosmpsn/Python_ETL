contatos = {
    "marcos@xpto.com": {"nome": "Marcos", "telefone": "3333-2222"},
    "thais@xpto.com": {"nome": "Thais", "telefone": "3333-1111"},
    "miuxa@xpto.com": {"nome": "Miúxa", "telefone": "3333-4444"},
    "enzo@xpto.com": {"Nome": "Enzo", "telefone": "3333-3333"}
}
print(contatos)

contatos.clear()
print(contatos)

contatos = {
    "marcos@xpto.com": {"nome": "Marcos", "telefone": "3333-2222"},
    "thais@xpto.com": {"nome": "Thais", "telefone": "3333-1111"},
    "miuxa@xpto.com": {"nome": "Miúxa", "telefone": "3333-4444"},
    "enzo@xpto.com": {"Nome": "Enzo", "telefone": "3333-3333"}
}
copia = contatos.copy()
print(copia)

pessoas = dict.fromkeys(["nome", "telefone"])
print(pessoas)

pessoas2 = dict.fromkeys(["nome", "telefone"], "vazio")
print(pessoas2)

print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("marcos@xpto.com", {}))

print(contatos.items())

print(contatos.keys())

print(contatos)
print(contatos.pop("enzo@xpto.com"))
print(contatos)
print(contatos.pop("enzo@xpto.com", {}))

contatos = {
    "marcos@xpto.com": {"nome": "Marcos", "telefone": "3333-2222"},
    "thais@xpto.com": {"nome": "Thais", "telefone": "3333-1111"},
    "miuxa@xpto.com": {"nome": "Miúxa", "telefone": "3333-4444"},
    "enzo@xpto.com": {"Nome": "Enzo", "telefone": "3333-3333"}
}
contatos.popitem()
print(contatos)
contatos.popitem()
print(contatos)
contatos.popitem()
print(contatos)

dados = {"nome": "Marcos", "telefone": "3333-2222"}
print(dados.setdefault("nome", "Maria"))
print(dados.setdefault("idade", 33))
print(dados)

contatos = {
    "marcos@xpto.com": {"nome": "Marcos", "telefone": "3333-2222"},
    "thais@xpto.com": {"nome": "Thais", "telefone": "3333-1111"},
    "miuxa@xpto.com": {"nome": "Miúxa", "telefone": "3333-4444"},
    "enzo@xpto.com": {"Nome": "Enzo", "telefone": "3333-3333"}
}
contatos.update({"enzo@xpto.com": {"nome": "Peruca", "telefone": "3333-5555"}})
print(contatos)

contatos.update({"bento@xpto.com": {"nome": "Bento", "telefone": "3333-7777"}})
print(contatos)

print(contatos.values())

print("telefone" in dados)
print("maria@xpto.com" in contatos)
print("telefone" in contatos["marcos@xpto.com"])
print("idade" in contatos["marcos@xpto.com"])

print(contatos)

del contatos["bento@xpto.com"]
print(contatos)

del contatos["marcos@xpto.com"]["telefone"]
print(contatos)