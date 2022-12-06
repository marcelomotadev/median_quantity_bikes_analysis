import pandas as pd
import numpy as np
import datetime as dt
from datetime import date, timedelta
from datetime import datetime

# Ler o arquivo csv para e armazena em um DataFrame

Base_Dados = pd.read_csv('bicicletas.csv')

# Extraindo informações desse banco de dados

# print(Base_Dados.info())
# print('\n')
# print(Base_Dados.describe())

#                                 Separando a Base de dados para encontrar a quantidade de feriados

feriado_verao = Base_Dados.query('(estacao == "verao") & (feriado == 1)')
feriado_outono = Base_Dados.query('(estacao == "outono") & (feriado == 1)')
feriado_inverno = Base_Dados.query('(estacao == "inverno") & (feriado == 1)')
feriado_primavera = Base_Dados.query('(estacao == "primavera") & (feriado == 1)')

# unique() -> retorna uma lista com os itens unicos de uma coluna especifica  nunique() -> retorna a quantidade

feriados_outono = feriado_outono['data'].unique()
feriados_inverno = feriado_inverno['data'].unique()
feriados_verao = feriado_verao['data'].unique()
feriados_primavera = feriado_primavera['data'].unique()

# print('Outono:', feriados_outono)
# print('Inverno:', feriados_inverno)
# print('Verao:', feriados_verao)
# print('Primavera:', feriados_primavera)

# -------------------------------------------------------------------------------------------

# funcao para encontrar quantos dias comecam com 2021 em uma lista e quantos comecam com 2022

example = Base_Dados.query('(estacao == "verao")')
verao = example['data'].unique()

def encontra_dias(list):
  y = 0
  z = 0  
  for x in list:  
    if x.startswith('2021'):
      y +=1
    else:
      z +=1
  print('2021: ', y,'2022: ', z)

# encontra_dias(verao)

# --------------- Temperatura e Quantidades por Estacao e Ano ----------------------------

# Ajustando o tipo do dado guardado na coluna 'data' de objeto para Datetime

Base_Dados['data'] = pd.to_datetime( Base_Dados['data'] )

# Criando uma nova Coluna 'Ano' para permitir o filtro por ano

Base_Dados['Ano'] = pd.DatetimeIndex( Base_Dados['data'] ).year

# Separando o Data Base por estacao e ano

outono_2021 = Base_Dados.query('(estacao == "outono") & (Ano == 2021)')
primavera_2021 = Base_Dados.query('(estacao == "primavera") & (Ano == 2021)')
verao_2021 = Base_Dados.query('(estacao == "verao") & (Ano == 2021)')
inverno_2021 = Base_Dados.query('(estacao == "inverno") & (Ano == 2021)')

outono_2022 = Base_Dados.query('(estacao == "outono") & (Ano == 2022)')
primavera_2022 = Base_Dados.query('(estacao == "primavera") & (Ano == 2022)')
verao_2022 = Base_Dados.query('(estacao == "verao") & (Ano == 2022)')
inverno_2022 = Base_Dados.query('(estacao == "inverno") & (Ano == 2022)')

#                                         temperaturas médias

def median_Temperature(year):
  if year == 2021:
    print('Verao 2021: ', verao_2021.groupby(by='data')['temperatura'].agg([np.mean]).mean())
    print('Outono 2021: ', outono_2021.groupby(by='data')['temperatura'].agg([np.mean]).mean())
    print('Inverno 2021: ', inverno_2021.groupby(by='data')['temperatura'].agg([np.mean]).mean())
    print('Primavera 2021: ', primavera_2021.groupby(by='data')['temperatura'].agg([np.mean]).mean())
  elif year == 2022:
    print('Verao 2022: ', verao_2022.groupby(by='data')['temperatura'].agg([np.mean]).mean())
    print('Outono 2022: ', outono_2022.groupby(by='data')['temperatura'].agg([np.mean]).mean())
    print('Inverno 2022: ', inverno_2022.groupby(by='data')['temperatura'].agg([np.mean]).mean())
    print('Primavera 2022: ', primavera_2022.groupby(by='data')['temperatura'].agg([np.mean]).mean())
  else:
    print('This Year isnt in range')

# median_Temperature(2021)
# print('\n')
# median_Temperature(2022)

#                                         quantidades médias por estacao

def median_Quantity(year):
  if year == 2021:
    print('verao 2021: ', verao_2021.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())
    print('outono 2021: ', outono_2021.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())
    print('inverno 2021: ', inverno_2021.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())
    print('primavera 2021: ', primavera_2021.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())
  elif year == 2022:
    print('verao 2022: ', verao_2022.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())
    print('outono 2022: ', outono_2022.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())
    print('primavera 2022: ', primavera_2022.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())
    print('inverno 2022: ', inverno_2022.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())
  else:
    print('This Year isnt in range')

# median_Quantity(2021)
# print('\n')
# median_Quantity(2022)

# print(Base_Dados.groupby('data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())

#                                         analisando feriados no verão

analise_media_quantidade = feriado_verao.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['min', 'max', 'sum', np.mean])

analise_media_temperatura = feriado_verao.groupby(by='data')['temperatura'].agg(['min', 'max', 'sum', np.mean])

print(analise_media_quantidade)
print('\n')
print(analise_media_temperatura)



