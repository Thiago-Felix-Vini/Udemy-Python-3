"""
Resolução do professor
"""
import os
lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i': # inserir 
        os.system('clear')
        valor = input('valor: ')
        lista.append(valor)

    elif opcao == 'a': # Deletar
        indice_str = input(
            'Escolha o indice para apagar: '
        )
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError: # aparece caso o usuario não tenha digitado um numero.
            print('Por favor digite número int.')
        except IndexError: # este except aparece caso o indice indicado pelo usuario não exista.
            print('Índice não existe na lista')
        except Exception: # aparece se o erro for desconhecido.
            print('Erro desconhecido')

    elif opcao == 'l': # Listar
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print (35*'-')
            print(i, valor)
            print (35*'-')
    else:
        print('Por favor, escolha i, a ou l.')