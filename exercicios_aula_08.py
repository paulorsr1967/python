import pandas as pd
import numpy as np
print(pd.__version__)

petr4 = pd.Series([22.29, 21.12, 20.48, 20.67, 21.92],
                  index = ['Mar 05', 'Mar 04', 'Mar 03', 'Mar 02', 'Mar 01'])
print(petr4)
dollar = 5.19
petr4_dollar = petr4 / dollar
print(petr4_dollar)
populacao_dicionario = {'São Paulo': 12.25, 'Guarulhos': 1.38, 'Santo Andre': 0.72}
populacao_serie = pd.Series(populacao_dicionario, index = ['Guarulhos', 'Santo Andre', 'São Paulo', 'São Roque'])
print(populacao_serie)
print(populacao_serie[populacao_serie.isnull()])
print(populacao_serie[populacao_serie.notnull()])
pop_dic = {'São Paulo': 12.25, 'Guarulhos': 1.38, 'Santo Andre': 0.72}
area_dic = {'Santo Andre' : 175, 'Osasco': 65, 'São Paulo': 1521, 'Guarulhos': 318}
pop = pd.Series(pop_dic)
area = pd.Series(area_dic)
print(pop * 1000000 / area)
dados = {
    'estado': ['SP', 'PB', 'RS'],
    'populacao': [45.54, 3.94, 11.29],
    'area': [249209, 56585, 281748]
        }
df = pd.DataFrame(dados, columns= ['populacao', 'area', 'estado', 'capital'])
print(df)
print(df.values)
print(df.columns)
print(df.index)
print(df['estado'])
print(df.area)
df2 = pd.DataFrame({
    'ibovespa': [110.335, 111.540, 111.184, 112.690, 115.202],
    'petr4': [21.92, 20.67, 20.48, 21.12, 22.29],
    'data': ['01-mar', '02-mar', '03-mar', '04-mar', '05-mar']
})
print(df2)
print(df2.dtypes)
print(df2.loc[0])
print(df2.loc[[2, 0], ['ibovespa', 'data']])
print(df2.loc[:, ['ibovespa', 'data']])
print(df2.loc[:, 'ibovespa':'data'])
df2.loc[1, 'petr4'] = 22.92
print(df2)
df2['nova_coluna'] = [0, 0, 0, 0, 0]
print(df2)
df2.ibovespa.astype(float)
print(df2)
df2['nova_coluna2'] = df2.petr4 * 5.16
print(df2)
df3 = df2.drop(['nova_coluna', 'nova_coluna2'], axis = 1 )
print(df3)
print(df3.loc[df3.ibovespa > 112, 'petr4'])
print(df3.loc[df3.ibovespa > 112, ['petr4']])
print(df3.petr4.max())
with open('petr4.csv') as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
df4 = pd.read_csv('petr4.csv', sep = ',')
print(df4)
print(df4.head(10))
print(df4.tail(10))
petr4 = pd.read_csv('petr4.csv')
ibovespa = pd.read_csv('ibovespa.csv')
print(ibovespa[ibovespa['Close'] == ibovespa['Close'].max()])
print(ibovespa[ibovespa['Close'] == ibovespa['Close'].min()])
data_max = ibovespa.loc[ibovespa['Close'] == ibovespa['Close'].max(), 'Date'].values[0]
data_min = ibovespa.loc[ibovespa['Close'] == ibovespa['Close'].min(), 'Date'].values[0]
print(data_max)
print(data_min)
print(petr4[petr4.Date == data_max])
print(petr4[petr4.Date == data_min])




