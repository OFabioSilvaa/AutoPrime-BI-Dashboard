import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configurar estilo profissional com fundo escuro
plt.style.use('dark_background')
sns.set_palette("husl")

# Cores profissionais para fundo escuro
colors = {
    'primary': '#FFFFFF',
    'secondary': '#E5E7EB', 
    'accent': '#3B82F6',
    'success': '#10B981',
    'warning': '#F59E0B',
    'danger': '#EF4444',
    'info': '#06B6D4'
}

# Carregar os dados
df = pd.read_csv('/home/ubuntu/autprime_data.csv')

# 1. Análise de Descontos por Cliente
plt.figure(figsize=(16, 10))
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(20, 16))
fig.patch.set_facecolor('#000000')

# Gráfico 1: Distribuição de Ofertas de Desconto
desconto_counts = df['oferta_desconto'].value_counts()
ax1.pie(desconto_counts.values, labels=desconto_counts.index, autopct='%1.1f%%', 
        startangle=90, colors=[colors['accent'], colors['success'], colors['warning'], colors['info']])
ax1.set_title('Distribuição de Ofertas de Desconto\nPortfólio de Benefícios', 
              fontsize=16, fontweight='bold', color='white', pad=20)

# Gráfico 2: Top 15 Clientes com Descontos
cliente_desconto = df.groupby(['nome', 'oferta_desconto']).agg({
    'valor_pago': 'sum',
    'nome': 'count'
}).rename(columns={'nome': 'total_alugueis'}).reset_index()
top_clientes_desconto = cliente_desconto.nlargest(15, 'total_alugueis')

bars = ax2.barh(range(len(top_clientes_desconto)), top_clientes_desconto['total_alugueis'], 
                color=[colors['accent'] if 'sem' in str(desc).lower() else colors['success'] 
                       for desc in top_clientes_desconto['oferta_desconto']])
ax2.set_yticks(range(len(top_clientes_desconto)))
ax2.set_yticklabels(top_clientes_desconto['nome'], fontsize=10)
ax2.set_xlabel('Total de Aluguéis', fontsize=12, fontweight='bold', color='white')
ax2.set_title('Top 15 Clientes por Volume\nStatus de Desconto', 
              fontsize=16, fontweight='bold', color='white', pad=20)
ax2.grid(axis='x', alpha=0.3)

# Adicionar valores nas barras
for i, bar in enumerate(bars):
    width = bar.get_width()
    desconto = top_clientes_desconto.iloc[i]['oferta_desconto']
    ax2.text(width + 0.1, bar.get_y() + bar.get_height()/2, 
             f'{int(width)} ({desconto})', ha='left', va='center', 
             fontweight='bold', color='white', fontsize=9)

# Gráfico 3: Receita por Tipo de Desconto
receita_desconto = df.groupby('oferta_desconto')['valor_pago'].sum().sort_values(ascending=True)
bars3 = ax3.barh(range(len(receita_desconto)), receita_desconto.values, 
                 color=sns.color_palette("plasma", len(receita_desconto)))
ax3.set_yticks(range(len(receita_desconto)))
ax3.set_yticklabels(receita_desconto.index, fontsize=12)
ax3.set_xlabel('Receita Total (R$)', fontsize=12, fontweight='bold', color='white')
ax3.set_title('Receita por Tipo de Desconto\nImpacto Financeiro dos Benefícios', 
              fontsize=16, fontweight='bold', color='white', pad=20)
ax3.grid(axis='x', alpha=0.3)

# Adicionar valores formatados
for i, bar in enumerate(bars3):
    width = bar.get_width()
    ax3.text(width + max(receita_desconto.values)*0.01, bar.get_y() + bar.get_height()/2, 
             f'R$ {width:,.0f}', ha='left', va='center', fontweight='bold', color='white')

# Gráfico 4: Análise de Valor Médio por Desconto
valor_medio = df.groupby('oferta_desconto')['valor_pago'].mean().sort_values(ascending=False)
bars4 = ax4.bar(range(len(valor_medio)), valor_medio.values, 
                color=sns.color_palette("viridis", len(valor_medio)))
ax4.set_xticks(range(len(valor_medio)))
ax4.set_xticklabels(valor_medio.index, rotation=45, ha='right', fontsize=10)
ax4.set_ylabel('Valor Médio por Aluguel (R$)', fontsize=12, fontweight='bold', color='white')
ax4.set_title('Valor Médio por Tipo de Desconto\nTicket Médio por Segmento', 
              fontsize=16, fontweight='bold', color='white', pad=20)
ax4.grid(axis='y', alpha=0.3)

# Adicionar valores nas barras
for i, bar in enumerate(bars4):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2, height + max(valor_medio.values)*0.01, 
             f'R$ {height:,.0f}', ha='center', va='bottom', fontweight='bold', color='white')

plt.tight_layout()
plt.savefig('/home/ubuntu/analise_descontos.png', dpi=300, bbox_inches='tight', 
            facecolor='black', edgecolor='none')
plt.close()

# 2. Matriz de Clientes x Descontos (Heatmap)
plt.figure(figsize=(14, 10))
fig, ax = plt.subplots(figsize=(14, 10))
fig.patch.set_facecolor('#000000')

# Criar matriz de clientes vs descontos
top_20_clientes = df['nome'].value_counts().head(20).index
df_top_clientes = df[df['nome'].isin(top_20_clientes)]
matriz_desconto = df_top_clientes.groupby(['nome', 'oferta_desconto']).size().unstack(fill_value=0)

sns.heatmap(matriz_desconto, annot=True, fmt='d', cmap='YlOrRd', 
            cbar_kws={'label': 'Número de Aluguéis'}, ax=ax)
ax.set_title('Matriz Cliente x Tipo de Desconto\nTop 20 Clientes - Padrão de Benefícios', 
             fontsize=16, fontweight='bold', color='white', pad=20)
ax.set_xlabel('Tipo de Desconto', fontsize=12, fontweight='bold', color='white')
ax.set_ylabel('Cliente', fontsize=12, fontweight='bold', color='white')

plt.tight_layout()
plt.savefig('/home/ubuntu/matriz_clientes_descontos.png', dpi=300, bbox_inches='tight',
            facecolor='black', edgecolor='none')
plt.close()

print("Análises de desconto geradas com sucesso!")
print(f"Distribuição de descontos:")
for desconto, count in df['oferta_desconto'].value_counts().items():
    print(f"  {desconto}: {count} aluguéis ({count/len(df)*100:.1f}%)")

