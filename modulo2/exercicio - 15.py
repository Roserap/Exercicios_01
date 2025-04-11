import os
import datetime
import calendar
import time

diretorio_atual = os.getcwd()
print(f"Diretório atual: {diretorio_atual}")

data_hora_atual = datetime.datetime.now()
print(f"Data e hora atuais: {data_hora_atual}")

ano_atual = data_hora_atual.year
mes_atual = data_hora_atual.month
calendario = calendar.month(ano_atual, mes_atual)
print(f"\nCalendário do mês atual:\n{calendario}")

print("Fazendo uma pausa de 3 segundos...")
time.sleep(3)
print("Pausa concluída!")
