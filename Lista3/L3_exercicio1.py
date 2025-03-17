"""
1) Contagem Progressiva

Escreva um programa que peça um número inteiro positivo ao usuário e exiba todos os
números de 1 até esse número, um por linha.
"""

try:
    numero = int(input("Digite um número inteiro positivo: "))

    
    if numero > 0:
        
        for i in range(1, numero + 1):
            print(i)
    else:
        print("Por favor, digite um número inteiro positivo.")
except ValueError:
    print("Entrada inválida! Por favor, digite um número inteiro.")
