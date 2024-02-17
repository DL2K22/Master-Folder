# Exercício 2 - Crie uma célula markdown com o título do notebook. (1 ponto)
print("## Tarefa Notebook")

# Exercício 3 - Crie uma célula markdown para uma introdução. (1 pt)
print("## Introduction\nTarefa realizada com o intuito de ser avaliado e adquirir nota para a avaliação")

# Exercice 4 - Crie uma célula markdown para listar as linguagens de ciência de dados. (3 pts)
print("## Langages de Science des Données")
print("- Python")
print("- R")
print("- Java")

# Exercício 5 - Crie uma célula markdown para listar bibliotecas de ciência de dados. (3 pts)
print("## Bibliotecas utilizadas em ciencias de dados:")
print("- Pandas")
print("- NumPy")
print("- Matplotlib")

# Exercício 6 - Crie uma célula markdown com uma tabela de ferramentas de ciência de dados. (3 pts)
import pandas as pd
# Dados para a tabela
dados = {'Nome': ['Jupyter', 'TensorFlow', 'Scikit-learn'],
         'Descrição': ['Ferramenta para calculo interativo', 'Biblioteca para automação de dados', 'biblioteca de aprendizado de máquina']}
# Criando um DataFrame a partir dos dados
tabela = pd.DataFrame(dados)
# Exibindo a tabela
print(tabela)

# Exercício 7 - Crie uma célula markdown apresentando exemplos de expressões aritméticas. (1 pt)
print("## Exemplos de Expressões Aritméticas\nAgora veremos alguns exemplos de expressões aritméticas.")

# Exercício 8 - Crie uma célula de código para multiplicar e adicionar números. (2 pts)
a = 5
b = 3
print("Resultado da multiplicação :", a * b)
print("Resultado da soma :", a + b)

# Exercício 9 - Crie uma célula de código para converter minutos em horas. (2 pts)
minutes = 150
heures = minutes / 60
print(minutes, "minutos equivale a", heures, "horas.")

# Exercício 10 - Insira uma célula markdown para listar Objetivos. (3 pts)
print("## Objetivos")
print("- Explore conceitos de ciência de dados.")
print("- Pratique usando o Jupyter Notebook.")
print("- Aprenda a manipular dados com Python.")

# Exercice 11 - (2 points)
print("## Author\nLucas")

