import os
os.system('cls')
#entrada
nome_produto = input("Digite a descrição do produto (nome): ")
quantidade = int(input('digite a quantidade: '))
preco_unitario = float(input("Digite o preço unitário: R$ "))
#processo
total = quantidade * preco_unitario
if quantidade <= 5:
    desconto = total * 0.02
elif quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05
total_a_pagar = total - desconto


#saida
print(f"\n--- RESUMO DA COMPRA ---")
print(f"Produto: {nome_produto}")
print(f"Total sem desconto: R$ {total:.2f}")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
