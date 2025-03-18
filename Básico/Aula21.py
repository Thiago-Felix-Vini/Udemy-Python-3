# Operador (or)
"""
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha:')

senha_permitida = '12345'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
"""    
# Avaliação de curto circuito 
senha = input(True and False or 0 or 'abc' or True)
print(senha)
"""
Ele retorna ABC por ser um dado True str.
 
"""
# UM if com or:
senha_1 = input('Senha: ') or 'Sem senha'
print(senha_1)