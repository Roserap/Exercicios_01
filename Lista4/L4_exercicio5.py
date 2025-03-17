"""5. Contar Ocorrências de um Elemento
Escreva um programa que peça ao usuário para inserir uma lista de números e um
número específico. O programa deve contar quantas vezes esse número aparece
na lista."""

entrada = input("Digite uma lista de números, separados por espaço: ")

numeros = [int(num) for num in entrada.split()]

numero_especifico = int(input("Digite o número que deseja contar: "))

ocorrencias = numeros.count(numero_especifico)

print(f"O número {numero_especifico} aparece {ocorrencias} vez(es) na lista.")
