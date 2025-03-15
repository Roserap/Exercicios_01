'''
5. Verificação de Triângulo
Peça ao usuário três números representando os lados de um triângulo. O programa deve
verificar e informar se os valores formam um triângulo válido (a soma de dois lados deve ser
sempre maior que o terceiro).
'''

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input(Digite o comprimento do terceiro lado: "))

    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        print("Os valores formam um triangulo válido.")
    else:
        print("Os valores não formam um triangulo válido.")
