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
    extend - estende listas
    + - concatena listas
Create Read Update  Delete
Criar, Ler, alterar, apagar = lista[i] (CRUD)
"""
"Exemplos de EXTEND e concatenação com lista"

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b # juntando as listas com concatenação 
#                             e passando para uma variavel

lista_d = lista_a.extend(lista_b) # Estende a lista A para a lista B, 
#                                   mas nõo é possivel guardar 
#                                   pois retorna NONE.

print(lista_c)
