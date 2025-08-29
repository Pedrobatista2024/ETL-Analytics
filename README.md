# 💻 Análise de Notebooks do Mercado Livre: Web Scraping e BI

Este projeto é uma solução completa de ponta a ponta para a análise de dados, cobrindo desde a **extração de dados da web (web scraping)** até a **visualização e análise final** em duas abordagens distintas. O objetivo principal é coletar,tratar dados de notebooks do site **Mercado Livre** e, em seguida, processá-los para extrair insights valiosos sobre preços, vendedores e avaliações.

---

## 🚀 Funcionalidades e Etapas do Projeto

O projeto segue um fluxo de trabalho bem definido, dividido nas seguintes etapas:

### 1. Extração de Dados (Web Scraping)

Utilizando o framework **Scrapy**, o projeto raspa a página de notebooks do Mercado Livre para coletar as seguintes informações:

* **Preço Antigo** e **Preço Atual**: Para analisar descontos.
* **Nome do Produto**: Descrição detalhada do notebook.
* **Vendedor**: Informações sobre a loja ou o vendedor.
* **Avaliação**: A nota ou rating do produto.

Os dados coletados são salvos em um arquivo `.csv` para a próxima fase.

### 2. Limpeza e Transformação (Data Wrangling)

Nesta etapa, as bibliotecas **Pandas** e **NumPy** são utilizadas para processar os dados brutos. As principais operações incluem:

* **Remoção de Prefixo**: Limpeza de caracteres indesejados nos dados de preço.
* **Mudança de Tipos**: Conversão de colunas numéricas (preço, avaliação) para o tipo correto.
* **Filtragem**: Remoção de dados irrelevantes ou duplicados.
* **Enriquecimento de Dados**: Adição de novas colunas, como um cálculo de desconto ou categoria.
* **Mudança de Delimitador**: Ajuste do arquivo CSV para um formato mais adequado.

### 3. Análise e Visualização

Após o tratamento, os dados são analisados de duas formas complementares:

#### **Abordagem 1: Business Intelligence (BI)**

* **Modelagem de Dados**: Os dados são modelados e carregados em um banco de dados **MySQL**.
* **Análise com Power BI**: O banco de dados é conectado ao **Power BI** para a criação de painéis e gráficos interativos, permitindo uma análise aprofundada dos preços, vendedores e avaliações de forma visual.

#### **Abordagem 2: Análise Exploratória com Python**

* **Análise com Python**: Uma análise exploratória detalhada é realizada utilizando bibliotecas como **Pandas**, **NumPy**, **Matplotlib** e **re**.
* **Gráficos e Insights**: São gerados gráficos e estatísticas diretamente no ambiente Python para identificar tendências, distribuições de preços e outras relações entre as variáveis.

---

## 🛠️ Tecnologias Utilizadas

* **Python**: Linguagem principal para todo o projeto.
* **Scrapy**: Framework para web scraping.
* **Pandas**: Manipulação e análise de dados.
* **NumPy**: Funções matemáticas e computação numérica.
* **Matplotlib**: Criação de gráficos e visualizações.
* **re**: Biblioteca para expressões regulares, usada na limpeza de dados.
* **MySQL**: Banco de dados relacional para armazenamento dos dados.
* **Power BI**: Ferramenta de Business Intelligence para visualização e dashboards.

---

## 👨‍💻 Autores

- [@IsmaelBrandao](https://github.com/IsmaelBrandao)  
- [@yarlenmagalhaes](https://github.com/yarlenmagalhaes)  
- [@Pedrobatista2024](https://github.com/Pedrobatista2024)

---

## 📄 Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT).
