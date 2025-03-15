"""
1. Par ou Ímpar?
Escreva um programa que solicite um número inteiro ao usuário e informe se ele é par ou
ímpar.
"""

numero = int(input("Digite um numero "))
if numero % 2 == 0:
    print(f"O numero{numero} é par.")
else:
    print(f"O numero{numero} é impar.")
