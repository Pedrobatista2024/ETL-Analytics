import pandas as pd # type: ignore
import numpy as np
from datetime import datetime
import csv

dados_ecomerce = pd.read_csv(r"C:\Users\estudante\Desktop\Pedro\projetos\etl_analytics\coleta\coleta\dadosScrapytrans01delimiter.csv", delimiter=';')

pd.options.display.max_columns = None

dados_ecomerce['source'] = "https://lista.mercadolivre.com.br/notebooks"
dados_ecomerce['data'] = datetime.now()

#regra para remover todos o notebooks com dados faltantes
dados_ecomerce = dados_ecomerce.dropna()

dados_ecomerce['preco_atual'] = dados_ecomerce['preco_atual'] * 1000
dados_ecomerce['preco_antigo'] = dados_ecomerce['preco_antigo'] * 1000


dados_ecomerce = dados_ecomerce[(dados_ecomerce['preco_atual'] >= 1000) & (dados_ecomerce['preco_atual'] <= 10000)]

dados_ecomerce = dados_ecomerce.replace({np.nan: None})

dados_ecomerce = dados_ecomerce.to_dict(orient='records')

caminho_arquivo = r"C:\Users\estudante\Desktop\Pedro\projetos\etl_analytics\coleta\coleta\dadosScrapytrans01delimitertrans02.csv"

fieldnames = list(dados_ecomerce[0].keys())

try:
    with open(caminho_arquivo, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dados_ecomerce)
    print(f"✅ Dados salvos com sucesso em: '{caminho_arquivo}'")
except Exception as e:
    print(f"❌ Erro ao salvar o arquivo CSV '{caminho_arquivo}': {e}")

