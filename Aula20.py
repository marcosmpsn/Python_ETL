nome = "Marcos"
idade = 33
profissao = "Programador"
linguagem = "Python"

pessoa = {"nome": "Thais", "idade": 30, "profissao": "autônomo", "linguagem": "cosméticos"}

print("Olá! Me chamo %s. Tenho %d anos e trabalho como %s especialista em %s" %(nome, idade, profissao, linguagem))

print("Olá! Me chamo {}. Tenho {} anos e trabalho como {} especialista em {}".format(nome, idade, profissao, linguagem))

print("Olá! Me chamo {2}. Tenho {3} anos e trabalho como {1} especialista em {0}".format(linguagem, profissao, nome, idade))

print("Olá! Me chamo {nome}. Tenho {idade} anos e trabalho como {profissao} especialista em {linguagem}".format(**pessoa))

print("Olá! Me chamo {nome}. Tenho {idade} anos e trabalho como {profissao} especialista em {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print(f"Olá! Me chamo {nome}. Tenho {idade} anos e trabalho como {profissao} especialista em {linguagem}")


PI = 3.141592

print(f"Valor de PI: {PI:.2f}")

print(f"Valor de PI: {PI:5.2f}")