"""2. Encontrar o Maior e o Menor Número
Escreva um programa que leia uma lista de números digitados pelo usuário e
determine o maior e o menor número presentes na lista."""


entrada = input("Digite uma lista de números, separados por espaço: ")

numeros = [float(num) for num in entrada.split()]

if numeros:
    
    maior = max(numeros)
    menor = min(numeros)

    print("O maior número é:", maior)
    print("O menor número é:", menor)
else:
    print("A lista está vazia. Por favor, digite alguns números.")
