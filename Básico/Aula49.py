"""
Listas em Python
Tipo list - Mutável 
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices de fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido 
    del - apaga um indice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update  Delete
Criar, Ler, alterar, apagar = lista[i] (CRUD)
"""
"Exemplo de APPEND, POP, DEL, INSERT e CLEAR"

#         0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')# adiciona no final da lista
nome = lista.pop()  # remove o que estiver no final da lista ou o que estiver indicado
lista.append(1233)  # adiciona no final da lista
del lista[-1]       # deleta da lista
# lista.clear()     # limpa a lista
lista.insert(0, 5)  # Adiciona um item na lista (indie, valor escolhido)
print(lista)

"ERROS"
# lista.insert(20000, 5) # Ele não gera um erro de 
#                          range mas pode ocasionar problemas 
#                          futuros no codigo.

# print(lista[100]) # Gera um erro pois o indice 
#                     escolhido está fora da Range da minha lista.


