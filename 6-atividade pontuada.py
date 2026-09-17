import os
os.system('cls')

# Entrada
qtd_morango = float(input("Digite a quantidade de morangos (em Kg): "))
qtd_maca = float(input("Digite a quantidade de maçãs (em Kg): "))

#processo
if qtd_morango <= 5:
    preco_morango = qtd_morango * 2.50
else:
    preco_morango = qtd_morango * 2.20


if qtd_maca <= 5:
    preco_maca = qtd_maca * 1.80
else:
    preco_maca = qtd_maca * 1.50

peso_total = qtd_morango + qtd_maca
valor_total = preco_morango + preco_maca


if peso_total > 8 or valor_total > 25.00:  # Nota: regra padrão de 10% (se for a partir de 10Kg, use peso_total >= 10)
    if peso_total >= 10 or valor_total > 15.00:
        valor_total *= 0.90  # Aplica 10% de desconto

print(f"\nValor a ser pago pelo cliente: R$ {valor_total:.2f}")