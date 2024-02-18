import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Converter a coluna 'Date' para o formato de data
data['Date'] = pd.to_datetime(data['Date'])

# Criar uma nova coluna 'Year' para armazenar o ano
data['Year'] = data['Date'].dt.year

# Criar um Bubble plot para mostrar o impacto da sazonalidade nas vendas de automóveis
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Year', y='Automobile_Sales', size='Seasonality_Weight', hue='Seasonality_Weight', data=data, sizes=(20, 200), palette='viridis', alpha=0.7)

plt.title('Impacto da Sazonalidade nas Vendas de Automóveis')
plt.xlabel('Ano')
plt.ylabel('Vendas de Automóveis')
plt.legend(title='Peso da Sazonalidade')
plt.show()
