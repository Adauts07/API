import sqlite3
import pandas as pd
import os

# --- Configurações ---
NOME_BANCO_DE_DADOS = 'database.db'

# Lista de tarefas de processamento.
PROCESSAMENTO_TAREFAS = [
    {
        "caminho_dados": os.path.join('data', 'SEMOB'),
        "nome_tabela": "SEMOB"
    },
    {
        "caminho_dados": os.path.join('data', 'DER', 'velocidade'),
        "nome_tabela": "DER_VELOCIDADE"
    },
    {
        "caminho_dados": os.path.join('data', 'DER', 'fluxo'),
        "nome_tabela": "DER_FLUXO"
    },
    # {
    #     "caminho_dados": os.path.join('data', 'IBRAM'),
    #     "nome_tabela": "IBRAM"
    # }
]

def criar_banco_consolidado():
    """
    Processa uma lista de tarefas, consolidando arquivos de pastas específicas
    em tabelas nomeadas no banco de dados SQLite.
    """
    if os.path.exists(NOME_BANCO_DE_DADOS):
        os.remove(NOME_BANCO_DE_DADOS)
        print(f"Banco de dados antigo '{NOME_BANCO_DE_DADOS}' removido.")

    conn = sqlite3.connect(NOME_BANCO_DE_DADOS)
    print(f"Novo banco de dados '{NOME_BANCO_DE_DADOS}' criado.")

    for tarefa in PROCESSAMENTO_TAREFAS:
        caminho_pasta = tarefa["caminho_dados"]
        nome_tabela = tarefa["nome_tabela"]

        if not os.path.isdir(caminho_pasta):
            print(f"\nAVISO: Pasta '{caminho_pasta}' não encontrada. Pulando a tabela '{nome_tabela}'.")
            continue

        print(f"\nProcessando pasta '{caminho_pasta}' para a tabela '{nome_tabela}'...")

        lista_dfs = []
        
        todos_os_arquivos = os.listdir(caminho_pasta)
        arquivos_para_processar = []

        if nome_tabela.startswith("DER_"):
            arquivos_para_processar = todos_os_arquivos[:10]
            print(f"  -> LIMITADO a {len(arquivos_para_processar)} de {len(todos_os_arquivos)} arquivos para a tabela '{nome_tabela}'.")
        else:
            arquivos_para_processar = todos_os_arquivos

        for nome_arquivo in arquivos_para_processar:
            caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
            df_arquivo = None

            if nome_arquivo.endswith('.xlsx'):
                try:
                    df_arquivo = pd.read_excel(caminho_arquivo)
                    print(f"  Lido com sucesso: {nome_arquivo}")
                except Exception as e:
                    print(f"  ERRO ao ler {nome_arquivo}: {e}")
            elif nome_arquivo.endswith('.csv'):
                 try:
                    df_arquivo = pd.read_csv(caminho_arquivo)
                    print(f"  Lido com sucesso: {nome_arquivo}")
                 except Exception as e:
                    print(f"  ERRO ao ler {nome_arquivo}: {e}")

            if df_arquivo is not None:
                lista_dfs.append(df_arquivo)

        if lista_dfs:
            df_consolidado = pd.concat(lista_dfs, ignore_index=True)
            print(f"--> Todos os arquivos da pasta foram consolidados.")
            
            # --- LINHA CORRIGIDA ---
            # Adiciona o índice do DataFrame como uma coluna chamada 'id'
            df_consolidado.to_sql(nome_tabela, conn, if_exists='replace', index=True, index_label='id')
            
            print(f"--> Tabela '{nome_tabela}' criada com {len(df_consolidado)} linhas e uma coluna 'id'.")
        else:
            print(f"--> Nenhum arquivo de dados válido encontrado na pasta '{caminho_pasta}'.")

    conn.close()
    print("\nProcesso finalizado. Conexão com o banco de dados fechada.")

if __name__ == '__main__':
    criar_banco_consolidado()