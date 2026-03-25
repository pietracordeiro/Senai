pressao = float(input("Digite a pressão: "))
temperatura = float(input("Digite a temperatura: "))
ciclos = int(input("Digite a quantidade de ciclos: "))

fator_risco = pressao * temperatura

if ciclos < 200:
    desconto = 0
elif ciclos >= 200 and ciclos <= 999:
    desconto = 0.05
elif ciclos >= 1000 and ciclos <= 1999:
    desconto = 0.10
else:
    desconto = 0.15

risco_final = fator_risco - (fator_risco * desconto)

print("Fator de risco bruto:", fator_risco)
print("Fator de risco com redução:", risco_final)