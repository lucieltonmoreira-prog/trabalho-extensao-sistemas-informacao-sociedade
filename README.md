# trabalho-extensao-sistemas-informacao-sociedade
Análise de Impacto Social e Exclusão Informacional (Disciplina: Sistemas de Informação e Sociedade)
# Projeto de Extensão: Sistemas de Informação e Sociedade
Este repositório documenta o pipeline de dados utilizado para analisar o impacto da exclusão informacional em moradores de 50+ anos.

Fluxo de Trabalho (Pipeline)

1. Extração de Dados
Os dados foram coletados via Google Forms com 15 participantes e exportados para Excel. 

2. Tratamento com Python (Pandas)
Utilizei o PyCharm Community para processar os dados brutos. O script Python realiza:
Limpeza: Remoção de metadados desnecessários do formulário.
Seleção de Variáveis: Utilização do método `.iloc` para filtrar as colunas de impacto social.
Padronização: Renomeação de colunas e criação de uma métrica de contagem (`Quantidade`).

3. Visualização no Power BI
O arquivo tratado foi importado para o Power BI Desktop, onde criei um dashboard interativo para visualizar:
* O nível de desinformação histórica do grupo (93,3%).
* A correlação entre falta de informação e barreiras financeiras.
* A percepção de 100% de impacto positivo da internet.

 Ferramentas Utilizadas
* Python (Pandas)
* PyCharm Community 2024.3.5
* Microsoft Excel
* Power BI Desktop
