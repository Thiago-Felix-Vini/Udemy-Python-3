"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de indices inexistentes na lista.
"""

import os
opção = ''
lista = []

while True:
    if len(lista) < 1:
        print (35*'-')
        print('Nada em lista')
        print (35*'-')
        
    for indice, compras in enumerate(lista):
        print (35*'-')
        print(indice, compras)
        print (35*'-')
        
    print('Escolha uma opção')
    print('[i]nserir, [a]pagar, [l]istar')
    opcao = input('Insira uma opção: ')
    
    if len(opcao) > 1:
        print(20*'/')
        print('insira apenas uma opção')
        print(20*'/')
        continue
    
    opcoes_aceitas = 'ial'
    if opcao not in opcoes_aceitas:
        print('Digite uma opção valida')
        continue
        
    if opcao == 'i': # inserir 
        os.system('clear')
        
        valor1 = input('Digite um valor para ser inserido: ')
        
        if len(valor1) >= 1:
            print(f'Seu valor foi inserido!!')
            continue

        if valor1 in (' '):
            print('insira o valor sem espaços')
            continue      
        

    if opcao == 'a': # deletar
        os.system('clear')

        indice_str = input(
        'Escolha o indice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possível apagar este indice.')
    

    if opcao == 'l' and len(valor1) > 1: # listar
        if len(valor1) < 1:
            print('Nada a listar')
            continue

        os.system('clear')
        
        if len(valor1) > 1:    
            lista.append(f'{valor1}')
            valor1 = 0
            print(f'Seu valor:({valor1}) foi listado com sucesso')           
            continue 
    
             

        
    
    