#Questao 4

salario = float(input("Digite o salario: R$"))
porcentagem = float(input("Digite a porcentagem de aumento:"))
aumento = salario*(porcentagem/100)
novoSalario = salario*(porcentagem/100)+salario
print("O aumento será de: R$ %.2f" %aumento)
print("O novo salario e: R$ %.2f" %novoSalario)

