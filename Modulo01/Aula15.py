validador = True

idade = int(input("Digite sua idade:"))

validador = (idade == 18)
print(f"A idade é igual a 18?{validador}")

validador = (idade != 18)
print(f"A idade é diferente a 18?{validador}")

validador = (idade > 18)
print(f"A idade é maior a 18?{validador}")

validador = (idade < 18)
print(f"A idade é menor a 18?{validador}")

validador = (idade >= 18)
print(f"A idade é maior ou igual a 18?{validador}")

validador = (idade <= 18)
print(f"A idade é menor ou igual a 18?{validador}")