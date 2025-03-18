"""
split e join com list e str
split - divide uma string 
join - une uma string
"""
frase = '  Olha só que   ,    coisa interessante            '
lista_frases_cruas = frase.split(',') # .split = separa a frase nos espaços em branco.

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases[i].strip()) # .strip = corta os espaços do começo e do fim.
    # print()
    # print(lista_frases[i].lstrip()) # .lstrip = corta o espaço na esquerda (começo) da frase.
    # print()
    # print(lista_frases[i].rstrip()) # .rstrip = corta o espaço na direita (final) da frase.
frases_unidas = '-'.join(lista_frases) # .join = junta elementos de uma iteravel (listas, tuplas) em uma unica string.
print(frases_unidas)