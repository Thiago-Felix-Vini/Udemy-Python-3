"""
Interpolação básica de strings
s - string 
d e i - int
f - float
x e x - Hexadecimal (ABCDEF0123456789)
"""
nome = 'luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco) 
#variavel = '%s, Teste com apenas um dado' % nome
print(variavel)
print('O hexadecimal de %d é %04x' % (1500, 1500)) 