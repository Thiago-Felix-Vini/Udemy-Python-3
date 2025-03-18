"""
Introdução ao desempacotamento + tuples (tuplas)
"""
"Utilizando ( _ ) para referenciar o restante das variaveis que não serão utilizadas "
_, _, nome, *_= ['Maria', 'Helena', 'Luiz']
print (nome)

"Criando uma variavel para armazenar o restante da lista"
# nome1, *resto = ['Maria', 'Helena', 'Luiz']
# print (nome1, resto)

"Erro de desempacotamento"
# nome1, nome2 = ['Maria', 'Helena', 'Luiz'] #Muitos valores para desempacotar (Gera erro)

"Uma variaveel recebe a lista que recebe outras variaveis"
# nomes = ['Maria', 'Helena', 'Luiz']
# nome1, nome2, nome3 = nomes
# print(nome2)