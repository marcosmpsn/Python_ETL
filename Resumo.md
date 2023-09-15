# RESUMO PYTHON
[Python.Org](https://www.python.org/)

[Boson Treinamentos - Tutorial](http://www.bosontreinamentos.com.br/programacao-em-python/guia-basico-da-funcao-print-em-python/)

# 1. TIPOS (Aula1.py)
Os tipos são as características e comportamentos de um valor (objeto).
## 1.1 - Tipos padrões (built-in)
| TIPO | DESCRIÇÃO |
| ------- | ------ |
| Texto | str (*string*) |
| Numérico | int (inteiro), float (decimais), complex (complexos) |
| Sequência | list (lista), tuple (*tupla?*), range (sequência ordenada) |
| Mapa | dict (chave,valor) |
| Coleção | set, fronzenset (semelhante a lista, porém sem elementos repetidos) |
| Booleano | bool (verdadeiro, falso; 0, 1) |
| Binário | bytes, bytearray, memoryview |

**Exemplos**
```
a = "hello world"
b = type(a)
print(b)

>>><class 'str'>

```
```
a = 10 + 3
b = type(a)
print(b)

>>><class 'int'>
```
```
a = 1.5 + 3.824
b = type(a)
print(b)

>>><class 'float'>

```
Ou seja, o Python já reconhece automaticamente o tipo (classe) dessas variáveis.

# 2. Modo Interativo
O modo interativo executa o python direto no terminal. Dessa forma, para situações mais simples, não é necessário escrever um código na liguagem para executar as ações. Exemplo: no modo interativo, para fazer uma soma, basta digitar 10 + 3 e o terminal apresentará o resultado (13), sem a necessidade de se digitar print(10 + 3).

Do mesmo modo, é possível abrir um programa já desenvolvido, por meio do comando *python -i*

```
>>>python -i [nome do programa].py
```

# 3. Variáveis e Constantes (Aula2.py)
## 3.1 - Variáveis
São valores que se modificam ao longo do programa. "Nascem" com um valor e são modificados conforme o programa roda

**Exemplo:**
```
a = 1 #valor inicial da variável
a = a + 12 #define o novo valor da variável

"a" agora é o valor anterior (1) + 12

print("a vale:", a)

>>>a vale: 13
```
## 3.2 - Constantes
Assim como as variáveis, as contantes também armazenam valores. Porém, as constantes <mark>**não**</mark> alteram seu valor conforme o programa roda.

Ao contrário de outras linguagens de programação, em Python não existe um comando ou um palavra para definir uma constante. Por convenção, para informar que a variável é constante, ela é escrita no código usando letras <mark>**MAIÚSCULAS**</mark>:

```
ESTADOS = ['SP', 'MG', 'RJ']
PI = 3.141592
```
## 3.3 - Boas práticas:
- Continuando com convenções, como a definição de constantes, outra muito utilizada é o padrão de nomes em *snake case*, tanto para o nome do arquivo quanto para variáveis no código.

    Consiste em substituir os espaços em nomes por um "_"(*underline*). Exemplo: produtos_em_estoque, clientes_vip

- Outro exemplo de boas práticas é a escolha de nomes sugestivos, que facilitem o entendimento do código e das variáveis utilizadas.

    Exemplo: Nomeie a variável que irá receber as vendas totais com um nome como "total_de_vendas" ao invés de um nome genérico como "a" que só você entende.

    Isso facilita para outros e até para você mesmo, quando for pegar um código antigo, por exemplo.

## 3.4 Convertendo o tipo da variável (Aula3.py)

É possivel fazer a conversão do tipo da variável. Por exemplo, transformar números em  uma *string* em números inteiros, ou inteiros em *float*.

```
preco = 10
print(type(preco))
print(preco)

>>><class 'int'>
10

preco = float(10)
print(type(preco))
print(preco)

>>><class 'float'>
10.0
```

É possível converter um valor *int* para *float*, e vice-versa, por meio de uma divisão:

```
preco = 10
metade = preco /2
print(type(metade))
print(metade)

>>><class 'float'>
5.0

preco = 11
metade = preco //2
print(type(metade))
print(metade)

>>><class 'int'>
5

```
<sub>Obs: O operador "//" dá como resultado apenas a perte inteira da dividão</sub>

Também é possível converter números em *string*, para que se possa concatenar em uma frase

```
idade = 28
preco = 10.50

inf1 = str(idade)
inf2 = str(preco)
print(type(inf1), inf1)
print(type(inf2), inf2)

print (idade + preco)
print(inf1 + inf2)


>>><class 'str'> 28
<class 'str'> 10.5
38.5
2810.5
```
Perceba que o último resultado (2810.5) foi um "juntamento" das variáveis inf1 e inf2. Como são *string*, o python as lê como texto e junta as duas numa coisa só, não realizando a soma como em "idade + preco" (38.5)

Uma outra forma de transformar números em uma *string* é inserir elas em um texto. Para isso, é necessário colocar um "f" antes do texto e inserir as variáveis dentro de {}(chaves). Assim o texto final será uma *string*, mas as variáveis continuam sendo números.

```
idade = 28
preco = 10.50

texto = f"idade {idade} preco {preco}"
print(type(texto))
print(texto)

>>><class 'str'>
idade 28 preco 10.5
```

Da mesma forma, é possível fazer o inverso, transformar uma *string* em número, definindo-a conforme a necessidade

```
idade = '28'
preco = '10.50'

print(type(idade))
print(type(preco))

>>><class 'str'>
<class 'str'>

inf1 = int(idade)
inf2 = float(preco)

print(type(inf1))
print(inf1)

print(type(inf2))
print(inf2)

>>><class 'int'>
28
<class 'float'>
10.5
```

## 3.5 - Erro de conversão
Caso o python não consiga converter as variáveis, ele mostrará uma mensagem de erro no terminal.

```
preco = 'python'
inf1 = float(preco)

print(type(inf1))
print(inf1)

>>>Traceback (most recent call last):
  File "d:\Cursos\DIO\Python\Aula3.py", line 52, in <module>
    inf1 = float(preco)
           ^^^^^^^^^^^^
ValueError: could not convert string to float: 'python'
```

# 4. Funções (Aula4.py)
## 4.1 Função *input*
A função *input* é uma função *built in* no python (já instalada por padrão). Ela é utilizada quando o usuário deve inserir o dado pelo teclado, sendo armazenado no código. A função armazena os dados como *string* (str).

```
nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
print(nome)
print(type(nome))
print(idade)
print(type(idade))

>>>Informe seu nome: Marcos
Informe sua idade: 33
Marcos
<class 'str'>
33
<class 'str'>
```
## 4.2 Função *print*
Já usamos essa função desde início, mas vamos nos aprofundar um pouco mais.

A função *print* apresenta na tela (terminal) o dado ou variável colocada na funcão. É possivel apresentar mais de um dado na mesma linha da função e existem alguns argumentos que podem ser utilizados nessa função (sep, end, file e flush)

| Argumento | Função |
|---|---|
| sep | troca o separador das variáveis pedidas. Caso não seja especificado, o padrão é " " (espaço). |
| end | insere o valor/caractere ao final das variáveis utilizadas. Caso não seja especificado, o padrão é uma nova linha (\n) |
| file |  Especifica um objeto com um método write, com um arquivo. O padrão é o dispositivo sys.stdout (saída padrão – a tela). |
| flush | Valor booleano que especifica se a saída é eliminada (True) ou gravada em buffer (False). O padrão é False. |

```
nome = "Marcos"
sobrenome = "Pinheiro"
print(nome)
print(nome, sobrenome)
print(nome, sobrenome, sep="/")
print(nome, sobrenome, end="...\n")
print (sobrenome, end="...")
print(nome)

>>>Marcos
Marcos Pinheiro
Marcos/Pinheiro
Marcos Pinheiro...
Pinheiro...Marcos
```
# 5. Operadores
## 5.1 - Operadores Aritméticos (Aula5.py)
### 5.1.1 - Soma, Subtração e Multiplicação

Usados como já estamos habituados: soma (+), subtração (-), multiplicação (*).

```
print(3 + 5)
>>>8

print(9 - 4)
>>>5

print(3 * 5)
>>>15
```
### 5.1.2 - Divisão e Divisão inteira
A divisão, como vimos anteriormente pode ser usada de forma simples (/) ou pegando apenas a parte inteira da divisão (//)

```
print(3 / 2)
>>>1.5

print(3 // 2)
>>>1
```
### 5.1.3 - Módulo (Resto da Divisão)
Módulo: chamamos de módulo o resto da divisão comum. Exemplo: 10 / 3 dá como resultado **inteiro** 3 e resto 1

```
print(10 // 3)
>>>3
print(10 % 3)
>>>1

print(5 // 3)
>>>1
print(5 % 3)
>>>2
```
### 5.1.4 - Exponenciação
Exponenciação: para fazer operações de exponenciação, usamos (**) como operador em python.

```
print(2**3)
>>>8

print(4**2)
16
```

Precedência dos operadores: Seguindo as regras matemáticas, existe uma ordem na resolução dos cálculos que deve ser seguida para que seja feita de forma correta. A ordem de precedência é:

- Parênteses
- Exponenciais
- Multiplicações e Divisões (da esquerda para direita)
- Somas e Subtrações (da esquerda para direita)

O python segue essa mesma regra

```
print(10 - 5 *2)
>>>0

print((10 - 5) * 2)
>>>10

print(10 ** 2 / 2)
>>>50.0
```

## 5.2 - Operadores de Comparação (Aula6.py)

São usados para comparar dois valores.

### 5.2.1 - Igualdade
Compara se os valores são iguais. Usa-se o operador (==). A resposta do terminal será um valor booleano (*True* se verdadeiro, *False* se falso).

```
saldo = 1000
saque = 700
print(saque == saldo)

>>>False
```

### 5.2.2 - Diferença
Compara se os valores são diferentes. Usa-se o operador (!=). A resposta do terminal será um valor booleano (*True* se verdadeiro, *False* se falso).

```
saldo = 1000
saque = 700
print(saque != saldo)

>>>True
```

### 5.2.3 - Maior que / Maior ou igual
Compara se o primeiro valor é maior (ou maior ou igual) ao segundo valor. Usa-se o operador (>) para maior e o operador (>=) para maior ou igual. A resposta do terminal será um valor booleano (*True* se verdadeiro, *False* se falso).

```
saldo = 1000
saque = 700
print(saque > saldo)
>>>False

print(saque > saldo)
>>>False
```

### 5.2.4 - Menor que / Menor ou igual
Compara se o primeiro valor é menor (ou menor ou igual) ao segundo valor. Usa-se o operador (<) para menor e o operador (<=) para menor ou igual. A resposta do terminal será um valor booleano (*True* se verdadeiro, *False* se falso).

```
saldo = 1000
saque = 700
print(saque < saldo)
>>>True

print(saque < saldo)
>>>True
```

## 5.3 - Operadores de Atribuição (Aula7.py)
São utilizados para atribuir o valor inicial ou sobrescrever o valor de uma variável

### 5.3.1 - Atribuição Simples
Usa-se o operador (=) para atribuir o valor a uma variável
```
saldo = 500
print(saldo)
>>>500
```
### 5.3.2 - Atribuição com operadores matemáticos
É possível utilizar os operadores matemáticos vistos anteriormente para modificar o valor de uma variável já atribuida.

Usa-se o operador (+=) para somar um valor a uma variável.

```
saldo = 500
saldo += 200
print(saldo)
>>>700
```
Usa-se o operador (-=) para subtrair um valor a uma variável.

```
saldo = 500
saldo -= 200
print(saldo)
>>>300
```
Usa-se o operador (*=) para multiplicar um valor a uma variável.

```
saldo = 500
saldo *= 2
print(saldo)
>>>1000
```
E assim por diante, com os operadores já vistos

## 5.4 - Operadores Lógicos (Aula8.py)
São operadores utilizados em conjunto com operadores de comparação, formando uma expressão. Como o resultado do comparador é um booleano, é possível montar uma expressão do tipo:

Op_comparação + Op_lógico + Op_comparação etc...
### 5.4.1 Operador E
Usa-se o operador (and) quando as comparações devem ser atendidas (True) concomitantemente (ao mesmo tempo)

```
saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)
>>>True

print(saque<=limite)
>>>False

op_e = saldo >= saque and saque <= limite
print(op_e)
>>>False
```
Perceba que para que a variável **op_e** seja verdadeira (True), ambas as comparações (saldo >= saque) e (saque <= limite) devem ser verdadeiras. Como uma delas é falsa, o resultado do operador lógico E também é falso. Vamos trocar o valor da variável saque para 50 e ver o que acontece:
```
saldo = 1000
saque = 50
limite = 100

print(saldo >= saque)
>>>True

print(saque<=limite)
>>>True

op_e = saldo >= saque and saque <= limite
print(op_e)
>>>True
```
### 5.4.2 - Operador Ou
Ao contrário do operador e, que ambas as comparações (afirmações) necessitavam ser verdadeiras para que ele retornasse verdadeira, o operador **OU** (or) basta que uma delas (ou ambas) seja verdadeira para que ele também seja.
Assim, o operador OU só retornará *False* se ambas as comparações (afirmações) forem falsas.

```
aldo = 1000
saque = 200
limite = 100

print(saldo >= saque)
>>>True

print(saque<=limite)
>>>False

op_ou = saldo >= saque or saque <= limite
print(op_ou)
>>>True
```
### 5.4.3 - Operador de Negação
O operador de negação (not) é usado para inverter o resultado de um booleano. Transforma um *True* em *False* e vice-versa.

```
saldo = 1000
saque = 200
limite = 100

op_e = saldo >= saque and saque <= limite
print(op_e)
>>>False
print(not op_e)
>>>True

op_ou = saldo >= saque or saque <= limite
print(op_ou)
>>>True
print(not op_ou)
>>>False
```
### 5.4.4 - Parênteses
Assim como nas operações matemáticas, o parênteses também é utilizado nos operadores lógicos para estabelecer a precedência de operação, qual será feito antes.

```
saldo = 1000
saque = 200
limite = 100
conta_especial = True

a = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(a)

>>>True

b = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(b)
>>>True
```

## 5.5 - Operadores de Identidade (Aula9.py)
Usa-se o operador (is) para comparar se dois objetos ocupam a mesma posição na memória.
```
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is limite)
```
## 5.6 - Operadores de Associação (Aula10.py)
Os operadores (in) e (not in) são usados para verificar se um objeto está presente em uma sequência ou não. O resultado também é um booleano.

```
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

print("Python" in curso)
>>>True

print("maçã" not in frutas)
>>>True

print(200 in saques)
>>>False
```
# 6. Indentação e Blocos (Aula11.py)

Indentação é uma forma de manter o código mais legível e de fácil manutenção. É feita por meio de "parágrafos" ou espaçamentos, de forma a facilitar a identificação dos blocos de código. 

Porém, em Python, existe um segundo papel pois é através da indentação que o interpretador consegue determinar onde um bloco de comandos inicia e onde termina.

Por convenção, é indicado utilizar 4 espaços em branco para cada nível de indentação.
```
def sacar(self, valor:float)  None: # início do bloco do método
    
    if self.saldo >= valor: # início do bloco do if
       
        self.saldo -= valor

    # fim do bloco do if
    
# fim do bloco do método
```
# 7. Estruturas Condicionais e de Repetição

## 7.1 Estruturas Condicionais (Aula12.py)

São estruturas que permitem o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

### 7.1.1 - If
Para estruturas simples, com um único desvio, podemos utilizar o comando *if*. O comando testará a expressão e, caso o retorno seja verdadeiro, irá executar as ações presentes no bloco de código *if*

```
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
if saldo < saque:
    print("Saldo insuficiente!")

>>>Informe o valor do saque: 500
>>>Realizando saque!

>>>Informe o valor do saque: 2500
>>>Saldo insuficiente!
```

### 7.1.2 - If / else
Para criar uma estrutura condicional com dois desvios (como no exemplo acima, em que cada if era um desvio), podemos utilizar os comandos *if* e *else*.

Se o teste lógico for verdadeiro, o código irá executar o comando *if*. Se for falso, executará o *else*.

Dessa forma, podemos reescrever o código anterior da seguinte forma:

```
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")

>>>Informe o valor do saque: 500
>>>Realizando saque!

>>>Informe o valor do saque: 2500
>>>Saldo insuficiente!
```

### 7.1.3 - If / elif / else

Caso seja necessário mais de dois desvios, podemos usar o comando *elif* (*else if*). O elif é outra expressão lógica, que será testada e caso verdadeira, o bloco *elif* será executado.

Não exite um número máximo de *elifs* que podemos utilizar, porém é recomendado evitar criar grandes estruturas condicionais, pois aumentam a complexidade do código.

```
opcao = int(input("Informe uma opção: \n [1] Sacar \n [2] Extrato"))

if opcao == 1:
    valor = float(input("Informe o valor do saque: "))
    # Continua o código como no exemplo anterior
elif opcao == 2:
    print("Exibindo o extrato ...")
else:
    print("Opção inválida")
```

### 7.1.4 - If Aninhado (Aula13.py)
É possível criar estruturas condicionais dentro de um bloco condicional já existente. Esse tipo de estrutura é chamada de if aninhado.

```
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
```

### 7.1.5 - If Ternário (Aula14.py)
*If ternário* é um modo de escrever uma condição em uma única linha de código.

Ele é composto por três partes:
- o retorno caso a expressão seja verdadeira;
- a expressão lógica;
- o retorno caso a expressão seja falsa.

```
status = "Sucesso" if saldo >= saque else "falha"
```

## 7.2 Estruturas de repetição

São utilizadas para repetir um trecho de um código por um determinado número de vezes.

Esse número pode ser conhecido previamente ou determinado por meio de uma experssão lógica.

### 7.2.1 - For (Aula15.py)
O comando *for* é mais usado quando sabemos exatamente quantas vezes  o bloco de código deve ser executado, ou quando queremos percorrer um objeto iterável (lista). 
```
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="\n")
else:
    print("fim do código")
```
<sub>Obs: o *else* no *for* não é obrigatório, mas pode ser colocado para executar uma ação ao final das repetições do *for*</sub>

### 7.2.2 - Range (Aula16.py)
A range é uma das funções *built-in* do Python. Ela é utilizada para produzir uma sequência de números inteiros a partir de um início (inclusive) para um fim (exclusive). Se usarmos range(i,j), será produzida uma sequência:
i, i+1, i+2, ..., j-1

Ela recebe três argumentos:
- stop (obrigatório);
- start (opcional);
- step (opcional)

```
a = range(5)
print(a)
>>>range(0, 5)

b = list(range(5))
print(b)
>>>[0, 1, 2, 3, 4]

for numero in range(0,11):
    print(numero, end=" ")
else:
    print()

>>>0 1 2 3 4 5 6 7 8 9 10

for numero in range(0, 51, 5):
    print(numero, end=" ")

>>>0 5 10 15 20 25 30 35 40 45 50

```

### 7.2.3 - While (Aula17.py)
O comando *while* é utilizado para repetir um bloco de código várias vezes. Faz sentido utilizar o *while* quando não sabemos o número exato de veses que o bloco de código será repetido.

```
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n [2] Extrato \n [0] Sair \n"))

    if opcao == 1:
        print("sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado! Volte sempre")
```
Observe que, neste código, enquando o *input* não for 0, o while continua rodando o código. Observe também que é possível usar o *else* no comando *while*, porém assim como no *for* ele não é obrigatório.

## 7.3 - Break e Continue (Aula18.py)
### 7.3.1 - Break
O *break* é um comando especial no python, usado para parar a execução de um código. Ele é bastante utilizado junto com *while* e *for* quando determinada condição é estabelecida

```
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)
```
No exemplo de código acima, o *while* continuará rodando, a não ser que o usuário digite o número 10. Enquanto essa condição não for satisfeita, o código continuará rodando.

Outro exemplo:
```
for numero in range(100):
    if numero == 22:
        break
    print(numero, end=" ")
```
Até que a contagem chegue em 22, o *for* continuará sendo executado e mostrando em qual número está.

### 7.3.2 - Continue
O comando *continue* é usado quando uma determinada condição deva ser ignorada em comandos continuos.

```
for numero in range(100):
    if numero == 12:
        continue
    print(numero, end=" ")

>>>0 1 2 3 4 5 6 7 8 9 10 11 13 14 15 16...
```

Perceba que no código acima, o número 12 foi "pulado" e não executou o comando do *for*.

# 8. Strings e Fatiamentos
## 8.1 - Métodos Utéis das String (Aula19.py)
### 8.1.1 - Maiúsculas, Minúsculas e Títulos
| Método | Comando |
|---|---|
| Maiúsculo | [variável].upper() |
| Minúsculo | [variável].lower() |
| Primeira Letra Maiúscula | [variável].title() |

```
curso = "pYtHoN"
print(curso.upper())
>>>PYTHON

print(curso.lower())
>>>python

print(curso.title())
>>>Python
```
### 8.1.2 - Eliminando espaços em branco

| Método | Comando |
|---|---|
| No início e no final | [variável].strip() |
| No início (esquerda) | [variável].lstrip() |
| No final (direita) | [variável].rstrip() |

```
curso2 = "    Python  "
print(curso2.strip())
>>>"Python"

print(curso2.lstrip())
>>>"Python  "

print(curso2.title())
>>>"    Python"

```

### 8.1.3 - Junções e Centralizações
| Método | Comando |
|---|---|
| Centralização com caractere | [variável].center([nº de caracteres total], [Caracter a ser usado antes e depois]) |
| Inserir caracter entre os já existentes na string | "[caracter]".join(variável) |

```
curso3 = "Python"
print(curso3.center(10,"*"))
>>>**Python**

print("-".join(curso3))
>>>P-y-t-h-o-n
```

## 8.2 - Interpolação de Variáveis (Aula20.py)
Existem três formas de interpolar variáveis em strings:
- A primeira é com o sinal " % "
- A segunda é utilizando o método format
- A terceira é utilizando f strings

### 8.2.1 - Usando o %

Apesar de não ser atualmente recomendada e seu uso em Python 3 ser raro, ela é utilizada usando o sinal % na sting onde ela será inserida (%s para strings, %d para integer e %f para floats) conforme o exemplo:

```
nome = "Marcos"
idade = 33
profissao = "Programador"
linguagem = "Python"

print("Olá! Me chamo %s. Tenho %d anos e trabalho como %s especialista em %s" %(nome, idade, profissao, linguagem))

>>>Olá! Me chamo Marcos. Tenho 33 anos e trabalho como Programador especialista em Python

```

### 8.2.2 - Usando o format
É semelhante ao %, porém usa-se {} lugar da %. 
Uma vantagem desse método é a possibilidade de mudar a ordem das variáveis, desde que se defina em qual ordem elas aparecerão na sting final.

```
nome = "Marcos"
idade = 33
profissao = "Programador"
linguagem = "Python"

pessoa = {"nome": "Thais", "idade": 30, "profissao": "autônomo", "linguagem": "cosméticos"}

print("Olá! Me chamo {}. Tenho {} anos e trabalho como {} especialista em {}".format(nome, idade, profissao, linguagem))
>>>Olá! Me chamo Marcos. Tenho 33 anos e trabalho como Programador especialista em Python

print("Olá! Me chamo {2}. Tenho {3} anos e trabalho como {1} especialista em {0}".format(linguagem, profissao, nome, idade))
>>>Olá! Me chamo Marcos. Tenho 33 anos e trabalho como Programador especialista em Python

print("Olá! Me chamo {nome}. Tenho {idade} anos e trabalho como {profissao} especialista em {liguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
>>>Olá! Me chamo Marcos. Tenho 33 anos e trabalho como Programador especialista em Python

print("Olá! Me chamo {nome}. Tenho {idade} anos e trabalho como {profissao} especialista em {liguagem}".format(**pessoa))
#[**pessoa é um dicionário no python. Ele deve ser definido antes de rodar o código]
>>>Olá! Me chamo Thais. Tenho 30 anos e trabalho como autônomo especialista em cosméticos

```
### 8.2.3 - Usando o f string

Funciona da mesma forma, porém a maior vantagem é não definir as variáveis usadas na string ao final, como os métodos anteriores.
Nesse, as varíaveis já são discriminadas na própria string final.

```
nome = "Marcos"
idade = 33
profissao = "Programador"
linguagem = "Python"

print(f"Olá! Me chamo {nome}. Tenho {idade} anos e trabalho como {profissao} especialista em {linguagem}")
>>>Olá! Me chamo Marcos. Tenho 33 anos e trabalho como Programador especialista em Python
```

### 8.2.4 - Formatando strings com f-string

É possivel formatar como as variáveis serão apresentadas na string usando o f-string.
Por exemplo, definimos PI = 3.141592 e queremos apenas 2 casas decimais. Usamos o f-string e na variável definimos [variável: [casas totais do número].[casas decimais][tipo da váriavel]]
No 1º exemplo, não foi definido um número de casas total e 2 casas decimais do tipo float (f).
Já no segundo, foi definido que o número teria 10 casas, sendo duas decimais.

```
PI = 3.141592

print(f"Valor de PI: {PI:.2f}")
>>>Valor de PI: 3.14

print(f"Valor de PI: {PI:10.2f}")
>>>Valor de PI:       3.14
```
## 8.3 - Fatiamento de Strings (Aula21.py)

É uma técnica utilizada para retornar substrings (partes da string original), informando o início, fim e passo [start, stop, step]

```
nome = "Marcos Pinheiro dos Santos Neto"

print(nome[0])
>>>M

print(nome[:6])
>>>Marcos

print(nome[7:])
>>>Pinheiro dos Santos Neto

print(nome[7:15])
>>>Pinheiro

print(nome[7:15:2])
>>>Pner

print(nome[:])
Marcos Pinheiro dos Santos Neto

print(nome[::-1]) #truque para inverter a ordem
>>>oteN sotnaS sod oriehniP socraM

print(nome[5::-1])
>>>socraM

print(nome[14:6:-1])
>>>oriehniP
```
## 8.4 - String em Multiplas Linhas (Aula22.py)

Strings de multiplas linhas são definidas informando 3 aspas simples ou duplas durante a atribuição. Elas podem ocupar várias linhas do código e todos os espaços em brando são incluídos na string final.

```
nome = "Marcos"

mensagem = f"""
Olá! Meu nome é {nome}.
Estou aprendendo Python na prática!
"""

mensagem2 = f'''
    Olá! Meu nome é {nome}.
Estou aprendendo Python na prática!
        Exemplo de espaçamentos diferentes
'''

print(mensagem)
>>>Olá! Meu nome é Marcos.
Estou aprendendo Python na prática!

print(mensagem2)
>>>    Olá! Meu nome é Marcos.
Estou aprendendo Python na prática!       
        Exemplo de espaçamentos diferentes
```

# 9. Listas
Listas em Pythns podem armazenar de maneira sequencial qualquer tipo de objeto. Podemos criar listas utilizando o construtor *list*, a função *range* ou colocando valores separados por virgula dentro de colchetes []. Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.
Exemplos: 

frutas = ["laranja", "maca", "uva"]

frutas = []  **lista vazia**

letras = list("python") **cada letra da palavra é um elemento da lista**

numeros = list(range(10))  **cada número da range de 0 a 9 é um elemento da lista**

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True] **lista de atributos do carro. Cada elemento (apesar de serem de tipos diferentes), são elementos da lista carro**

A lsita é uma sequência, ou seja, podemos acessar seus dados usando os índices, iniciando em zero.

```
frutas = ["laranja", "maca", "uva"]

print(frutas[0])
>>>laranja

print(frutas[1])
>>>maca

print(frutas[2])
>>>uva
```

Podemos também usar índices negativos. O índice -1 seria o último elemento da lista, por exemplo.

```
frutas = ["laranja", "maca", "uva"]

print(frutas[-1])
>>>uva

print(frutas[-2])
>>>maca

print(frutas[-3])
>>>laranja
```

## 9.1 - Listas Aninhadas
Como em Python as listas são objetos, isso significa que uma lista consegue armazenar outra lista. Com isso, podemos criar estruturas bidimensionais (tabelas), e acessar dados informando os índices de linha e coluna.

```
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"],
]

print(matriz[0])
>>>[1, 'a', 2]

print(matriz[0][0])
>>>1

print(matriz[0][-1])
>>>2

print(matriz[-1][-1])
>>>c

```

## 9.2 - Fatiamento
Assim como vimos nas stings, podemos fatiar as listas em sublistas, derivadas da lista inicial. A técnica é a mesma, usando os índices de elementos das lsitas:

```
lista = list("python")
print(lista)
>>> ['p', 'y', 't', 'h', 'o', 'n']

print(lista[2:])
>>>['t', 'h', 'o', 'n']

print(lista[:2])
>>>['p', 'y']

print(lista[1:3])
>>>['y', 't']

print(lista[0:3:2])
>>>['p', 't']

print(lista[::])
>>>['p', 'y', 't', 'h', 'o', 'n']

print(lista[::-1])
>>>['n', 'o', 'h', 't', 'y', 'p']

```

## 9.3 - Iterar Listas

A forma mais comum de iterar (percorrer) os dados de uma lista é utilizando o comando *for*

```
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

>>>gol
celta
palio
```
## 9.4 - Função *enumerate*

Às vezes, é necessário saber qual o índice do objeto dentro do laço *for*. Para isso, podemos usar a função *enumerate*.

```
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

>>>0: gol
1: celta
2: palio
```
## 9.5 - Compreensão de listas (Aula24.py)

A compreensão de lista oferece uma sintaxe mais curta quando você deseja criar uma nova lsita com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

Observe o seguinte código. Ele separa os números pares da lista numeros em outra lista (pares)
```
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)
>>>[30, 2, 34]
```
Usando a compreensão de listas, isso pode ser feito de outra forma, com menos código e mais rápida:

```
numeros = [1, 30, 21, 2, 9, 65, 34]

pares2 = [numero for numero in numeros if numero % 2 == 0]
print(pares2)
>>>[30, 2, 34]
```

Outro exemplo:

```
numeros = [1, 30, 21, 2, 9, 65, 34]

quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)
>>>[1, 900, 441, 4, 81, 4225, 1156]

quadrado2 = [numero **2 for numero in numeros]
print(quadrado2)
>>>[1, 900, 441, 4, 81, 4225, 1156]

```

## 9.6 - Métodos da classe list (Aula25.py)

### 9.6.1 - Append
Usado para adicionar elementos a uma lista.

Estrutura: [lista].append([novo elemento])
```
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)
>>>[1, 'Python', [40, 30, 20]]
```
### 9.6.2 - Clear
Usado quando se quer limpar uma lista existente

Estrutura: [lista].clear()
```
lista = [1, 'Python', [40, 30, 20]]

lista.clear()

print(lista)
>>>[]
```

### 9.6.3 - Copy
Copia uma lista existente em outra lista determinada. (Faz uma cópia da lista original)

Estrutura: [lista].copy()

```
lista = [1, 'Python', [40, 30, 20]]

l2 = lista.copy()

print(l2)
>>>[1, 'Python', [40, 30, 20]]

```
### 9.6.4 - Count
Usado para contar quantas vezes um determinado objeto aparece na lista

Estrutura: [lista].count([objeto])

```
cores = ["vermelho", "azul", "verde", "azul"]
print(cores.count("vermelho"))
>>>1

print(cores.count("verde"))
>>>1

print(cores.count("azul"))
>>>2
```

### 9.6.5 - Extend
Usado para juntar duas listas. Esse método não elimina valores duplicados

Estrutura: [lista].extend([valores])

```
lista = [1, 'Python', [40, 30, 20]]
l2 = lista.copy()

lista.extend(["java", "csharp"])
print(lista)
>>>[1, 'Python', [40, 30, 20], 'java', 'csharp']

lista.extend(l2)
print(lista)
>>>[1, 'Python', [40, 30, 20], 'java', 'csharp', 1, 'Python', [40, 30, 20]]

```
A diferença entre o *extend* e o *append* é que o *append* é usado para elementos individuais, isolados, enquando o *extend* é usado para listas inteiras.

### 9.6.6 - Index

Usado para encontrar a posição da primeira ocorrência do elemento buscado na lista.

Estrutura: [lista].index([elemento])

```
lista = [1, 'Python', [40, 30, 20], 'java', 'csharp', 1, 'Python', [40, 30, 20]]

print(lista.index("Python"))
>>>1

print(lista.index("java"))
>>>3

print(lista.index(1))
>>>0

```

### 9.6.7 - Pop

Retira o elemento da lista pelo índice designado no argumento. Se não for designado o índice, retira o último elemento da lista.

Estrutura: [lista].pop[índice]

```
lista = [1, 'Python', [40, 30, 20], 'java', 'csharp', 1, 'Python', [40, 30, 20]]

lista.pop()
print(lista)
>>>[1, 'Python', [40, 30, 20], 'java', 'csharp', 1, 'Python']

lista.pop(2)
print(lista)
>>>[1, 'Python', 'java', 'csharp', 1, 'Python']

```

### 9.6.8 - Remove

Retira a primeira ocorrência do elemento designado da lista. Difere do *pop* pois o argumento no *remove* é o próprio objeto a ser removido, e não o índice dele na lista.

Estrutura: [lista].remove([objeto])

```
lista = [1, 'Python', 'java', 'csharp', 1, 'Python']

lista.remove("java")
print(lista)
>>>[1, 'Python', 'csharp', 1, 'Python']

lista.remove("Python")
print(lista)
>>>[1, 'csharp', 1, 'Python']
```

### 9.6.9 - Reverse
Inverte a ordem dos elementos da lista (espelhamento).

Estrutura: [lista].reverse()

```
lista = [1, 'csharp', 1, 'Python']

lista.reverse()
print(lista)
>>>['Python', 1, 'csharp', 1]
```

### 9.6.10 - Sort
Ordena a lista conforme o argumento. Caso não seja dado nenhum argumento, a ordem será alfabética/numérica. A lista deve conter elementos do mesmo tipo.

Estrutura: [lista].sort([argumento])

Argumentos possíveis:
- reverse (True/False)
- key (função específica)

```
linguagens = ["python", "js", "c", "java", "csharp"]
numeros = [1, 45, 32, 98, 65, 48, 27]

linguagens.sort()
print(linguagens)
>>>['c', 'csharp', 'java', 'js', 'python']

numeros.sort()
print(numeros)
>>>[1, 27, 32, 45, 48, 65, 98]

linguagens.sort(reverse=True)
print(linguagens)
>>>['python', 'js', 'java', 'csharp', 'c']

numeros.sort(reverse=True)
print(numeros)
>>>[98, 65, 48, 45, 32, 27, 1]
```

No exemplo a seguir, a organização será por tamanho da palavra. Nesse caso usou-se uma função anônima *lambda* definida por len(x) - (*lenght*, tamanho, comprimento).
As funções serão vistas em detalhes mais adiante.

```
linguagens.sort(key=lambda x: len(x))

>>>['c', 'js', 'java', 'python', 'csharp']

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)
>>>['python', 'csharp', 'java', 'js', 'c']
```
## 9.7 - Funções *Built-in* em listas (Aula26.py)
### 9.7.1 - Len
Tivemos um *spoiler* no item anterior, mas o *len* é usado para saber o tamanho da lista, isto é, quantos elementos tem na lista.

Estrutura: len([lista])

```
linguagens = ['python', 'csharp', 'java', 'js', 'c']

print(len(linguagens))
>>>5
```
### 9.7.2 - Sorted
Ordena os elementos da lista, de forma parecida como vimos nos métodos.

Estrutura: sorted([lista],[argumentos])

```
linguagens = ['python', 'csharp', 'java', 'js', 'c']

print(sorted(linguagens))
>>>['c', 'csharp', 'java', 'js', 'python']
print(linguagens)
>>>['python', 'csharp', 'java', 'js', 'c']
```
Perceba que, ao contrário do método (que organiza a lista), a função executa apenas para aquele momento, não mexendo a lista original.

```
print(sorted(linguagens, key=lambda x: len(x)))
>>>['c', 'js', 'java', 'python', 'csharp']

print(sorted(linguagens, key=lambda x: len(x), reverse=True))
>>>['python', 'csharp', 'java', 'js', 'c']
```

# 10. Tuplas (Aula27.py)

Tuplas são estruturas muito parecidas com as listas. A principal diferença é que as tuplas são imutáveis, enquanto as listas são mutáveis.

Podemos crias tuplas através da classe *tuple*, ou colocando valores dentro de parênteses (), separados por vírgulas.

Exemplo

```
frutas = ("laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil", )

```
Boas práticas: para diferenciar uma tupla de uma ordem de precedência, por exemplo, é uma praxe colocar uma vírgula ao final dos elementos do tupla (como no exemplo acima, em frutas e em pais).

A tupla é uma sequência. Para acessar os elementos da tupla, utilizamos os índices, começando em zero, assim como nas listas. Também é possível utilizar indexadores negativos.

```
tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[1])
>>>y

print(tupla[4])
>>>o

print(tupla[-1])
>>>n
```

Novamente, assim como as listas, é possível fazer tuplas aninhadas, criando assim estruturas bidimensionais (tabelas e matrizes).

```
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)
```

Assim como as listas, as tuplas também podem ser fatiadas da mesma forma. Basta passar o índice de início, fim e o *step* para fazê-lo.

```
tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])
>>>('t', 'h', 'o', 'n')

print(tupla[:3])
>>>('p', 'y', 't')

print(tupla[1:3])
>>>('y', 't')

print(tupla[0:5:2])
>>>('p', 't', 'o')

print(tupla[::])
>>>('p', 'y', 't', 'h', 'o', 'n')

print(tupla[::-1])
>>>('n', 'o', 'h', 't', 'y', 'p')
```

Apenas a título de curiosidade, quando se tenta alterar uma tupla aparece o seguinte erro:

```
tup = (1, 3)
tup[0] = 2

>>>TypeError: 'tuple' object does not support item assignment
```

As iterações e enumerações também são iguais as listas.

## 10.1 - Métodos da classe *tuple* (Aula28.py)

No geral, funcionam iguais aos métodos de lista. Porém, como as tuplas são imutáveis, temos menos métodos.

### 10.1.1 - Count
[tupla].count([elemento])
```
cores = ("vermelho", "azul", "verde", "azul")

print(cores.count("vermelho"))
>>>1

print(cores.count("verde"))
>>>1

print(cores.count("azul"))
>>>2
```

### 10.1.2 - Index
[tupla].index([elemento])

```
linguagens = ("python", "js", "c", "java", "csharp", )

print(linguagens.index("java"))
>>>3

print(linguagens.index("python"))
>>>0
```
## 10.1.3 - Função Len em tuplas
len([tupla])

```
linguagens = ("python", "js", "c", "java", "csharp", )

print(len(linguagens))
>>>5
```

