
def contar_pares(n):
    
    for i in range(0, n + 1, 2):
        yield i


n = int(input("Digite um número: "))

print(f"Números pares até {n}:")
for par in contar_pares(n):
    print(par)
