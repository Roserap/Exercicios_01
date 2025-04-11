def contar_vogais(frase):
    
    vogais = 'aeiouAEIOU'
    contagem = {vogal: 0 for vogal in vogais}
    
    for letra in frase:
        if letra in contagem:
            contagem[letra] += 1
            
    return contagem

def frase_invertida(frase):
    
    return frase[::-1]

def substituir_espacos(frase):
    
    return frase.replace(' ', '-')

frase_usuario = input("Digite uma frase: ")

contagem_vogais = contar_vogais(frase_usuario)
print("Contagem de vogais:")
for vogal, contagem in contagem_vogais.items():
    if contagem > 0:
        print(f"{vogal}: {contagem}")

frase_reversa = frase_invertida(frase_usuario)
print(f"Frase ao contrário: {frase_reversa}")

frase_substituida = substituir_espacos(frase_usuario)
print(f"Frase com espaços substituídos: {frase_substituida}")
