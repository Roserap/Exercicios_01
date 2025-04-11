
class Livro:
    def __init__(self, titulo, autor, paginas):
        
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        
        return f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}"

    def __len__(self):
        
        return self.paginas


livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1216)


print("Detalhes do Livro:")
print(livro1)


print(f"Número de páginas: {len(livro1)}")
