"""1. Soma dos Elementos de uma Lista
Escreva um programa que solicite ao usuário uma lista de números inteiros e
calcule a soma de todos os elementos da lista."""



entrada = input("Digite uma lista de números inteiros, separados por espaço: ")

numeros = []
for num in entrada.split():
    numeros.append(int(num))

soma = sum(numeros)

print("A soma dos elementos da lista é:", soma)
