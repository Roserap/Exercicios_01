
class Contador:
    def __init__(self, n):
        
        self.n = n
        self.atual = 1

    def __iter__(self):
        
        return self

    def __next__(self):
        
        if self.atual <= self.n:
            numero = self.atual
            self.atual += 1
            return numero
        else:
            raise StopIteration

n = int(input("Digite um número: "))

contador = Contador(n)

print(f"Contando de 1 até {n}:")
for numero in contador:
    print(numero)
