import os
os.system('cls')
#entrada
renda = float(input('digite sua renda: '))
valor_total = float(input('digite o valor do emprestimo: '))
parcelas = int(input('digite a quantidade de parcelas: '))

#processo
prestacao = valor_total / parcelas
max_emprestimo = renda * 10
max_prestacao = renda * 0.3
#saida
if valor_total <= max_emprestimo and prestacao <= max_prestacao:
    print('emprestimo APROVADO')
else:
    print('emprestimo NEGADO')
