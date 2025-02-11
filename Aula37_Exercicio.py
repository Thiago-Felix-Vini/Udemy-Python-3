"""
Iterando strings com while 
"""
"""
#       012345678910
nome = 'Luiz Otávio' # Iteraveis
#       1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string += '*L*U*I*Z *O*T*Á*V*I*O'
"""

nome = input('Digite seu nome e seu sobrenome: ')
indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
 
novo_nome += '*'
print(novo_nome)
  

"Resolução do professor"


# nome = ('Luiz Otávio')

# indice = 0 
# novo_nome = ''
# while indice < len(nome):
#     letra = nome[indice]
#     novo_nome += f'*{letra}'
#     indice += 1

# novo_nome += '*'
# print(novo_nome)