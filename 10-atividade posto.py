import os
os.system('cls')

litros = float(input("Digite a quantidade de litros vendidos: "))
combustivel = input("Digite o tipo de combustível (A - Álcool / G - Gasolina): ").upper()

match combustivel:

    case "A":
        preco = 3.79

        if litros <= 25:
            desconto = 0.10
        else:
            desconto = 0.20

    case "G":
        preco = 6.59

        if litros <= 25:
            desconto = 0.15
        else:
            desconto = 0.30

    case _:
        print("Tipo de combustível inválido.")
        desconto = 0
        preco = 0

valor = litros * preco
valor_desconto = valor * desconto
total = valor - valor_desconto

print("\nQuantidade de litros:", litros)
print("Combustível:", combustivel)
print("Valor do desconto: R$", format(valor_desconto, ".2f"))
print("Valor a pagar: R$", format(total, ".2f"))
