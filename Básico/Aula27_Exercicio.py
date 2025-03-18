nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print('Seu nome invertido é:',nome [::-1])
    
    if nome and (' ' in nome) and idade:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
        
    print(f'Seu nome tem: {len(nome)} letras')
    print('A primeria letra do seu nome é:',nome[0])
    print('A última letra do seu nome é:',nome[-1])
     
else:
    print('Você deixou campos vazios, encerrando programa...')





# Correção do professor:
""" 
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
        
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')
"""