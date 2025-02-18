"""
Listas em Python
Tipo list - Mutável 
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices de fatiamento
Métodos úteis: 
append, insert, pop, del, clear, extend, +
Create read Update  Delete
Cria, ler, alterar, apagar = lista[i] (CRUD)
"""
"Exemplo de APPEND e POP"

lista = [10, 20, 30, 40,]
# lista[2] = 300
# del lista [2] #Deletando o indice 2
# print(lista)
# print(lista[2]) #Python moveu meu indice 3 para prencher o lugar do indice 2

lista.append(50) # Adicionando um valor no FINAL da lista
lista.pop() # Remove o último indice da lista
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3) # guardando o item removido em uma variavel 
print(lista, 'Removido,', ultimo_valor)