n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunda nota:"))

media = (n1 + n2) / 2

if(media < 7.0):
    mensagem = f"Você foi reprovado com a média {media}"
elif(media >= 7.0):
     mensagem = f"Você foi aprovado com a média {media}"

print(mensagem)