"""
Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda 
< - Direita
^ - Centro
= - Força o número a aparecer antes do zero 
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a __repr_ _str_  
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.716967926762:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')