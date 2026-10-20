import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
df = pd.read_excel('dados/dados_linhas.xlsx')

plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

# Criar gráfico de linha com evolução temporal por loja
sns.lineplot(
    data=df, 
    x='data', 
    y='vendas', 
    hue='loja', 
    marker='o', 
    linewidth=2
)

plt.title('Evolução Temporal de Vendas por Loja', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Vendas (R$)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Loja')

plt.tight_layout()
plt.savefig('grafico_linhas.png', dpi=300)
plt.show()
