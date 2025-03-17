"""4. Inverter a Lista
Escreva um programa que leia uma lista de palavras e exiba essa lista na ordem
inversa."""

entrada = input("Digite uma lista de palavras, separadas por espaço: ")

palavras = entrada.split()

palavras_invertidas = palavras[::-1]

print("Lista de palavras na ordem inversa:", palavras_invertidas)
