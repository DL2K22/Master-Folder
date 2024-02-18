import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Converter a coluna 'Date' para o formato de data
data['Date'] = pd.to_datetime(data['Date'])

# Criar uma nova coluna 'Year' para armazenar o ano
data['Year'] = data['Date'].dt.year

# Agrupar as vendas por ano
sales_by_year = data.groupby('Year')['Automobile_Sales'].sum().reset_index()

# Criar o gráfico de linha
plt.figure(figsize=(10, 6))
plt.plot(sales_by_year['Year'], sales_by_year['Automobile_Sales'], marker='o', linestyle='-')
plt.title('Vendas de Automóveis ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Vendas de Automóveis')
plt.grid(True)
plt.show()
