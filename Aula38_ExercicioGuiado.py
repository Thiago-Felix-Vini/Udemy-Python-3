" Calculadora com while"

while True:
    
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    
    try:
        num_int_1 = float(num_1)
        num_int_2 = float(num_2)
        
    except:
        print('Você não digitou um número valido')  
        continue
    
    print(f'Escolha um operador:')
    print('[1] Soma, [2] Subtração, [3] Divisão ou [4] Multiplicação')
    opera = input()
        
    operadores_permitidos = '1234'
    
    if opera not in operadores_permitidos:
        print('Operador invávlido.')
        continue
    
    opera_int = int(opera)
    
    if opera_int == 1:
        resul_soma = (num_int_1 + num_int_2 )
        print(f'O resultado da sua soma foi: {resul_soma}')
        
    if opera_int == 2:
        resul_sub = (num_int_2 - num_int_1)
        print(f'O resultado da sua subtração foi: {resul_sub}')
        
    if opera_int == 3:
        resul_div = (num_int_2 / num_int_1)
        modulo = (num_int_2 % num_int_1)
        print(f'O resultado da sua Divisão foi: {resul_div}')
        print(f'O resto da divisão: {modulo}')
        
    if opera_int == 4:
        resul_multi = (num_int_2 * num_int_1)
        print(f'O resultado da sua soma foi: {resul_multi}')

    sair = input('Quer sair? [s]im: ').lower().startswith('s') # .lower (deixa tudo em letra minuscula), .startswith('s') (Identifica a condiçõo emposta enre aspas e da como True)
    if sair is True:
        print('Saindo...')
        break
    
     