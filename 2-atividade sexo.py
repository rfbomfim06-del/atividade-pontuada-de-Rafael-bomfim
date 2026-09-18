# Exercício 5
import os
os.system('cls')
#entrada
nome = input('digite seu nome: ')
sexo = input('digite seu sexo (M ou F): ')
estado_civil = input('digite seu estado civil: ')

#processo
if sexo == 'F' and estado_civil:
    tempo= input('infome do tempo de casada')
print('quantos anos de casada?')
print("sexo:", sexo)
print("estado civil", estado_civil)
print("tempo:", tempo)

else:
print("estado civil", estado_civil)
print("sexo:", sexo)
