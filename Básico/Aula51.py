"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# nome = 'Luiz'
# noutra_variavel = nome
# nome = 'João'
# print(nome)
# print(noutra_variavel)

lista_a = ['Luiz', 'Maria']
lista_b = lista_a .copy() #Copiando a lista A para a lista B com metodo '.copy()'.

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b) #Após efetuar o metodo copy, minha lista B 
               # não é alterada pela 
               # mudança feita na lista A