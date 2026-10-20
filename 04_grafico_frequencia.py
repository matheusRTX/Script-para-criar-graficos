import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
df = pd.read_excel('dados/dados_frequencia.xlsx')

# Contagem de ocorrências
df_freq = df['tipo_atendimento'].value_counts().reset_index()
df_freq.columns = ['tipo_atendimento', 'frequencia']

plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# Criar gráfico de frequência
ax = sns.barplot(
    data=df_freq, 
    x='tipo_atendimento', 
    y='frequencia', 
    palette='viridis'
)

# Adicionar rótulos nas barras
for p in ax.patches:
    ax.annotate(
        f'{int(p.get_height())}', 
        (p.get_x() + p.get_width() / 2., p.get_height()), 
        ha='center', va='bottom', fontsize=11, fontweight='bold', xytext=(0, 5), 
        textcoords='offset points'
    )

plt.title('Frequência de Tipos de Atendimento / Chamados', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Tipo de Atendimento', fontsize=12)
plt.ylabel('Quantidade de Chamados', fontsize=12)

plt.tight_layout()
plt.savefig('grafico_frequencia.png', dpi=300)
plt.show()
