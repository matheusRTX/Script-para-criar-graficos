import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados
df = pd.read_excel('dados/dados_heatmap.xlsx')

# Criar tabela dinâmica (Pivot Table) para a matriz do heatmap
df_pivot = df.pivot(index='dia_semana', columns='horario', values='movimento_clientes')

# Ordenar dias da semana
dias_ordem = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
df_pivot = df_pivot.reindex([d for d in dias_ordem if d in df_pivot.index])

plt.figure(figsize=(10, 6))

# Plotar Heatmap
sns.heatmap(df_pivot, annot=True, fmt='d', cmap='YlOrRd', cbar_kws={'label': 'Movimento de Clientes'})

plt.title('Mapa de Calor: Movimento de Clientes por Dia e Horário', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Horário', fontsize=12)
plt.ylabel('Dia da Semana', fontsize=12)

plt.tight_layout()
plt.savefig('grafico_heatmap.png', dpi=300)
plt.show()
