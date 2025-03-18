"""
Introdução ás funções (def) em Pyhton
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
e retornar um valor especifico.
Por padrão, funçoões python retornam None (nada).
"""

"criando um função com def" 

# def Print(): #print com P maiusculo sendo criada
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')
# Print()

"Adicionando parametros na funçào"

# def imprimir(a, b, c):
#     print(a, b, c)
   


# imprimir(1, 2, 3)
# imprimir(4, 5, 6)


def saudacao(nome = 'Sem nome'):
    print(f'Olá, {nome}!')


saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')
saudacao()

