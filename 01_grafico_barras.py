import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
df = pd.read_excel('dados/dados_barras.xlsx')

# Configurar estilo
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# Criar gráfico de barras agrupadas por Categoria e Região
ax = sns.barplot(
    data=df, 
    x='categoria', 
    y='vendas_medias', 
    hue='regiao', 
    palette='Set2'
)

# Customização
plt.title('Vendas Médias por Categoria e Região', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Vendas Médias (R$)', fontsize=12)
plt.legend(title='Região', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig('grafico_barras.png', dpi=300)
plt.show()
