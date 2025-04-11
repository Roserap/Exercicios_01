
entrada = input("Digite uma lista de palavras separadas por espaço: ")

lista_palavras = entrada.split()

lista_ordenada = sorted(lista_palavras)

numero_palavras = len(lista_palavras)

palavras_maiusculas = [palavra.upper() for palavra in lista_palavras]

print("Lista ordenada alfabeticamente:", lista_ordenada)
print("Número total de palavras:", numero_palavras)
print("Palavras em maiúsculas:", palavras_maiusculas)
