# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser 
# verdadeiras
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considaerados falsy (que vc já viu)
# 0.0.0 '' False
# Tamnbém existe o tipo Nome que é 
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha:')

senha_permitida = '12345'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    
    
"""
print(True and False and True)

"""