'''
Cálculo de Média e Aprovação
Elabore um programa que solicite duas notas ao usuário e calcule a média. Em seguida,
informe se o aluno foi:
• Aprovado (média maior ou igual a 7)
• Recuperação (média entre 5 e 6.9)
• Reprovado (média abaixo de 5)
'''

nota1 = float("Digite a primeira nota: ")
nota2 = float("Digite a segunda nota: ")

media = nota1 + nota2 / 2

if media => 7:
    print(f"media: {media:.2f} - aprovado")
elif 5 <= media < 7
    print(f"media: {media:.2f} - recuperacao")
else:
    print(f"media: {media:.2f} - reprovado")
