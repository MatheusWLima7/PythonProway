import random

destino1 = str(input("Informe o primeiro destino de viagem:"))
destino2 = str(input("Informe o segundo destino de viagem:"))
destino3 = str(input("Informe o terceiro destino de viagem:"))
destino4 = str(input("Informe o quarto destino de viagem:"))
destino5 = str(input("Informe o quinto destino de viagem:"))
destino6 = str(input("Informe o sexto destino de viagem:"))

ListaDestinos = [destino1, destino2, destino3, destino4, destino5, destino6]
print(ListaDestinos)
sorteio = random.choice(ListaDestinos)

print("O destino sorteado foi:", sorteio)