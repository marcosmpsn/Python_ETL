# Desafio: Criando um pipeline de ETL com Python

import pandas as pd
import random

#Extraindo os dados do csv (E)
Base_clientes = pd.read_csv('D:\Cursos\DIO\Python\Desafio\Clientes.csv')
Base_frases = pd.read_csv('D:\Cursos\DIO\Python\Desafio\Frases.csv')

nomes = Base_clientes['Nome'].tolist()
vocativo = Base_frases['Vocativo'].tolist()
frase = Base_frases['Frase'].tolist()

#Transformando os dados (T)
lista = []

for nome in nomes:
    x = random.randint(0,29)
    a = f'{vocativo[x]} {nome}! {frase[x]}'
    lista.append(a)

#Carregar os novos dados em um novo arquivo csv. (L)
Lista_Pronta = pd.DataFrame({'Nome': nomes, 'Frase': lista})
Lista_Pronta.to_csv('D:\Cursos\DIO\Python\Desafio\Lista_Pronta.csv')