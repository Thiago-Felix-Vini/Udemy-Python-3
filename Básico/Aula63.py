"""
Operação termária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
# condicao = 10 == 10
# variavel = 'valor' if True else 'Outro valor'
# print(variavel)

# digito = 9 # > 9 = 0
# # novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)

"Não recomendado"
print('valor' if False else 'Outro valor' if False else 'Fim')