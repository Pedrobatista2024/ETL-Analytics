import csv

def converter_delimitador_csv(caminho_entrada, caminho_saida):
    """
    Abre um arquivo CSV que usa vírgula (,) como delimitador, e o salva em um novo arquivo
    usando ponto e vírgula (;) como delimitador.
    **NOVIDADE:** Adiciona o Byte Order Mark (BOM) ao salvar em UTF-8 para melhor compatibilidade com o Excel.

    Argumentos:
        caminho_entrada (str): O caminho completo para o arquivo CSV de entrada (com vírgula como delimitador).
        caminho_saida (str): O caminho completo para o novo arquivo CSV de saída (com ponto e vírgula como delimitador).
    """
    try:
        linhas_do_csv = []

        with open(caminho_entrada, 'r', encoding='utf-8', newline='') as infile:
            reader = csv.reader(infile, delimiter=',')
            for row in reader:
                linhas_do_csv.append(row)

        if not linhas_do_csv:
            print(f"Aviso: O arquivo '{caminho_entrada}' está vazio. Nenhum dado para converter.")
            return

        # --- AQUI ESTÁ A MUDANÇA PARA ADICIONAR O BOM ---
        # Usamos 'utf-8-sig' que é 'utf-8' com o BOM incluído.
        with open(caminho_saida, 'w', encoding='utf-8-sig', newline='') as outfile:
            writer = csv.writer(outfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(linhas_do_csv)

        print(f"---")
        print(f"✅ Conversão de delimitador concluída com sucesso!")
        print(f"Arquivo de entrada (delimitador ',') : '{caminho_entrada}'")
        print(f"Arquivo de saída (delimitador ';', com BOM) : '{caminho_saida}'")
        print(f"---")

    except FileNotFoundError:
        print(f"---")
        print(f"❌ Erro: O arquivo de entrada '{caminho_entrada}' não foi encontrado.")
        print(f"---")
    except Exception as e:
        print(f"---")
        print(f"❌ Ocorreu um erro durante a conversão: {e}")
        print(f"---")

# --- Exemplo de Uso (igual ao anterior) ---
if __name__ == "__main__":
    CAMINHO_DO_SEU_CSV_ORIGINAL = r"C:\Users\estudante\Desktop\Pedro\projetos\coleta\coleta\dados_tratados.csv"
    CAMINHO_DO_NOVO_CSV_CORRIGIDO = r"C:\Users\estudante\Desktop\Pedro\projetos\coleta\coleta\dados_tratados_ponto_e_virgula.csv"
    
    converter_delimitador_csv(CAMINHO_DO_SEU_CSV_ORIGINAL, CAMINHO_DO_NOVO_CSV_CORRIGIDO)


    