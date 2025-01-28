# CALC DE IMC
nome = input ('Digite o seu nome: ')
altura = input ('Digite sua altura: ')
peso = input ('Digite o seu peso em quilos: ')

altura_1 = float(altura)
peso_1 = float(peso)
imc = (peso_1 / altura_1**2)

imc_1 = print (f'{nome} Você tem um indice de taxa corporal de {imc}')

if imc == imc > 30:
    print ('Obesidade')
    
if imc == imc < 25:
    print ('peso normal')  
    
if imc == imc > 26 < 30:
    print ('pré obesidade')


