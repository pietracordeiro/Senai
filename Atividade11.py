estoque = {}
print ("Seja bem-vinda(o) ao sistema de gestão de estoque desenvolvido da Pietra")
while True:
    operacao = input ("Deseja registrar a entratada e saída do produto?(digite'entrada' ou 'saída') ou 'sair'").lower()

    if operacao not in ['entrada', 'saida', 'sair']:
        print ("operacao inválida.")
        continue

    if operacao == 'sair':
        break

    produto = input("nome do produto: ").strip()
    qtd = int(input("quantidade"))
    
    if operacao == 'entrada':
        estoque[produto] = estoque.get(produto, 0) + qtd
    elif operacao == 'saida':
        if estoque.get(produto, 0) >= qtd:
            estoque[produto] -= qtd
        else:
            print("Erro:produto inexistente ou estoque insufiiente.")

print("\n ---Estoque Final--- ")
for p, q in estoque.items():
    print(f"{p}: {q}")