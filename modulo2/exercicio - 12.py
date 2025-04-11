
def multiplicador(fator):
    
    def multiplicar(numero):
        return numero * fator
    return multiplicar


fator = float(input("Digite um fator para multiplicação: "))

multiplica_por_fator = multiplicador(fator)

numero = float(input("Digite um número para multiplicar: "))

resultado = multiplica_por_fator(numero)

print(f"O resultado de {numero} multiplicado por {fator} é: {resultado}")
