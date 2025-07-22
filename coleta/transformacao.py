import json # Módulo para trabalhar com arquivos JSON
import re   # Módulo para expressões regulares (Regex), excelente para encontrar padrões em texto
import csv  # Módulo para trabalhar com arquivos CSV (caso precise)

caminhoJson = r"C:\Users\estudante\Desktop\Pedro\projetos\coleta\coleta\data.json" # Seu caminho para o arquivo JSON
caminhoCsv = r"C:\Users\estudante\Desktop\Pedro\projetos\coleta\coleta\data.csv"  # Seu caminho para o arquivo CSV

# --- 1. Funções de Carregamento de Dados ---
def carregar_dados_json(caminho_arquivo):
    """
    Função para carregar dados de um arquivo JSON.
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        return dados
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print(f"Erro: Não foi possível decodificar o JSON do arquivo '{caminho_arquivo}'. Verifique a formatação.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao carregar o JSON: {e}")
        return []

def carregar_dados_csv(caminho_arquivo):
    """
    Função para carregar dados de um arquivo CSV.
    """
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                dados.append(row)
        return dados
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao carregar o CSV: {e}")
        return []

# --- 2. Funções de Transformação Individuais ---

def remover_prefixo(texto, prefixo):
    """
    Remove um prefixo específico de uma string, se ele existir, e limpa espaços.
    **NOVIDADE:** Remove todos os caracteres de dois pontos (':') da string resultante.
    Exemplo: "Nome: Notebook" -> "Notebook"
              "Vendedor: Por: Loja" -> "Loja"
              "Texto: com: dois: pontos" -> "Texto com dois pontos"

    Argumentos:
        texto (str): A string original da qual o prefixo será removido.
        prefixo (str): O prefixo a ser removido.

    Retorna:
        str: A string sem o prefixo, sem dois pontos e com espaços extras removidos.
             Retorna a string original (com strip e sem :) se o prefixo não for encontrado.
    """
    if not isinstance(texto, str):
        return None
    
    # Remove o prefixo
    if texto.strip().startswith(prefixo):
        cleaned_text = texto.strip()[len(prefixo):].strip()
    else:
        cleaned_text = texto.strip() # Se o prefixo não for encontrado, usa o texto original limpo

    # Remove todos os caracteres de dois pontos (':') da string resultante
    return cleaned_text.replace(":", "")

def processar_preco(preco_str):
    """
    Converte uma string de preço (ex: "R$1.799", "R$1.799,00", "—") para um número float.
    Retorna float, ou 'Preço não encontrado' se for um traço ou inviável.
    """ 
    if not isinstance(preco_str, str):
        return None 
        
    preco_limpo_temp = preco_str.replace("R$", "").replace(" ", "").strip()

    if preco_limpo_temp == "—" or not preco_limpo_temp:
        return None

    match_numero = re.search(r'[\d\.,]+', preco_limpo_temp)
    if not match_numero:
        return None
    
    numero_bruto = match_numero.group(0)
    
    if ',' in numero_bruto and '.' in numero_bruto:
        if numero_bruto.rfind(',') > numero_bruto.rfind('.'):
            preco_limpo_final = numero_bruto.replace(".", "").replace(",", ".")
        else:
            preco_limpo_final = numero_bruto.replace(",", "") 
    elif ',' in numero_bruto:
        preco_limpo_final = numero_bruto.replace(",", ".")
    else:
        preco_limpo_final = numero_bruto
        
    try:
        return float(preco_limpo_final)
    except ValueError:
        print(f"ERRO CRÍTICO: Impossível converter '{preco_limpo_final}' (original: '{preco_str}') para float. Provável formato inesperado.")
        return None

def processar_reviews(reviews_str):
    """
    Extrai a avaliação numérica e o número total de reviews de uma string.
    Retorna tupla (avaliacao_float, reviews_int) ou strings de "não encontrado".
    """
    avaliacao = None
    reviews = None

    if not isinstance(reviews_str, str):
        return None, None

    if reviews_str.strip() == "Avaliação: — (— reviews)" or not reviews_str.strip():
        return None, None

    match_avaliacao = re.search(r'(\d+\.\d+)', reviews_str)
    if match_avaliacao:
        try:
            avaliacao = float(match_avaliacao.group(1))
        except ValueError:
            pass

    match_reviews = re.search(r'\((\d+)\s*reviews\)', reviews_str)
    if match_reviews:
        try:
            reviews = int(match_reviews.group(1))
        except ValueError:
            pass

    return (avaliacao if avaliacao else None,
            reviews if reviews else None)

# --- 3. Função Principal de Transformação de um Único Item ---
def transformar_item_notebook(item_original):
    """
    Transforma um dicionário de dados de notebook do formato original para o desejado.
    Esta versão REMOVE a chave 'pagina' e corrige o tratamento do 'vendedor' e a remoção de ':'.
    """
    item_transformado = {}

    # O campo 'nome' agora também terá os dois pontos removidos pela função remover_prefixo
    item_transformado['nome'] = remover_prefixo(item_original.get('nome', ''), "Nome: ")

    # --- LÓGICA CORRIGIDA PARA O TRATAMENTO DO VENDEDOR ---
    vendedor_original = item_original.get('vendedor', '').strip() # Pega e limpa a string original
    vendedor_final = None # Valor padrão caso nada seja encontrado

    # Tenta extrair com o prefixo mais específico "Vendedor: Por "
    if vendedor_original.startswith("Vendedor: Por "):
        # Extrai o nome após o prefixo e remove dois pontos
        extracted_name = vendedor_original[len("Vendedor: Por "):].strip().replace(":", "")
        if extracted_name: # Se algo significativo foi extraído
            vendedor_final = extracted_name
    # Se o prefixo específico não foi encontrado, tenta com o prefixo genérico ":"
    elif vendedor_original.startswith(":"): # Corrigi aqui para buscar "Vendedor: "
        # Extrai o nome após o prefixo e remove dois pontos
        extracted_name = vendedor_original[len("Vendedor: "):].strip().replace(":", "")
        if extracted_name: # Se algo significativo foi extraído
            vendedor_final = extracted_name
    # Se nenhum dos prefixos foi encontrado ou a extração resultou em string vazia,
    # 'vendedor_final' permanece como "Vendedor não encontrado".

    item_transformado['vendedor'] = vendedor_final

    # Outros campos
    avaliacao, reviews = processar_reviews(item_original.get('reviews', ''))
    item_transformado['Avaliação'] = avaliacao
    item_transformado['reviews'] = reviews

    item_transformado['preco_antigo'] = processar_preco(item_original.get('preco_antigo', ''))
    item_transformado['preco_atual'] = processar_preco(item_original.get('preco_atual', ''))

    return item_transformado

# --- 4. Função para Processar Todos os Dados ---
def transformar_todos_os_dados(lista_dados_originais):
    """
    Aplica a função de transformação 'transformar_item_notebook' a cada dicionário.
    """
    dados_transformados = []
    for item in lista_dados_originais:
        dados_transformados.append(transformar_item_notebook(item))
    return dados_transformados

# --- 5. Funções de Salvamento de Dados ---
def salvar_dados_json(dados, caminho_arquivo):
    """
    Salva uma lista de dicionários em um arquivo JSON.
    """
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        print(f"✅ Dados salvos com sucesso em: '{caminho_arquivo}'")
    except Exception as e:
        print(f"❌ Erro ao salvar o arquivo JSON '{caminho_arquivo}': {e}")

def salvar_dados_csv(dados, caminho_arquivo):
    """
    Salva uma lista de dicionários em um arquivo CSV.
    """
    if not dados:
        print("Nenhum dado para salvar no CSV.")
        return

    fieldnames = list(dados[0].keys())

    try:
        with open(caminho_arquivo, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dados)
        print(f"✅ Dados salvos com sucesso em: '{caminho_arquivo}'")
    except Exception as e:
        print(f"❌ Erro ao salvar o arquivo CSV '{caminho_arquivo}': {e}")


# --- 6. Bloco de Execução Principal (main) ---
if __name__ == "__main__":
    # --- Configurações de Caminho de Arquivo ---
    # Defina o caminho para o seu arquivo de entrada JSON
    #caminho_arquivo_entrada_json = caminhoJson
    
    # OPCIONAL: Defina o caminho para o seu arquivo de entrada CSV (descomente para usar)
    caminho_arquivo_entrada_csv = caminhoCsv

    #caminho_arquivo_saida_json = 'dados_notebooks_transformados_sem_pagina.json'
    # OPCIONAL: Defina o caminho para o arquivo de saída CSV (descomente para usar)
    caminho_arquivo_saida_csv = 'dados_teste_null.csv'

    print(f"Iniciando o processo de transformação de dados para notebooks do Mercado Livre...")
    print(f"Carregando dados...")

    # --- Escolha a Fonte de Dados de Entrada (JSON ou CSV) ---
    # Por padrão, o script carregará o JSON. Para usar o CSV, comente a linha do JSON
    # e descomente a linha do CSV abaixo.

    #dados_originais = carregar_dados_json(caminho_arquivo_entrada_json) 
    
    # # Exemplo de como carregar dados de um arquivo CSV (descomente as 2 linhas abaixo para usar):
    print(f"Carregando dados de: {caminho_arquivo_entrada_csv}")
    dados_originais = carregar_dados_csv(caminho_arquivo_entrada_csv)

    if not dados_originais:
        print("Nenhum dado foi carregado ou ocorreu um erro. Encerrando o script.")
    else:
        print(f"✅ {len(dados_originais)} itens carregados com sucesso.")

        print("Iniciando a transformação dos dados...")
        dados_transformados = transformar_todos_os_dados(dados_originais)
        print(f"✅ {len(dados_transformados)} itens transformados com sucesso.")

        #print(f"Salvando dados transformados em JSON: {caminho_arquivo_saida_json}")
        #salvar_dados_json(dados_transformados, caminho_arquivo_saida_json)

        # #Exemplo de como salvar dados transformados em um arquivo CSV (descomente a linha abaixo para usar):
        print(f"Salvando dados transformados em CSV: {caminho_arquivo_saida_csv}")
        salvar_dados_csv(dados_transformados, caminho_arquivo_saida_csv)

        print("\nProcesso de transformação e salvamento concluído! 🎉")

        print("\n🔍 Alguns itens transformados para verificação:")
        for i, item in enumerate(dados_transformados):
            if i < 5 or i >= len(dados_transformados) - 5: # Mostra os primeiros 5 e os últimos 5
                print(f"--- Item {i+1} ---")
                print(json.dumps(item, indent=2, ensure_ascii=False))
                if i == 4 and len(dados_transformados) > 10: # Se houver mais de 10 itens, mostra "..." no meio
                    print("...\n")