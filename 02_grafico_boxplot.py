import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def tratar_valor_float(v):
    if isinstance(v, datetime.datetime):
        return float(f"{v.year}.{v.month:02d}")
    return float(v)

# Carregar e limpar dados (tratar datas incorretas vindas do Excel)
df = pd.read_excel('dados/dados_boxplot.xlsx')
df['salario'] = df['salario'].apply(tratar_valor_float)

plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# Criar Boxplot de Salário por Departamento
sns.boxplot(
    data=df, 
    x='departamento', 
    y='salario', 
    palette='Blues'
)

plt.title('Distribuição Salarial por Departamento', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Departamento', fontsize=12)
plt.ylabel('Salário (R$)', fontsize=12)

plt.tight_layout()
plt.savefig('grafico_boxplot.png', dpi=300)
plt.show()
