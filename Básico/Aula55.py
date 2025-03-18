"""
Tipo tupla - Uma lista imutável
"""
"Convertendo lista para tupla e vice versa "
nomes = ['Maria', 'Helena', 'Luiz']
nomes = tuple(nomes)
nomes = list(nomes)
print(nomes[-1])
print(nomes)

"Tupla comum"
# nomes = ['Maria', 'Helena', 'Luiz']
# print(nomes[-1])

"Erro"
# nomes = ['Maria', 'Helena', 'Luiz']
# nomes[1] = 'outro' #Alterando valor de algo imutável (Gerando erro)
# _, _, nome, *_= nomes
# print(nomes)
# print (nome)