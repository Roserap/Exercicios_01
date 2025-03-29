"""4. Acesso a Elementos de uma Lista
Crie uma lista com cinco números e permita que o usuário informe um índice para
acessar um valor da lista. Utilize tratamento de exceções para evitar erros caso o
usuário digite um índice inválido."""

def acessar_elemento_lista():
    
    lista_numeros = [10, 20, 30, 40, 50]
    
    while True:
        try:
            indice = int(input("Digite um índice (0 a 4) para acessar um valor da lista: "))
            
            valor = lista_numeros[indice]
            print(f"O valor no índice {indice} é: {valor}")
            break
        except IndexError:
            print("Erro: Índice inválido. Por favor, digite um índice entre 0 e 4.")
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro.")


if __name__ == "__main__":
    acessar_elemento_lista()
