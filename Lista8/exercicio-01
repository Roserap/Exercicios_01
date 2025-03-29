"""1. Divisão Segura
Crie um programa que solicite ao usuário dois números e realize a divisão do
primeiro pelo segundo. Utilize tratamento de exceções para evitar erros de
divisão por zero e erros de entrada inválida (como caracteres não numéricos)."""

def divisao_segura():
    while True:
        try:
            num1 = float(input("Digite o primeiro número (numerador): "))
            num2 = float(input("Digite o segundo número (denominador): "))
            
            resultado = num1 / num2
            print(f"O resultado da divisão de {num1} por {num2} é: {resultado:.2f}")
            break

        except ValueError:
            print("Erro: Por favor, insira apenas números válidos.")
        except ZeroDivisionError:
            print("Erro: Divisão por zero não é permitida. Por favor, insira um número diferente de zero para o denominador.")


if __name__ == "__main__":
    divisao_segura()
