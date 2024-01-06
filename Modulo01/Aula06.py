#Criando formas constantes de acesso a dados inconstantes
nome= input("Digite seu nome:")
sobrenome = input("Digite seu sobrenome:")
idade = int(input("Digite sua idade:"))

# Concatenação: por dados um do lado do outro
#Com a concatenação temos 3 strings declaradas e 3 variaveis adicionadas que serao interpretados os tipos posteriormente

#Mascara de substituição
print("O nome é {}\no sobrenome é {}\nA idade é {}",format(nome,sobrenome,idade))