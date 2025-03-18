for i in range(10): #Conte até chegar em 9 passando em cada número, para completar a condição.
    if i == 2:
        print('i é 2, pulando...')
        continue
    
    if i == 8:
        print('i é 8, seu else não executá')
        break
    
    for j in range(1, 3): #Conte até 2 passando em cada número
        print(i, j)
else:
    print('For completo com sucesso!')