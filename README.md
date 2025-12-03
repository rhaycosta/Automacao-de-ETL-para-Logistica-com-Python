# 🚚 Automação de ETL para Logística com Python

> **Status do Projeto:** Concluído ✅

## 📋 Sobre o Projeto

Este projeto foi desenvolvido para resolver um problema recorrente na área de logística: o recebimento de relatórios de frete em formatos não padronizados (CSV "sujos"), que exigiam horas de tratamento manual no Excel.

Criei um script em **Python** que realiza todo o processo de **ETL (Extract, Transform, Load)** automaticamente. O script lê os dados brutos, aplica regras de negócio para limpeza e exporta uma planilha pronta para ser consumida por ferramentas de BI (Power BI/Tableau) ou Excel.

### 🎯 O Problema Resolvido
- **Antes:** CSV com separadores errados, encoding quebrado (UTF-8 vs ANSI), datas misturadas (PT-BR/EN-US) e nomes de cidades inconsistentes (ex: "sp", "São Paulo", "sao paulo").
- **Depois:** Arquivo `.xlsx` formatado, com datas padronizadas, valores numéricos convertidos corretamente e cidades normalizadas.

## 🛠 Tecnologias Utilizadas

* **Python 3.x**
* **Pandas** (Manipulação e tratamento de dados)
* **OpenPyXL** (Exportação para Excel)
* **VS Code** (IDE)

## ⚙️ Funcionalidades do Script

O código `etl_logistica.py` executa o seguinte pipeline:

1.  **Extração (Extract):**
    * Leitura de arquivos CSV ignorando erros de encoding.
    * Identificação automática de separadores.

2.  **Transformação (Transform):**
    * 🧹 **Limpeza de Strings:** Remoção de caracteres especiais (R$, kg) e espaços vazios.
    * 📅 **Tratamento de Datas:** Conversão segura de strings para `datetime`, lidando com erros ('coerce').
    * 💰 **Conversão Numérica:** Transformação de valores monetários e pesos para `float` e preenchimento de nulos (fillna) com a média.
    * 📍 **Padronização (De/Para):** Dicionário para corrigir nomes de cidades (ex: 'BH - Minas' -> 'Belo Horizonte, MG').

3.  **Carga (Load):**
    * Exportação para Excel (`.xlsx`) limpo e organizado.

## 🚀 Como Rodar o Projeto

Pré-requisitos: Python instalado.

```bash
# 1. Clone o repositório
git clone [https://github.com/](https://github.com/)[SEU-USUARIO]/[NOME-DO-REPO].git

# 2. Instale as dependências
pip install pandas openpyxl

# 3. Gere os dados de teste (opcional, pois simula o arquivo da transportadora)
python gerar_dados.py

# 4. Execute o script de ETL
python etl_logistica.py
