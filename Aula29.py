""" ALGUMAS BOAS PRÁTICAS

CONSTANTE = "Variáveis" que não vão mudar
muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruimm)

"""
velocidade = 61  # velocidade atual do carro
local_carro = 101  # local em que o carro está na estrada

RADAR_1 = 60  # máxima do radar 1 
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

velocidade_em_que_carro_passou_radar_1 = velocidade > RADAR_1 # deixando o código mais legivel
carro_passou_radar_1 = local_carro >=local_carro >= \
        (LOCAL_1 + RADAR_RANGE) and \
        local_carro <= (local_carro + RADAR_RANGE)
        
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_em_que_carro_passou_radar_1

# if velocidade > RADAR_1:
#     print('Velocidade carro passou do radar 1')
    
# if carro_multado_radar_1 and Velocidade_em_que_carro_passou_radar_1:
#     print('carro multado em radar 1')


if velocidade_em_que_carro_passou_radar_1:
    print('Velocidade carro passou do radar 1')
    
if carro_passou_radar_1:
    print('Carro passou radar 1')
    
if carro_multado_radar_1:
    print('Carro multado em radar 1')
    