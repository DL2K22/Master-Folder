import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Calcular o total de despesas com publicidade durante os períodos de recessão e não recessão
total_ad_exp_recession = data[data['Recession'] == 1]['Advertising_Expenditure'].sum()
total_ad_exp_non_recession = data[data['Recession'] == 0]['Advertising_Expenditure'].sum()

# Criar dados para o pie chart
labels = ['Recessão', 'Não Recessão']
sizes = [total_ad_exp_recession, total_ad_exp_non_recession]
colors = ['lightcoral', 'lightblue']
explode = (0.1, 0)  # Explodir a fatia da recessão para destacá-la

# Criar o pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Despesas com Publicidade de XYZAutomotives durante Recessão e Não Recessão')

plt.show()
