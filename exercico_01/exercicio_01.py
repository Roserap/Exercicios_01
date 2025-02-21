"""1. Cálculo da Área do Círculo
Escreva um programa que peça ao usuário o valor do raio de um círculo e calcule sua área.
Use a fórmula:

Area = II X raio2
"""

import math

raio = float(imput("Digite o valor do raio: "))

area = math.pi * (raio ** 2)

print(f"A área do circulo com raio {raio} é: {area:.2f}")