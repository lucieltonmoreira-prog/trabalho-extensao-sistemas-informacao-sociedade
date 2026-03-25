import pandas as pd

df = pd.read_excel(r'C:\Users\lucie\Downloads\Trabalho_Sistemas_Informacao.xlsx')

# Selecionando somente as colunas das perguntas
df = df.iloc[:, [4, 5, 6, 7]]

# Renomeando as colunas para melhor visualização
df.columns = ['Nivel_Conhecimento', 'Canais_Informacao', 'Impedimento_Estudos', 'Impacto_Internet']

# Criando uma coluna de contagem para facilitar no Power BI
df['Quantidade'] = 1


df.to_excel("dados_coletados_tratados.xlsx", index=False)
print("Sucesso! O arquivo dados_coletados_tratados.xlsx foi gerado.")


