
nome_arquivo = 'dados.txt'

try:
    
    with open(nome_arquivo, 'r') as arquivo:
        
        linhas = arquivo.readlines()
        
        numero_de_linhas = len(linhas)
        
        print(f"O arquivo '{nome_arquivo}' possui {numero_de_linhas} linhas.\n")
        
        print("Conteúdo do arquivo:")
        for linha in linhas:
            print(linha.strip())

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
