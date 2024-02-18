import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Converter a coluna 'Date' para o formato de data
data['Date'] = pd.to_datetime(data['Date'])

# Criar uma nova coluna 'Year' para armazenar o ano
data['Year'] = data['Date'].dt.year

# Filtrar os dados durante os períodos de recessão
recession_data = data[data['Recession'] == 1]

# Calcular a média do preço do veículo para cada ano durante os períodos de recessão
average_price_by_year = recession_data.groupby('Year')['Price'].mean().reset_index()

# Criar o scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(average_price_by_year['Price'], recession_data.groupby('Year')['Automobile_Sales'].sum(), color='blue', alpha=0.7)

plt.title('Correlação entre Preço Médio do Veículo e Volume de Vendas durante Recessões')
plt.xlabel('Preço Médio do Veículo')
plt.ylabel('Volume de Vendas de Automóveis')
plt.grid(True)
plt.show()
