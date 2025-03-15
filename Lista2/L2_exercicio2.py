'''
2. Maior Número
Faça um programa que peça dois números ao usuário e exiba o maior deles. Caso os números
sejam iguais, exiba uma mensagem informando essa condição.
'''
numero1 = float(input("Digite o primeiro numero. "))
numero2 = float(input("Digite o segundo numero. "))

    if numero1 > numero2:
        print(f"O numero maior é: {numero1}")
    elif numero2 > numero1:
        print(f"O maior numero é: {numero2}")
    else:
        print(f"Os numeros são iguais")
