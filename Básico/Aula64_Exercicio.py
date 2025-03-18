import re
import sys

entrada = input('CPF [670.825.860-94]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
) 

entrada_e_sequencia = entrada == entrada[0] * len(entrada)

if entrada_e_sequencia:
    print('Você enviou dados sequenciais.')
    sys.exit()
# cpf_enviado_usuario = '670.825.860-94' \
# .replace('.', '') \
# .replace('.', '') \
# .replace('.', '')

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_2 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * (contador_regressivo_2)
    contador_regressivo_2 -= 1
digito_1 = ((resultado_digito_1 * 10) % 11)
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)

#Calculnado o segundo digito do cpf

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0 

for digito in dez_digitos:
    resultado_digito_2 = int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)

# Validação

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('Cpf inválido')
