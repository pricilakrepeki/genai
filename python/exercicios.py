# EX. 1: Hello World Personalizado
# Peça o nome do usuário e imprima uma mensagem de boas-vindas personalizada
# Exemplo: "Olá, André! Seja bem-vinda à Especialização em IA Generativa!"
nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Seja bem-vinda à Especialização em IA Generativa!")

# EX. 2: Calculadora de Soma
# Conceitos: Tipos numéricos, conversão de tipos
# Peça dois números ao usuário e mostre a soma deles
# Desafio: Mostre também a subtração, multiplicação e divisão
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print(f"Soma: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")
print(f"Divisão: {num1 / num2 if num2 != 0 else 'Erro: divisão por zero'}")

#EX. 3: Par ou Ímpar
#Conceitos: Operador "%" (módulo), condicionais "if/else"
# Peça um número ao usuário e diga se ele é par ou ímpar
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")

#EX. 4: Conversor de Temperatura
#Conceitos: Operações matemáticas, formatação de strings
# Converta Celsius para Fahrenheit: (C × 9/5) + 32
# Peça a temperatura em Celsius e mostre em Fahrenheit
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")

#EX. 5: Calculadora de Média
#Conceitos: Listas, "sum()", "len()"
# Peça 4 notas ao usuário e calcule a média
# Mostre se o aluno foi aprovado (média >= 7) ou reprovado
notas = []
for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)
media = sum(notas) / len(notas)
print(f"Média: {media:.2f}")
if media >= 7:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")

#EX. 6: Tabuada
#Conceitos: Loops "for", range
# Peça um número e mostre a tabuada dele (1 a 10)
# Exemplo:
# 5 x 1 = 5
# 5 x 2 = 10 ...
numero = int(input("Digite um número para ver sua tabuada: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#EX. 7: Números Primos
#Conceitos: Loops "while", lógica matemática
# Peça um número e diga se ele é primo ou não
# Um número primo só é divisível por 1 e por ele mesmo