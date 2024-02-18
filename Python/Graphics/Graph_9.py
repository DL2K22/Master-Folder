import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Filtrar os dados para incluir apenas os períodos de recessão
recession_data = data[data['Recession'] == 1]

# Criar o gráfico de linha para analisar o efeito da taxa de desemprego no tipo de veículo e nas vendas durante o período de recessão
plt.figure(figsize=(12, 8))
sns.lineplot(x='Year', y='Automobile_Sales', hue='Vehicle_Type', style='unemployment_rate', markers=True, data=recession_data)

plt.title('Efeito da Taxa de Desemprego no Tipo de Veículo e nas Vendas durante a Recessão')
plt.xlabel('Ano')
plt.ylabel('Vendas de Automóveis')
plt.legend(title='Taxa de Desemprego')
plt.show()
