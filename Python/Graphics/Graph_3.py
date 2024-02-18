import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Converter a coluna 'Date' para o formato de data
data['Date'] = pd.to_datetime(data['Date'])

# Criar uma nova coluna 'Year' para armazenar o ano
data['Year'] = data['Date'].dt.year

# Criar o gráfico de linha com diferentes linhas para cada tipo de veículo e distinguir entre períodos de recessão e não recessão
plt.figure(figsize=(12, 8))
sns.lineplot(x='Year', y='Automobile_Sales', hue='Vehicle_Type', style='Recession', data=data, marker='o', palette='tab10')
plt.title('Vendas de Automóveis por Tipo de Veículo durante Recessão e Não Recessão')
plt.xlabel('Ano')
plt.ylabel('Vendas de Automóveis')
plt.grid(True)
plt.legend(title='Tipo de Veículo')
plt.show()
