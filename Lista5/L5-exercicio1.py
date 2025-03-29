"""1. Cálculo do Fatorial
Crie uma função que receba um número inteiro como parâmetro e retorne o seu
fatorial. Em seguida, utilize essa função em um programa principal para calcular o
fatorial de um número informado pelo usuário."""

def fatorial(n):
    # O fatorial de 0 é 1
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Programa principal
if __name__ == "__main__":
    numero = int(input("Informe um número inteiro para calcular o fatorial: "))
    if numero < 0:
        print("Fatorial não é definido para números negativos.")
    else:
        resultado = fatorial(numero)
        print(f"O fatorial de {numero} é: {resultado}")
