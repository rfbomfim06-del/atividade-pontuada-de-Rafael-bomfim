import os
os.system('cls')
#entrada
codigo = int(input('digite o codigo : '))
#processo
print("===== CD'S =====")
print("1 - verde       R$ 10,00")
print("2 - azul       R$ 20,00")
print("3 - amarelo    R$ 30,00")
print("4 - vermelho R$ 40,00")

match codigo:
    case 1:
        cor = 'verde'
        preco = 10.00
    case 2:
        cor = 'azul'
        preco = 20.00
    case 3:
        cor = 'amarelo'
        preco = 30.00
    case 4:
        cor = 'amarelo'
        preco = 40.00

#saida
print('cor:',cor)
print('preco:',preco)


