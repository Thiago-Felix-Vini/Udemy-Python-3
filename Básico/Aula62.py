# Desempacotamento
# de meétodos e funções
string = 'ABCD'
lista = ['Maria','Helena','Eduarda']
tupla = 'Python', 'é','legal'

# p, b, *_, ap, u = lista
# print(p, u, ap)

# for nome in lista: # Exibir cada item da lista
#     print(nome, end=' ')

"Mesmo resultado, processos diferentes:"
print('Maria','Helena','Eduarda')
print(*lista)
print(*string)
print(*tupla)