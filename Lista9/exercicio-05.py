"""5. Operações Bancárias com Tratamento de Erros
Crie um programa que simule um sistema bancário simples. O saldo inicial do
usuário é de R$ 1000,00. O programa deve permitir que o usuário insira um valor
para saque e, caso o valor solicitado seja maior que o saldo disponível, uma
exceção personalizada deve ser lançada informando que o saldo é insuficiente."""

class SaldoInsuficienteError(Exception):
    """Exceção personalizada para saldo insuficiente."""
    pass

def realizar_saque(saldo, valor_saque):
    if valor_saque > saldo:
        raise SaldoInsuficienteError("Erro: Saldo insuficiente para realizar o saque.")
    saldo -= valor_saque
    return saldo

if __name__ == "__main__":
    saldo_inicial = 1000.00
    print(f"Seu saldo inicial é: R$ {saldo_inicial:.2f}")

    while True:
        try:
            valor_saque = float(input("Digite o valor que deseja sacar: R$ "))
            saldo_inicial = realizar_saque(saldo_inicial, valor_saque)
            print(f"Saque realizado com sucesso! Seu novo saldo é: R$ {saldo_inicial:.2f}")
            break
        except SaldoInsuficienteError as e:
            print(e)
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número válido.")
