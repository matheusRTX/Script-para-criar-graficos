import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
df = pd.read_excel('dados/dados_dispersao.xlsx')

plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# Criar gráfico de dispersão Altura vs Peso
sns.scatterplot(
    data=df, 
    x='altura_cm', 
    y='peso_kg', 
    hue='sexo', 
    style='sexo',
    s=70, 
    palette='Set1'
)

plt.title('Relação entre Altura e Peso por Sexo', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Altura (cm)', fontsize=12)
plt.ylabel('Peso (kg)', fontsize=12)
plt.legend(title='Sexo')

plt.tight_layout()
plt.savefig('grafico_dispersao.png', dpi=300)
plt.show()
