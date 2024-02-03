from time import sleep

valor = "sim"

while valor.lower == "sim":

    valor = int(input("Digite o numero de nomes que deseja inserir"))
    nomes = []

    for i in range(1, valor+1):
        nome = input(f"Digite o {i} nome: ")
        nomes.append(nome)
    for i in range(10):
        print("*")
        sleep(1)

    for nome in nomes:
        print(nome)

        valor = input("Deseja executar o sistema novamente ?\nsim\nnao\n >>> ")

    for i in range (10):
        print("*")
        sleep(1)
    print("Você saiu do sistema")