"""
Cálculo do Salário Mensal
Faça um programa que pergunte o número de horas trabalhadas no mês e o valor recebido
por hora. O programa deve calcular e exibir o salário total do mês.
"""

    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

    valor_por_hora = float(input("Informe o valor por hora trabalhada: "))

    salario_total = horas_trabalhadas * valor_por_hora

    print(f"O salário total do mês é: R$ {salario_total:.2f}")