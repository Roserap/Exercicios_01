import platform

nome_sistema = platform.system()
versao_sistema = platform.version()
arquitetura_processador = platform.architecture()[0]

print(f"Nome do Sistema Operacional: {nome_sistema}")
print(f"Versão do Sistema: {versao_sistema}")
print(f"Arquitetura do Processador: {arquitetura_processador}")
