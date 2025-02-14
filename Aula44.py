"""
Iterável -> str, range, etc
metodo = (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor 
iter -> me entrege seu iterador
"""
# texto = iter('Luiz') #__iter__()
# print(next(texto))



texto = 'Luiz' # iteravel
# iterador = iter(texto) # iterador

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(texto)



# QUando o valor da minha str esgota causa um erro