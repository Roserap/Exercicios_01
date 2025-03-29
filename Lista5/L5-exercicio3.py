"""3. Cálculo da Média de uma Lista
Crie uma função que receba uma lista de números e retorne a média dos valores.
No programa principal, peça ao usuário para inserir os números e exiba a média
utilizando a função criada."""

def calcular_media(lista):
    
    if len(lista) == 0:
        return 0
    
    soma = sum(lista)
    
    media = soma / len(lista)
    return media

if __name__ == "__main__":
    numeros = []
    while True:
        entrada = input("Digite um número (ou 'sair' para finalizar): ")
        if entrada.lower() == 'sair':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, insira um número válido.")

    media = calcular_media(numeros)
    print(f"A média dos números inseridos é: {media}")
