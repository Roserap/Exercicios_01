
class Animal:
    def fazer_som(self):
        
        pass

class Cachorro(Animal):
    def fazer_som(self):
        
        print("O cachorro faz: Au Au!")

class Gato(Animal):
    def fazer_som(self):
        
        print("O gato faz: Miau!")

cachorro = Cachorro()
cachorro.fazer_som()

gato = Gato()
gato.fazer_som()
