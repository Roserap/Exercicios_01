"""2. Abertura Segura de Arquivo
Escreva um programa que solicite ao usuário o nome de um arquivo para leitura. O
programa deve tentar abrir o arquivo e exibir seu conteúdo. Utilize tratamento de
exceções para lidar com a ausência do arquivo e outros possíveis erros."""

def abrir_arquivo_seguro():
    
    nome_arquivo = input("Digite o nome do arquivo para leitura (inclua a extensão, por exemplo, 'arquivo.txt'): ")

    try:
        
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print("\nConteúdo do arquivo:")
            print(conteudo)

    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado. Verifique o nome e tente novamente.")
    except IOError:
        print("Erro: Ocorreu um erro ao tentar ler o arquivo.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    abrir_arquivo_seguro()
