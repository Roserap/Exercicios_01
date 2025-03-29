"""2. Verificação de Número Primo
Crie uma função que receba um número inteiro e retorne True se for primo e False
caso contrário. No programa principal, solicite um número ao usuário e utilize a
função para verificar se ele é primo."""

def eprimo(n):
    
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    numero = int(input("Informe um número inteiro para verificar se é primo: "))
    if eprimo(numero):
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
