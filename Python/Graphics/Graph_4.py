import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Converter a coluna 'Date' para o formato de data
data['Date'] = pd.to_datetime(data['Date'])

# Criar uma nova coluna 'Year' para armazenar o ano
data['Year'] = data['Date'].dt.year

# Criar subplots para comparar as variações no GDP durante os períodos de recessão e não recessão
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10), sharex=True)

# Plot para o período de recessão
sns.lineplot(ax=axes[0], x='Year', y='GDP', data=data[data['Recession'] == 1], marker='o', color='r')
axes[0].set_title('Variação no GDP durante Períodos de Recessão')
axes[0].set_ylabel('GDP')

# Plot para o período não recessivo
sns.lineplot(ax=axes[1], x='Year', y='GDP', data=data[data['Recession'] == 0], marker='o', color='b')
axes[1].set_title('Variação no GDP durante Períodos Não Recessivos')
axes[1].set_xlabel('Ano')
axes[1].set_ylabel('GDP')

plt.tight_layout()
plt.show()
