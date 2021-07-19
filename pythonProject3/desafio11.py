km = float(input("Quantos km foram percorridos com o carro? "))
dias = int(input("Por quantos dias? "))
valor = (dias * 60) + (0.15 * km)
print("Preço a pagar por {} dias e {}km rodados: R${}".format(dias, km, valor))
