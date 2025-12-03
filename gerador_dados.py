import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configuração para reprodutibilidade
np.random.seed(42)
random.seed(42)

# Gerar 200 linhas de dados
n_rows = 200
ids = range(1001, 1001 + n_rows)

# Cidades com erros de padronização propositais
cidades = [
    'São Paulo, SP', 'Rio de Janeiro, RJ', 'Belo Horizonte, MG', 'Curitiba, PR',
    'Porto Alegre, RS', 'Salvador, BA', 'Recife, PE', 'Brasília, DF',
    'sao paulo', 'BH - Minas', 'Curitiba - PR'
]

status_list = ['Entregue', 'Em Trânsito', 'Pendente', 'Cancelado', None]

data = {
    'ID_Pedido': ids,
    'Data_Pedido': [],
    'Cidade_Destino': [],
    'Peso_kg': [],
    'Valor_Frete': [],
    'Status_Entrega': []
}

for _ in range(n_rows):
    # Data: Aleatória, misturando formatos (BR, ISO e erros)
    date = datetime.now() - timedelta(days=random.randint(0, 60))
    rand = random.random()
    if rand < 0.1:
        data['Data_Pedido'].append(date.strftime('%d/%m/%Y')) # BR
    elif rand < 0.2:
        data['Data_Pedido'].append(date.strftime('%Y-%m-%d')) # ISO
    elif rand < 0.25:
        data['Data_Pedido'].append("Data Inválida") # Erro Crítico
    else:
        data['Data_Pedido'].append(date.strftime('%d-%m-%Y'))

    data['Cidade_Destino'].append(random.choice(cidades))

    # Peso: Misturando números com texto ("10kg") e nulos
    if random.random() < 0.05:
        data['Peso_kg'].append(None)
    elif random.random() < 0.1:
        data['Peso_kg'].append(f"{random.randint(1,50)}kg")
    else:
        data['Peso_kg'].append(round(random.uniform(0.5, 50.0), 2))

    # Frete: Colocando "R$" para sujar a coluna numérica
    peso_val = data['Peso_kg'][-1]
    try:
        val = float(str(peso_val).replace("kg",""))
        frete = val * 1.5 + random.uniform(10, 50)
        if random.random() < 0.2:
            data['Valor_Frete'].append(f"R$ {frete:.2f}")
        else:
            data['Valor_Frete'].append(round(frete, 2))
    except:
        data['Valor_Frete'].append(None)

    data['Status_Entrega'].append(random.choice(status_list))

df = pd.DataFrame(data)
# Duplicar as primeiras 10 linhas para simular erro de sistema
df = pd.concat([df, df.iloc[:10]])

# Salvar o arquivo "problema"
df.to_csv('dados_logistica_brutos.csv', index=False)
print("Arquivo 'dados_logistica_brutos.csv' gerado com sucesso!")