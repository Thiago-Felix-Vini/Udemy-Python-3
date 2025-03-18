""" 
Introdução ao try/except
try -> tentar executar o código
excpet -> ocorreu algum erro ao tentar executar

"""
# NÃO É COMUM NEM PRUDENTE UTILIZAR O TRYEXCEPT DESSA MANEIRA, ESTOU UTILIZANDO DESSA FORMA APENAS PARA TESTES E CONHECIMENTO.

numero_str = input(
    'Vou dobrar o número que você digitar: '
    )

try:   #ISTO É CHAMADO DE "FAIL FAST" (ERRAR O MAIS RÁPIDO POSSÍVEL E MANDAR PARA A EXCEÇÃO)
    numero_float = float(numero_str) 
    print('FLOAT:', numero_float)
    print(f'O dobre de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if(numero_str.isdigit()):
#     numero_float = float(numero_str)
#     print(f'O dobre de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')