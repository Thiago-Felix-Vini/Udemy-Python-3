#Formatação de strings 

nome = 'Thiago Vinicius'
altura = 1.75
peso = 124
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é:'
linha_3 = f'{imc:.2f}'

print (linha_1)
print (linha_2)
print (linha_3)

#Anotação
"""
O codigo (:.nf) define as casas decimais caso o número seja float

"""