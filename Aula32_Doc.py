"Documentação, tipos imutáveis, métodos de string"

"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'Thiago Vinicius'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
# string[3] = 'ABC'
# print(string)
# print(outra_variavel)
print(string.zfill(100))