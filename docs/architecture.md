# **Arquitetura do Pipeline (PySpark)**

## O projeto é feito com um pipeline construído utilizando **PySpark**, com o objetivo de consolidar, limpar e preparar o conjunto de dados de e-commerce brasileiro (Olist) para fins de análise e modelagem do Machine Learning.

## O processo é dividido em quatro fases principais: **Ingestão**, **Transformação (Joins)**, **Limpeza e Normalização**, e **Exportação**.

## **Ingestão e Inicialização do Ambiente**

### Esta fase estabelece o ambiente de processamento e carrega as fontes de dados brutas.

### - Tecnologia Principal: Apache Spark (via PySpark).

### - Inicialização: Uma SparkSession é criada (appName="leituracsv", master="local[*]") para gerenciar as operações distribuídas.

### - Ingestão de Dados: Múltiplas tabelas de dados brutos (em formato CSV) são lidas e carregadas em DataFrames do Spark, representando as diferentes entidades do e-commerce (customers, orders, order_items, products, order_payments, geolocation).

## **Transformação: Consolidação e Enriquecimento de Dados**

### O foco desta etapa é criar um DataFrame Base (df_base) unificado, consolidando as informações de diversas entidades.

## Pré-Processamento Geográfico

### O DataFrame geolocation é agregado (groupBy("geolocation_city", "geolocation_state")) para calcular as coordenadas geográficas médias (avg_lat, avg_lng). Isso cria o DataFrame geo_base, que será usado para enriquecer os dados dos clientes com uma coordenada de localização única por cidade/estado.

## Joins Sequenciais

### É realizada uma série de operações join para ligar as entidades em um único conjunto de fatos no nível de item de pedido (order_id + product_id).

## Seleção Final

### O df_base final é construído selecionando as colunas de interesse para a análise, incluindo chaves, status, timestamps, informações do cliente/produto/pagamento e as coordenadas geográficas enriquecidas.

## **Limpeza e Normalização de Dados**

### Esta fase foca em garantir a qualidade e a consistência do df_base.

## Tratamento de Duplicatas

### Duplicatas são removidas com base nas chaves primárias do fato: df_base = df_base.dropDuplicates(["order_id", "product_id"]).

## Tratamento de Missing Values

### O tratamento é aplicado em duas abordagens:

### - Remoção de Linhas (Drop): Linhas com valores nulos em colunas consideradas essenciais para a análise (product_id, price, payment_value, latitude_media, longitude_media) são removidas via .dropNa().

### - Preenchimento de Linhas (Fill): Valores nulos em colunas opcionais são preenchidos (imputação):product_category_name $\rightarrow$ "desconhecido"freight_value $\rightarrow$ 0

## **Padronização e Conversão de Tipos**

### A consistência dos dados é assegurada com operações de normalização:

### - Strings: order_status e product_category_name são convertidas para minúsculas e têm espaços em branco removidos (trim). customer_state é convertida para maiúsculas.

### - Tipos de Dados: Colunas monetárias (price, freight_value, payment_value) são explicitamente convertidas para o tipo Double para garantir cálculos precisos.

### - Data: A coluna de timestamp (order_purchase_timestamp) é convertida para uma coluna de apenas data (order_date) usando a função to_date().

## **Exportação e Validação**

### A etapa final garante que o conjunto de dados limpo e processado esteja pronto para consumo.

### - Validação: Estatísticas descritivas (.describe()) e contagens por grupo (order_status, customer_state) são executadas para validar a distribuição dos dados após a limpeza.

### - Exportação: O df_base final é exportado para o disco em dois formatos otimizados, garantindo a persistência e o acesso eficiente para aplicações downstream:

### - Parquet: Exportação principal (.parquet()) que preserva o esquema e é ideal para ambientes Spark/Data Lake.

### - CSV: Exportação secundária (.csv(coalesce(1))) para facilitar a visualização e o uso em ferramentas que exigem este formato.

## **Conclusão final**

### A arquitetur
