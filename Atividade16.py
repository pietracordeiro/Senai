print("Bem-vindo ao sistema de qualidade")
print("Aluna: Pietra Angelina")

for i in range(5):

    leitura = float(input("Digite o valor da leitura do sensor: "))
    horas = int(input("Digite as horas de uso do sensor: "))

    if horas < 200:
        desconto = 0
    elif horas >= 200 and horas <= 999:
        desconto = 0.05
    elif horas >= 1000 and horas <= 1999:
        desconto = 0.10
    else:
        desconto = 0.15

    valor_calibrado = leitura - (leitura * desconto)

    print("Valor bruto:", leitura)
    print("Valor calibrado:", valor_calibrado)
    print("-----------------------")