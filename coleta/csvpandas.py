import pandas as pd

dados = pd.read_csv('05dados_tratados_ponto_e_virgula.csv', sep=';')

pd.set_option('display.max_columns', None)

print(dados.head(6))

produto = dados[['nome','source']]

vendedor = dados['vendedor']

detalhes_produto = dados[['Avaliação','reviews','preco_antigo','preco_atual','data']]

produto.to_csv('produto.csv', index= False, sep=';')

detalhes_produto.to_csv('detalhes_produto.csv', index= False, sep=';')

vendedor.to_csv('vendedor.csv', index= False, sep=';')