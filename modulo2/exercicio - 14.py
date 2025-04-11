import struct

numeros = [10, 20, 30, 40, 50]

nome_arquivo = 'dados.bin'

with open(nome_arquivo, 'wb') as arquivo_binario:
    for numero in numeros:
        arquivo_binario.write(struct.pack('i', numero))

print(f"Números gravados no arquivo '{nome_arquivo}'.")

print("Números armazenados no arquivo:")
with open(nome_arquivo, 'rb') as arquivo_binario:
    while True:
        bytes_lidos = arquivo_binario.read(4)
        if not bytes_lidos:
            break
        numero = struct.unpack('i', bytes_lidos)[0]
        print(numero)
