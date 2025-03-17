"""3. Remover Duplicatas
Escreva um programa que leia uma lista de números e remova os valores
duplicados, mantendo a ordem original."""

entrada = input("Digite uma lista de números, separados por espaço: ")

numeros = [int(num) for num in entrada.split()]

numeros_unicos = []

for num in numeros:
    if num not in numeros_unicos:
        numeros_unicos.append(num)

print("Lista sem duplicatas:", numeros_unicos)
