import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
df = pd.read_excel('dados/dados_pizza.xlsx')

plt.figure(figsize=(8, 8))

# Criar gráfico de pizza/rosca
colors = sns.color_palette('pastel')[0:len(df)]
wedges, texts, autotexts = plt.pie(
    df['faturamento'], 
    labels=df['canal_venda'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors,
    wedgeprops=dict(width=0.4, edgecolor='w')
)

plt.setp(autotexts, size=11, weight="bold")
plt.title('Distribuição do Faturamento por Canal de Venda', fontsize=14, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('grafico_pizza.png', dpi=300)
plt.show()
