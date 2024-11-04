import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para carregar os dados
def carregar_dados():
    # Aqui você deve colocar o caminho do arquivo CSV gerado anteriormente
    df = pd.read_csv('dados_presenca.csv')
    df['Data'] = pd.to_datetime(df['Data'])
    return df

# Função para analisar a frequência de presenças por dia da semana
def analise_frequencia_por_dia(df):
    df['Dia da Semana'] = df['Data'].dt.day_name()
    frequencia_dias = df.groupby('Dia da Semana').size().reindex([
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    ]).fillna(0)
    
    plt.figure(figsize=(10,6))
    sns.barplot(x=frequencia_dias.index, y=frequencia_dias.values, palette='YlOrBr')
    plt.title('Frequência de Presenças por Dia da Semana')
    plt.xlabel('Dia da Semana')
    plt.ylabel('Número de Presenças')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('frequencia_dias_semana.png')
    plt.show()

# Função para analisar a frequência de presenças por modalidade
def analise_frequencia_por_modalidade(df):
    frequencia_modalidade = df['Modalidade'].value_counts()
    
    plt.figure(figsize=(10,6))
    sns.barplot(x=frequencia_modalidade.index, y=frequencia_modalidade.values, palette='YlOrBr')
    plt.title('Frequência de Presenças por Modalidade')
    plt.xlabel('Modalidade')
    plt.ylabel('Número de Presenças')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('frequencia_modalidades.png')
    plt.show()

# Função para analisar o status de pagamento
def analise_pagamentos(df):
    pagamentos = df.groupby(['Modalidade', 'Pagamento Mensalidade']).size().unstack(fill_value=0)
    
    pagamentos.plot(kind='bar', stacked=True, figsize=(10,6), colormap='YlOrBr')
    plt.title('Status de Pagamento por Modalidade')
    plt.xlabel('Modalidade')
    plt.ylabel('Número de Alunos')
    plt.xticks(rotation=45)
    plt.legend(title='Pagamento Mensalidade')
    plt.tight_layout()
    plt.savefig('pagamentos_modalidades.png')
    plt.show()

# Função principal para executar as análises
def main():
    df = carregar_dados()
    analise_frequencia_por_dia(df)
    analise_frequencia_por_modalidade(df)
    analise_pagamentos(df)

if __name__ == "__main__":
    main()
