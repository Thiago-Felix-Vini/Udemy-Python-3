"""
emunerate - emunera iteráveis (indices)
"""
#[(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista): # Melhor forma de utilizar o enumerate.
    print(indice, nome, lista[indice])

# lista_enumerada = enumerate(lista) #Passando o enumarate para uma variavel, porém só e possivel utilizar uma vez seu valor
# print(lista_enumerada)

# for item in lista_enumerada:
#     print(item)

# for item in enumerate(lista): #Criando um enumarate direto no for.
#     print(item)

# lista_enumerada = list(enumerate(lista))
# print(lista_enumerada)
    
# for item in enumerate(lista): # Separando o indice e o nome
#     indice, nome = item
#     print(indice, nome)
    

# for indice, nome in enumerate(lista): # Manira mais simples de separar
#     print(indice, nome)\

# for item in enumerate(lista): #Separando com for dentro de for
#     print('FOR da tupla')
#     for valor in item:
#         print(f'\t{valor}')
        