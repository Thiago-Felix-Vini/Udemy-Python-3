"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual 
Argumento não nomeado recebe apenase o argumento (valor)
"""

# def soma(x, y): #parametro da Def
#     #Definição da função 
#     print(f'{x=} + y={y}', '|', 'x + y =', x + y)
# soma(1,2) #Argumento
# soma(y=2, x=1)


"Argumento nomeado"
def soma(x, y, z): #parametro da Def
    #Definição da função 
    print(f'{x=} + y={y} {z=}', '|', 'x + y + z =', x + y + z)

soma(1, 2, 3) #Argumento
soma(1, 2, z=3)#Argumento nomeado
#Quando nomear um argumento todos os proximos argumentos devem ser nomeados também
print(1, 2 , 3, sep='-')