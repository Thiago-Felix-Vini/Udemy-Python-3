"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# num_str = input('Digite um número Inteiro: ')
# try:
#     num_int = int(num_str)
#     num_int_1 = (num_int % 2 == 0)
    
#     if num_int_1 is True and int:
#         print('Seu número é par')
        
#     if num_int_1 is False and int:
#         print('Seu número é impar')
        
# except:
#     print('Você não digitou um número inteiro, encerrando programa...')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horario_usu = input('Digite seu horario atual no formato 24h: ')

# horario_float = float(horario_usu)

# if horario_float >= 18.00:
#     print('Boa noite!!')
    
# if horario_float >= 12.00 and \
#     horario_float <= 17.59:
#     print('Boa tarde!!')
    
# elif horario_float >= 00.00 and \
#     horario_float <= 11.59:
#     print('Bom dia!!')
    
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome_1 = input('Digite seu primeiro nome: ')

lendo_nm = len(nome_1)
lendo_nm_int = int(lendo_nm)

if lendo_nm_int <= 4:
    print('Seu nome é pequeno')
if lendo_nm_int >= 5 and lendo_nm_int <= 6:
    print('Seu nome é normal')
if lendo_nm_int > 6:
    print('Seu nome é grande')
