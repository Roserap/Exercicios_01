"""5. Conversão de Temperatura
Crie uma função que converta temperaturas de Celsius para Fahrenheit. No
programa principal, solicite uma temperatura ao usuário em graus Celsius e utilize
a função para exibir o valor correspondente em Fahrenheit."""

def celsius_para_fahrenheit(celsius):
    
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

if __name__ == "__main__":
    
    temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
    
    temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)
    
    print(f"A temperatura em Fahrenheit é: {temperatura_fahrenheit:.2f} °F")
