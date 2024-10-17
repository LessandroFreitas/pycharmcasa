"""
#6 Realiza a leitura de 1 float referente ao salário do cidadão e apresenta o salário com reajuste de 10% da inflação.

salario = float(input("digite o salario "))

aumento = salario * 1.1
print(aumento)

#8 Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte
resultado:
• A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
• A mensagem "Reprovado", se a média for menor do que sete;
• A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("digite um valor: "))
nota2 = float(input("digite um valor: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção")

elif media >= 7 and media < 10:
    print("APROVADO")

elif media >= 0 and media < 7:
    print("REPROVADO")

else:
    print("Media invalida!")


• #9 Faça um Programa que leia dois números inteiros e mostre o maior deles.

numero1 = int(input("digite um valor: "))
numero2 = int(input("digite um valor: "))

if numero1 > numero2:
    print("O maior numero é",numero1)
else:
    print("O maior numero é",numero2)


#10 Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela

variavel1 = int(input("digite um valor: "))
variavel2 = int(input("digite um valor: "))

novaVariavel1 = variavel1
novaVariavel2 = variavel2

novaVariavel1 = variavel2
print (novaVariavel1)

novaVariavel2 = variavel1
print (novaVariavel2)


11 As Organizações Hamurabi Medeiros resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram
para desenvolver o programa que calculará os reajustes.
• Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
salário atual:
• salários até R$ 280,00 (incluindo) : aumento de 20%
• salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
• salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
• salários de R$ 1500,00 em diante : aumento de 5%
• Após o aumento ser realizado, informe na tela:
• o salário antes do reajuste;
• o percentual de aumento aplicado;
• o valor do aumento;
• o novo salário, após o aumento.
"""

salario = int (input("Informe o valor em R$: "))

if 0 <= salario <= 280:
    aumento1 = salario * 1.2
    valorReajuste1 = aumento1-salario
    print("")
    print("Salário anterior: ",salario,"\nO percentual aplicado foi: 20 %","\nO valor do aumento é:",valorReajuste1,"\nO novo salário é: ",aumento1)

elif salario > 280 and salario <= 700:
    aumento2 = salario * 1.15
    valorReajuste2 = aumento2 - salario
    print("")
    print("Salário anterior: ", salario, "\nO percentual aplicado foi: 15 %", "\nO valor do aumento é:", valorReajuste2,
          "\nO novo salário é: ", aumento2)

elif salario > 700 and salario <= 1500:
    aumento3 = salario * 1.1
    valorReajuste3 = aumento3 - salario
    print("")
    print("Salário anterior: ", salario, "\nO percentual aplicado foi: 10 %", "\nO valor do aumento é:", valorReajuste3,
          "\nO novo salário é: ", aumento3)

elif salario > 1500:
    aumento4: float = salario * 1.05
    valorReajuste4 = aumento4 - salario
    print("")
    print("Salário anterior: ", salario, "\nO percentual aplicado foi: 5 %", "\nO valor do aumento é:", valorReajuste4,
          "\nO novo salário é: ", aumento4)


"""
12 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
calcule a sua média. A atribuição de conceitos deve obedecer à tabela acima.


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1+nota2) / 2

if 9 <= media <= 10:
    print("Conceito A sua média foi",media)
elif media >= 7.5 and media < 9:
    print("Conceito B sua média foi", media)
elif  media >= 6 and media < 7.5:
    print("Conceito C sua média foi",media)
elif media >= 4 and media < 6:
    print("Conceito D sua média foi", media)
elif  media >= 0 and media < 4:
    print("Conceito E sua média foi",media)
else:
    print('Média inválida!')

"""