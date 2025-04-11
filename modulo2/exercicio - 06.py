
try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    resultado = numero1 / numero2
    print(f"O resultado da divisão de {numero1} por {numero2} é: {resultado}")

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero. Por favor, insira um número diferente de zero para o segundo número.")

except ValueError:
    print("Erro: Você deve inserir apenas números. Por favor, tente novamente.")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
