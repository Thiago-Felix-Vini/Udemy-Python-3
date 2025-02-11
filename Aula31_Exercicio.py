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

"Exercicio 1, Metodo do professor"

# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'impar'
    
#     if par_impar:
#         par_impar_texto = 'par'
        
#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# horario_usu = input('Digite seu horario atual no formato 24h: ')

# horaio_int = int(horario_usu)

# if horaio_int >= 18 and \
    # horario_int <= 23:
#     print('Boa noite!!')
    
# if horaio_int >= 12 and \
#     horaio_int <= 17:
#     print('Boa tarde!!')
    
# elif horaio_int >= 00 and \
#     horaio_int <= 11:
#     print('Bom dia!!')

"Exercicio 2, Metodo do professor"

# entrada = input ('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)
    
#     if hora >= 0 and hora <= 11:
#         print('Bom dia!!')

#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde!!')

#     elif hora >= 18 and hora <= 23:
#         print('Boa noite!!')

#     else:
#         print('Não conheço essa hora')

# except:
#     print('Por favor, digite apenas números inteiros')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos, escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# nome_1 = input('Digite seu primeiro nome: ')

# lendo_nm = len(nome_1)
# lendo_nm_int = int(lendo_nm)

# if lendo_nm_int <= 4:
#     print('Seu nome é pequeno')

# if lendo_nm_int >= 5 and lendo_nm_int <= 6:
#     print('Seu nome é normal')

# if lendo_nm_int > 6:
#     print('Seu nome é grande')

"Exercicio 3, Metodo do professor"

# nome = input('Digite seu nome: ')
# tamanho_nome = len(nome)

# if tamanho_nome > 1:
#     if tamanho_nome <= 4:
#         print('Seu nomeé curto')
#     elif tamanho_nome >= 5 and tamanho_nome <= 6:
#         print('Seu nome é normal')
#     else:
#         print('Seu nome é muito grande')
# else:
#     print('Digite mais de uma letra')