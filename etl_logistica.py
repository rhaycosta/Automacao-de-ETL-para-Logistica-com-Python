import pandas as pd

print("--- 1. EXTRAÇÃO (Lendo o arquivo sujo) ---")
try:
    # ATENÇÃO: Usei o nome do arquivo que apareceu no seu terminal
    df = pd.read_csv('dados_logistica_brutos.csv', encoding='utf-8', sep=',')
    print("Arquivo carregado com sucesso!")
except FileNotFoundError:
    print("Erro: O arquivo 'dados_logistica_brutos.csv' não foi encontrado.")
    exit()

print("--- 2. TRANSFORMAÇÃO (Limpeza) ---")

# A. Datas
df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], errors='coerce', dayfirst=True)
df = df.dropna(subset=['Data_Pedido'])

# B. Números (Peso)
df['Peso_kg'] = df['Peso_kg'].astype(str).str.replace('kg', '', regex=False).str.strip()
df['Peso_kg'] = pd.to_numeric(df['Peso_kg'], errors='coerce')
df['Peso_kg'] = df['Peso_kg'].fillna(df['Peso_kg'].mean())

# C. Números (Frete)
df['Valor_Frete'] = df['Valor_Frete'].astype(str).str.replace('R$', '', regex=False).str.replace(',', '.')
df['Valor_Frete'] = pd.to_numeric(df['Valor_Frete'], errors='coerce')

# D. Textos (Status)
df['Status_Entrega'] = df['Status_Entrega'].fillna('Não Informado')
df['Status_Entrega'] = df['Status_Entrega'].str.upper().str.strip()

# --- NOVO: E. Padronização de Cidades ---
print("Padronizando nomes das cidades...")
correcoes = {
    'sao paulo': 'São Paulo, SP',
    'BH - Minas': 'Belo Horizonte, MG',
    'Curitiba - PR': 'Curitiba, PR'
}
# O replace corrige baseado no dicionário acima
df['Cidade_Destino'] = df['Cidade_Destino'].replace(correcoes)

print("--- 3. CARGA (Salvando Excel) ---")

# Formatação final
df['Data_Pedido'] = df['Data_Pedido'].dt.strftime('%d/%m/%Y')
df['Peso_kg'] = df['Peso_kg'].round(2)
df['Valor_Frete'] = df['Valor_Frete'].round(2)

nome_saida = 'tabela_logistica_limpa.xlsx'
df.to_excel(nome_saida, index=False)

print(f"SUCESSO! Arquivo '{nome_saida}' pronto para o BI.")