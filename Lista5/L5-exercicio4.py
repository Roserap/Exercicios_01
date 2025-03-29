"""4. Contador de Vogais em uma Palavra
Crie uma função que receba uma palavra como parâmetro e retorne a quantidade
de vogais presentes nela. No programa principal, solicite uma palavra ao usuário e
utilize a função para exibir o número de vogais."""

def contar_vogais(palavra):
    
    vogais = "aeiouAEIOU"
    contador = 0
    
    for letra in palavra:
        if letra in vogais:
            contador += 1

    return contador

if __name__ == "__main__":
    palavra = input("Digite uma palavra: ")
    quantidade_vogais = contar_vogais(palavra)
    print(f"A quantidade de vogais na palavra '{palavra}' é: {quantidade_vogais}")
