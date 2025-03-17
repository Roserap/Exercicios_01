""""4. Números Ímpares em um Intervalo
Peça ao usuário dois números inteiros, representando um intervalo A,B. O programa deve
exibir todos os números ímpares dentro desse intervalo (inclusive os limites, se forem
ímpares)."
"""
a = int(input("Digite o primeiro número inteiro (A): "))
b = int(input("Digite o segundo número inteiro (B): "))


if a > b:
    a, b = b, a


print(f"Números ímpares no intervalo de {a} a {b}:")

for numero in range(a, b + 1):
    if numero % 2 != 0:
        print(numero)
