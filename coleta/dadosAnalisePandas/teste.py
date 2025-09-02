import pandas as pd

pd.set_option('display.max_columns', None)

dados = pd.read_csv(r"C:\Users\estudante\Desktop\Pedro\projetos\etl_analytics\coleta\coleta\dadosMySql\05dados_tratados_ponto_e_virgula.csv", sep=';')

#print(dados.head())

top1not = dados[dados['nome'] == "Notebook Samsung Galaxy Book4 Windows 11 Home Intel Core I3 8gb 256gb Ssd 15.6'' Full Hd Led 1.55 Kg Grafite"].sort_values(by='preco_antigo',ascending=False)

print(top1not)