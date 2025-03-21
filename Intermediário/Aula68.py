"""
Valores padrão para parâmetros podem
ter valores padrào. Caso o valor não seja 
enviado para o parâmetro, o valor padrão será 
usado.
Refatorar: editar o seu código.
"""

# def soma(x, z=None, y=None): #Error: type None,
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=} {z=}', x + y + z)

soma(1, 2)
soma(3, 5)
soma(100, 20)
soma(7, 9, 0)
soma(y=9, z=7, x=0)
