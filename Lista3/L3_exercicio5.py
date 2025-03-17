""""5. Sequência de Fibonacci
Escreva um programa que peça ao usuário um número N e exiba os N primeiros termos da
Sequência de Fibonacci.
Obs: A sequência de Fibonacci começa com 0 e 1, e cada termo seguinte é a soma dos dois
anteriores:"""

n = int(input("Digite um número inteiro positivo (N): "))

if n <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    
    fibonacci = [0, 1]

    
    for i in range(2, n):
        proximo_termo = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(proximo_termo)

    
    print(f"Os {n} primeiros termos da sequência de Fibonacci são:")
    print(fibonacci[:n])
