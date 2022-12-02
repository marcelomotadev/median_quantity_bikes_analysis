import datetime
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime as dt
from datetime import date, timedelta
from datetime import datetime

Base_Dados = pd.read_csv('bicicletas.csv')

#                                         quantidade de feriados

feriado_outono = Base_Dados.query('(estacao == "outono") & (feriado == 1)')
feriado_inverno = Base_Dados.query('(estacao == "inverno") & (feriado == 1)')
feriado_verao = Base_Dados.query('(estacao == "verao") & (feriado == 1)')
feriado_primavera = Base_Dados.query('(estacao == "primavera") & (feriado == 1)')

# unique() -> retorna os dias nunique() -> retorna retorna quantidade 

feriados_outono = feriado_outono['data'].nunique()
feriados_inverno = feriado_inverno['data'].nunique()
feriados_verao = feriado_verao['data'].nunique()
feriados_primavera = feriado_primavera['data'].nunique()

# -------------------------------------------------------------------------------------------

# funcao para encontrar quantos dias comecam com 2021 em uma lista e quantos comecam com 2022

def encontra_dias(list):
  y = 0
  z = 0  
  for x in list:  
    if x.startswith('2021'):
      y +=1
    else:
      z +=1
  print('2021: ', y,'2022: ', z)

# -----------------------------------------------------------------------------------------

Base_Dados['data'] = pd.to_datetime( Base_Dados['data'])

Base_Dados['Ano'] = pd.DatetimeIndex( Base_Dados['data'] ).year

#                                         temperaturas médias



outono_2021 = Base_Dados.query('(estacao == "outono") & (Ano == 2021)')
print(outono_2021.groupby(by='data')['temperatura'].agg([np.mean]).mean())
primavera_2021 = Base_Dados.query('(estacao == "primavera") & (Ano == 2021)')
print(primavera_2021.groupby(by='data')['temperatura'].agg([np.mean]).mean())
verao_2021 = Base_Dados.query('(estacao == "verao") & (Ano == 2021)')
print(verao_2021.groupby(by='data')['temperatura'].agg([np.mean]).mean())
inverno_2021 = Base_Dados.query('(estacao == "inverno") & (Ano == 2021)')
print(inverno_2021.groupby(by='data')['temperatura'].agg([np.mean]).mean())

# print('\n')

outono_2022 = Base_Dados.query('(estacao == "outono") & (Ano == 2022)')
print('outono 2022: ', outono_2022.groupby(by='data')['temperatura'].agg([np.mean]).mean())
primavera_2022 = Base_Dados.query('(estacao == "primavera") & (Ano == 2022)')
print('primavera 2022: ', primavera_2022.groupby(by='data')['temperatura'].agg([np.mean]).mean())
verao_2022 = Base_Dados.query('(estacao == "verao") & (Ano == 2022)')
print('verao 2022: ', verao_2022.groupby(by='data')['temperatura'].agg([np.mean]).mean())
inverno_2022 = Base_Dados.query('(estacao == "inverno") & (Ano == 2022)')
print('inverno 2022: ', inverno_2022.groupby(by='data')['temperatura'].agg([np.mean]).mean())
print('\n')


#                                         quantidades médias


outono_2021 = Base_Dados.query('(estacao == "outono") & (Ano == 2021)')
print(outono_2021.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())
primavera_2021 = Base_Dados.query('(estacao == "primavera") & (Ano == 2021)')
print(primavera_2021.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())
verao_2021 = Base_Dados.query('(estacao == "verao") & (Ano == 2021)')
print(verao_2021.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())
inverno_2021 = Base_Dados.query('(estacao == "inverno") & (Ano == 2021)')
print(inverno_2021.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())

print('\n')

outono_2022 = Base_Dados.query('(estacao == "outono") & (Ano == 2022)')
print('outono 2022: ', outono_2022.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())
primavera_2022 = Base_Dados.query('(estacao == "primavera") & (Ano == 2022)')
print('primavera 2022: ', primavera_2022.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())
verao_2022 = Base_Dados.query('(estacao == "verao") & (Ano == 2022)')
print('verao 2022: ', verao_2022.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())
inverno_2022 = Base_Dados.query('(estacao == "inverno") & (Ano == 2022)')
print('inverno 2022: ', inverno_2022.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())
# print('\n')

print(Base_Dados.groupby('data')['quantidade_de_bikes_utilizadas'].agg(['sum']).mean())

#                                         analisando feriados no verão

analise_media_quantidade = feriado_verao.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['min', 'max', 'sum', np.mean])
print(analise_media_quantidade)
print('\n')
analise_media_temperatura = feriado_verao.groupby(by='data')['temperatura'].agg(['min', 'max', 'sum', np.mean])
print(analise_media_temperatura)
