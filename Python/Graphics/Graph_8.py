import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Filtrar os dados para incluir apenas os períodos de recessão
recession_data = data[data['Recession'] == 1]

# Calcular o total de despesas com publicidade para cada tipo de veículo durante os períodos de recessão
total_ad_exp_by_vehicle_type = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()

# Criar dados para o pie chart
labels = total_ad_exp_by_vehicle_type['Vehicle_Type']
sizes = total_ad_exp_by_vehicle_type['Advertising_Expenditure']
colors = plt.cm.Set3.colors  # Cores distintas para cada fatia

# Criar o pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Despesas Totais com Publicidade por Tipo de Veículo durante Recessão')

plt.show()
