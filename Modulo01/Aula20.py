numero = int(input("Digite um número para a tabuada que gostaria de saber: "))
for i in range(1,11):
    print("{} X {} = {}".format(numero,i,numero*i))