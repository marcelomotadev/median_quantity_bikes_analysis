import pandas as pd
import numpy as np

data = pd.read_csv('bicicletas.csv')

data_verao = data.query('(estacao == "verao")')

data_verao_feriado = data.query('(estacao == "verao") & (feriado == 1)')

# data_verao_feriado_00 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "0:00:00")')
# data_verao_feriado_01 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "1:00:00")')
# data_verao_feriado_02 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "2:00:00")')
# data_verao_feriado_03 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "3:00:00")')
# data_verao_feriado_04 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "4:00:00")')
# data_verao_feriado_05 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "5:00:00")')
# data_verao_feriado_06 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "6:00:00")')
# data_verao_feriado_07 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "7:00:00")')
# data_verao_feriado_08 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "8:00:00")')
# data_verao_feriado_09 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "9:00:00")')
# data_verao_feriado_10 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "10:00:00")')
# data_verao_feriado_11 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "11:00:00")')
# data_verao_feriado_12 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "12:00:00")')
# data_verao_feriado_13 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "13:00:00")')
# data_verao_feriado_14 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "14:00:00")')
# data_verao_feriado_15 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "15:00:00")')
# data_verao_feriado_16 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "16:00:00")')
# data_verao_feriado_17 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "17:00:00")')
# data_verao_feriado_18 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "18:00:00")')
# data_verao_feriado_19 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "19:00:00")')
# data_verao_feriado_20 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "20:00:00")')
# data_verao_feriado_21 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "21:00:00")')
# data_verao_feriado_22 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "22:00:00")')
# data_verao_feriado_23 = data.query('(estacao == "verao") & (feriado == 1) & (hora == "23:00:00")')


# print(data_verao.describe())
print(data_verao_feriado.groupby(by='data')['quantidade_de_bikes_utilizadas'].agg(['sum', 'max', np.mean]))
print(data_verao_feriado.groupby(by='data')['temperatura'].agg(['min' , 'max', np.mean]))


