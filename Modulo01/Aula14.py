a = "="*20

print(a, "Primeiro Funcionário", a)

nome1 = str(input("Digite seu nome:"))
idade1 = int(input("Digite sua idade:"))
salario1 = float(input("Digite seu salário:"))

print(a, "Segundo Funcionário", a)

nome2 = str(input("Digite seu nome:"))
idade2 = int(input("Digite sua idade:"))
salario2 = float(input("Digite seu salário:"))

print(a, "Terceiro Funcionário", a)

nome3 = str(input("Digite seu nome:"))
idade3 = int(input("Digite sua idade:"))
salario3 = float(input("Digite seu salário:"))

print(a, "Quarto Funcionário", a)

nome4 = str(input("Digite seu nome:"))
idade4 = int(input("Digite sua idade:"))
salario4 = float(input("Digite seu salário:"))

Funcionario1 = {"Nome": nome1, "Idade": idade1, "Salário": salario1}
Funcionario2 = {"Nome": nome2, "Idade": idade2, "Salário": salario2}
Funcionario3 = {"Nome": nome3, "Idade": idade3, "Salário": salario3}
Funcionario4 = {"Nome": nome4, "Idade": idade4, "Salário": salario4}

listaFuncionarios = [Funcionario1, Funcionario2, Funcionario3, Funcionario4]

print(a, "Primeiro Funcionário", a)
print(listaFuncionarios[0])

print(a, "Segundo Funcionário", a)
print(listaFuncionarios[1])

print(a, "Terceiro Funcionário", a)
print(listaFuncionarios[2])

print(a, "Quarto Funcionário", a)
print(listaFuncionarios[3])

