import pandas as pd
import matplotlib.pyplot as plt 
import re 
import io

dados_ecomerce = pd.read_csv(r"C:\Users\estudante\Desktop\Pedro\projetos\etl_analytics\coleta\coleta\dadosScrapytrans01delimitertrans02delimiter02.csv", delimiter=';')

pd.set_option('display.max_columns', None)
 
#print(dados_ecomerce.head())

# Analise 01: QUAL A VARIAÇÃO MEDIA DE PREÇO POR VENDEDOR:

#dados_ecomerce['variacao_preco'] = dados_ecomerce['preco_antigo'] - dados_ecomerce['preco_atual']
#
#var_preco_medio_vendedor = dados_ecomerce.groupby('vendedor')['variacao_preco'].mean().sort_values(ascending=False).reset_index()
#
#print(var_preco_medio_vendedor)
#
## GRAFICO
#
#fig = var_preco_medio_vendedor.plot(kind='bar',
#                                    x='vendedor',
#                                    y='variacao_preco',
#                                    title='Variação da Media de Preço', 
#                                    xlabel='Vendedor',
#                                    ylabel='Media da Variação do Preço',
#                                    rot=100,
#                                    figsize=(10,8))
#plt.show()

# Analise 02: QUAL A RELAÇÃO ENTRE AVALIAÇÃO E O NUMERO DE REVIEWS:

#fig = dados_ecomerce.plot(kind='scatter',
#                         x='reviews',
#                         y='Avaliação', 
#                         title='Relação entre Reviews e Avaliação',
#                         xlabel='Numero de Reviews',
#                         ylabel='Avaliação',
#                         figsize=(10,8),
#                         s=100,
#                         color= 'red')
#plt.show()

# Analise 03: DISTRIBUIÇÃO DOS PREÇOS:

#fig = dados_ecomerce.plot(kind='hist',
#                          y= 'preco_atual',
#                          bins= 6,
#                          title='Distribuição de Preços',
#                          xlabel='Preço Atual',
#                          ylabel='frequencia',
#                          figsize=(8,6))
#plt.show()

# Analise 04: QUAL O PREÇO MEDIO DOS NOTEBOOKS POR PROCESSADOR('I3','I5','I7'):
#def extract_processor(name):
#    processor_regex = re.search(r'(i[357]|ryzen\s?[357])', name, re.IGNORECASE)
#    if processor_regex:
#        return processor_regex.group(1).replace(' ', '').lower()
#    return 'Other'
#
## Cria a nova coluna 'processor'
#dados_ecomerce['processor'] = dados_ecomerce['nome'].apply(extract_processor)
#
#
## Calcula o preço médio agrupando por tipo de processador
#average_prices = dados_ecomerce.groupby('processor')['preco_atual'].mean().sort_values(ascending=False)
#
#
## Cria e salva o gráfico de barras
#plt.figure(figsize=(10, 6))
#average_prices.plot(kind='bar', color='skyblue')
#plt.title('Preço Médio de Notebooks por Tipo de Processador')
#plt.xlabel('Tipo de Processador')
#plt.ylabel('Preço Médio Atual (R$)')
#plt.xticks(rotation=0)
#plt.grid(axis='y', linestyle='--', alpha=0.7)
#plt.tight_layout()
#plt.savefig('average_price_per_processor.png')
#plt.show()



# nome     vendedor  Avaliação reviews  preco_antigo  preco_atual   source                        data