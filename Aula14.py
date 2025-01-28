#Formatação de strings com metodo format 

a = 'AAAAAA'
b = 'BBBBBB'
c = 1.1
string = 'a={0} b={nome2} c={nome3:.2f}'
formato = string.format( a,nome2=b,nome3=c)

print(formato)

#ANOTAÇÕES 
""" 1
O metodo format respeita uma ordem 
de 0 para os parametros seguintes.

"""

""" 2
Caso ocorra erro de "ranger" é porque 
não resta mais nada a ser alocado.

"""

""" 3
Tudo que vinher depois de um parametro 
nomeado deve ser nomeado também, 
caso não seja apresentara erro.

"""