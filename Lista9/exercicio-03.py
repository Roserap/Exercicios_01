"""3. Conversão de Entrada com Exceções
Crie um programa que peça ao usuário para digitar um número inteiro. O programa
deve tentar converter a entrada e exibir o dobro desse número. Caso o usuário
digite um valor inválido, o programa deve exibir uma mensagem de erro e solicitar
a entrada novamente até que um número válido seja fornecido."""

def obter_numero_inteiro():
    while True:
        entrada = input("Digite um número inteiro: ")
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    numero_inteiro = obter_numero_inteiro()
    dobro = numero_inteiro * 2
    print(f"O dobro de {numero_inteiro} é: {dobro}")
