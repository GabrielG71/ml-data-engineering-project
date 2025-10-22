## 📁 Estrutura do Projeto

```bash
ml-data-engineering-project/
│
├── 📂 driver/                         # Drivers necessários para conexões com bancos de dados ou APIs
│   ├── jdbc.jar                       # Exemplo: Driver JDBC para conexões com bancos relacionais
│   └── README.md                      # Descrição dos drivers utilizados e instruções de instalação
│
├── 📂 notebooks/                      # Notebooks Jupyter organizados por etapa da pipeline ETL
│   ├── 01-extract.ipynb               # Extração de dados (E)
│   ├── 02-transform.ipynb             # Limpeza e transformação dos dados (T)
│   ├── 03-load.ipynb                  # Carga dos dados em destino final (L)
│   ├── 04-quality-check.ipynb         # Validação e controle de qualidade dos dados
│
├── 📂 input/                          # Diretório de dados de entrada
│   ├── 📂 csv/                        # Arquivos CSV brutos
│   │   ├── combustivel.csv
│   │   ├── vendas.csv
│   │   └── clientes.csv
│   ├── 📂 json/                       # Dados em formato JSON
│   │   └── dados_api.json
│   ├── 📂 api_responses/              # Respostas salvas de APIs externas (cache)
│   └── README.md                      # Descrição das origens e formatos dos dados
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
├── 📂 utils/                          # Scripts e funções auxiliares reutilizáveis
│   ├── db_connection.py               # Funções de conexão com bancos de dados
│   ├── data_cleaning.py               # Funções genéricas de limpeza e padronização
│   ├── api_utils.py                   # Scripts para chamadas e tratamento de APIs
│   ├── file_utils.py                  # Manipulação de arquivos (zip, csv, etc.)
│   └── README.md                      # Descrição das utilidades e exemplos de uso
│
├── 📂 tests/                          # Testes automatizados e validações unitárias
│   ├── test_data_cleaning.py
│   ├── test_db_connection.py
│   └── README.md
│
├── 📂 docs/                           # Documentação do projeto
│   ├── architecture.md                # Arquitetura da pipeline ETL
│   ├── data-dictionary.md             # Dicionário de dados
│   ├── sprints.md                     # Registro de sprints e tarefas (Scrum)
│   └── team-notes.md                  # Notas e decisões de equipe
│
├── requirements.txt                   # Dependências do projeto (pandas, sqlalchemy, etc.)
├── config.yaml                        # Configurações globais (caminhos, credenciais, etc.)
├── .gitignore                         # Ignorar arquivos sensíveis e temporários
└── README.md                          # Descrição geral do projeto
