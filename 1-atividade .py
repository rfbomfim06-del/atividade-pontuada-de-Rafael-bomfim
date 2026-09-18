import os
os.system('cls')

#entrada
valorA = input('digite o valor de A: ')
valorB = input('digite o valor de B: ')
valorC = input('digite o valor de C: ')

#processo
soma = valorA + valorB
if soma < valorC:
    print(f'valorA + ValorB é menor que valorC')

elif soma > valorC:
    print(f'valorA + ValorB é maior que valorC')
#saida
print(f'\nsoma:{soma}')
