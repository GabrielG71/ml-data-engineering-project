## 📁 Estrutura do Projeto

```bash
ml-data-engineering-project/
│
├── 📂 driver/                         # Drivers necessários para conexões com bancos de dados ou APIs
│   ├── jdbc.jar                       # Exemplo: Driver JDBC para conexões com bancos relacionais
│
├── 📂 notebooks/                      # Notebooks Jupyter organizados por etapa da pipeline ETL
│   ├── 01-extract.ipynb               # Extração de dados (E)
│   ├── 02-transform.ipynb             # Limpeza e transformação dos dados (T)
│   ├── 03-load.ipynb                  # Carga dos dados em destino final (L)
│   ├── 04-quality-check.ipynb         # Validação e controle de qualidade dos dados
    ├── test.ipynb                     # Teste de Notebooks
│
├── 📂 input/                          # Diretório de dados de entrada
│   ├── 📂 csv/                        # Arquivos CSV brutos
│   │   ├── combustivel.csv
│   │   ├── vendas.csv
│   │   └── clientes.csv
│   ├── 📂 json/                       # Dados em formato JSON
│   │   └── dados_api.json
│   ├── 📂 api_responses/              # Respostas salvas de APIs externas (cache)
│
├── 📂 output/                         # Resultados processados e prontos para uso
│   ├── 📂 clean/                      # Dados limpos e transformados
│   │   ├── vendas_tratadas.csv
│   │   └── combustivel_tratado.csv
│   ├── 📂 reports/                    # Relatórios em CSV, Excel, ou PDF
│   │   ├── relatorio_vendas.xlsx
│   │   └── relatorio_estoque.pdf
│   ├── 📂 powerbi/                    # Dados prontos para consumo por ferramentas de BI
│   │   └── dataset_final.csv
│   └── 📂 archive/                    # Dados históricos ou backups
│
├── 📂 logs/                           # Logs de execução e debug
│   ├── etl_2025-10-21.log
│   └── error_2025-10-21.log
│
├── 📂 src/                          # Scripts e funções auxiliares reutilizáveis
│   ├── db_connection.py               # Funções de conexão com bancos de dados
│
├── 📂 tests/                          # Testes automatizados e validações unitárias
│   ├── teste.py
│
├── 📂 docs/                           # Documentação do projeto
│   ├── architecture.md                # Arquitetura da pipeline ETL
│   ├── sprints.md                     # Registro de sprints e tarefas (Scrum)
│
├── requirements.txt                   # Dependências do projeto (pandas, sqlalchemy, etc.)
├── environment.yaml                   # Configurações de ambiente
├── .gitignore                         # Ignorar arquivos sensíveis e temporários
└── README.md                          # Descrição geral do projeto
└── .env                               # Variaveis de Ambiente (Ocultada pelo .gitignore)
```
