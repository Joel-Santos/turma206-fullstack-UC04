#Questão 01 - Calcular o ano de nascimento a partir da idade e do ano atual
idade = int(input("Digite sua idade: "))
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = ano_atual - idade
print(f"Você nasceu no ano de {ano_nascimento}.")

# Questão 02 - Verifica se um número é par ou ímpar
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# Questão 03 - Verifica se dois números são múltiplos entre si
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if a % b == 0 or b % a == 0:
    print("São Múltiplos")
else:
    print("Não são Múltiplos")

# Questão 04 - Verifica se um número é primo
numero = int(input("Digite um número: "))
eh_primo = True  # Assumimos que o número é primo
for i in range(2, numero):
    if numero % i == 0:
        eh_primo = False
        break
if eh_primo and numero > 1:
    print("É primo.")
else:
    print("Não é primo.")

# Questão 05 - Classifica a temperatura como frio, ameno ou quente
temperatura = float(input("Digite a temperatura: "))
if temperatura < 15:
    print("Clima frio.")
elif 15 <= temperatura <= 30:
    print("Clima ameno.")
else:
    print("Clima quente.")

# Questão 06 - Aplica desconto de 10% para compras acima de R$100
valor = float(input("Digite o valor da compra: "))
if valor > 100:
    valor *= 0.9  # Aplica o desconto
print(f"Valor final: R${valor:.2f}")

# Questão 07 - Exibe os 100 primeiros números naturais em ordem crescente
for i in range(1, 101):
    print(i, end=" ")

# Questão 08 - Exibe os 200 primeiros números naturais em ordem decrescente
for i in range(200, 0, -1):
    print(i, end=" ")

# Questão 09 -  Soma as idades até que o usuário digite 0
soma = 0
while True:
    idade = int(input("Digite uma idade (ou 0 para parar): "))
    if idade == 0:
        break
    soma += idade
print(f"Soma total das idades: {soma}")


# Questão 10 - Contar o número de palavras em uma frase
frase = input("Digite uma frase: ")
palavras = frase.split()  # Divide a frase em palavras
print(f"Número de palavras: {len(palavras)}")

# Questão 11 - Cadastrar produtos com nome, preço e quantidade
produtos = []
while True:
    nome = input("Digite o nome do produto (ou 'sair' para parar): ")
    if nome == "sair":
        break
    preco = float(input("Digite o preço: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})
print("Produtos cadastrados:", produtos)

# Questão 12 - Valida se o CPF tem 11 dígitos numéricos
cpf = input("Digite o CPF: ")
if len(cpf) == 11 and cpf.isdigit():
    print("CPF válido.")
else:
    print("CPF inválido.")

# Questão 13 - Soma os números pares digitados até que o usuário insira 0
soma = 0
while True:
    numero = int(input("Digite um número (ou 0 para parar): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        soma += numero
print(f"Soma dos números pares: {soma}")


# Questão 14 - Sorteia um nome entre os informados pelo usuário
import random
nomes = []
while True:
    nome = input("Digite um nome (ou 'sair' para parar): ")
    if nome == "sair":
        break
    nomes.append(nome)
if nomes:
    print(f"Nome sorteado: {random.choice(nomes)}")
else:
    print("Nenhum nome foi cadastrado.")


# Questão 15 - Valida se a senha tem pelo menos 8 caracteres e contém números
senha = input("Digite a senha: ")
if len(senha) >= 8 and any(char.isdigit() for char in senha):
    print("Senha válida.")
else:
    print("Senha inválida.")

# Questão 16 - Calcula a média das notas cadastradas
notas = []
while True:
    nota = input("Digite uma nota (ou 'sair' para parar): ")
    if nota == "sair":
        break
    notas.append(float(nota))
if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota foi cadastrada.")

# Questão 17 - Conta o número de vogais em uma palavra
palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"  # Lista de vogais
contagem = sum(1 for letra in palavra if letra in vogais)
print(f"Número de vogais: {contagem}")


# Questão 18 - Verifica se um número é perfeito
numero = int(input("Digite um número: "))
soma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
if soma_divisores == numero:
    print("Número Perfeito")
else:
    print("Não é Perfeito")


# Questão 19 - Calcula o produto dos números de uma lista
numeros = list(map(int, input("Digite os números separados por espaço: ").split()))
produto = 1
for num in numeros:
    produto *= num
print(f"Produto dos números: {produto}")


# Questão 20 - Busca nomes que contenham uma palavra específica
nomes = []
while True:
    nome = input("Digite um nome (ou 'sair' para parar): ")
    if nome == "sair":
        break
    nomes.append(nome)
palavra = input("Digite uma palavra para buscar: ")
resultado = [nome for nome in nomes if palavra in nome]
if resultado:
    print(f"Nomes que contêm '{palavra}': {resultado}")
else:
    print(f"Nenhum nome contém '{palavra}'.")
