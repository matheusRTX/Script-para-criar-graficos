import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def tratar_valor_float(v):
    if isinstance(v, datetime.datetime):
        return float(f"{v.year}.{v.month:02d}")
    return float(v)

# Carregar e limpar dados
df = pd.read_excel('dados/dados_regressao.xlsx')
df['renda_mensal'] = df['renda_mensal'].apply(tratar_valor_float)
df['gasto_mensal'] = df['gasto_mensal'].apply(tratar_valor_float)

plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# Gráfico de dispersão com linha de regressão linear
sns.regplot(
    data=df, 
    x='renda_mensal', 
    y='gasto_mensal', 
    scatter_kws={'alpha': 0.7, 'color': '#2b5c8f'}, 
    line_kws={'color': '#e74c3c', 'linewidth': 2}
)

plt.title('Regressão Linear: Renda Mensal vs Gasto Mensal', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Renda Mensal (R$)', fontsize=12)
plt.ylabel('Gasto Mensal (R$)', fontsize=12)

plt.tight_layout()
plt.savefig('grafico_regressao.png', dpi=300)
plt.show()
