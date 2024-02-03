from time import sleep
valor = int(input("Insira a quantidade de nomes que deseja inserir na lista: "))
nomes = []

for i in range(1,valor+1):
    nome = input(f"Digte o {i} nome: ")
    nomes.append(nome)
for i in range(10):
    print("*")
    sleep(1)
for nome in nomes:
    print(nomes)

    
