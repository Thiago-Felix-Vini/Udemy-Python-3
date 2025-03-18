"""
Lista de listas de seus indices
"""
salas = [
    #  0        1
    ['Maria','Helena', ], #0
    # 0
    ['Elaine',], #1
    #0      1        2
    ['Luiz','João','Eduarda',(0, 10, 20, 30, 40)], # 2
]

"Como acessar os indices"
# print(salas[0][1])
# print(salas[1][0])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)

print(*salas, sep='\n') # A função sep define o separador entre os argumentos passados. 
#                          Por padrão, o separador é um espaço 

