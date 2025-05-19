distancia = float(input(f'Digite a distancia em Km: '))
combustivel_gasto = float(input(f'Digite o total de combustível gasto em litros: '))
consumo_medio = distancia / combustivel_gasto 

print(f' O consumo médio é: {consumo_medio}.')

if consumo_medio <= 8:
    print('Consumo elevado! 🚗📉')
elif consumo_medio <= 12:
    print('Consumo médio 🚗📊')
else:
    print('Consumo econômico! 🚗📈')

print(f' O consumo médio é: {consumo_medio}.')