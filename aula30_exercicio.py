velocidade = int(input('Insira a velocidade do carro: '))
local_carro = int(input('Insira o local do carro: '))

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if velocidade > RADAR_1 and (local_carro >= LOCAL_1 - RADAR_RANGE and local_carro <= LOCAL_1 + RADAR_RANGE):
    print('Velocidade do carro passou do limite do radar 1')
    print('O carro foi multado')