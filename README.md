# dashboard-defeitos-funcionais
Esse é um dashboard realizado em Python com a biblioteca Pandas e Streamlit. O projeto foi pensado para visualizar um relatório de defeitos funcionais abertos no ALM no projeto Vale

Sobre o Projeto:
Este dashboard foi desenvolvido para analisar e visualizar dados de defeitos funcionais, proporcionando uma interface interativa e intuitiva para acompanhar métricas importantes do projeto.

Funcionalidades:
Filtros Interativos: Filtrar dados por "Detected in Cycle" com checkboxes selecionáveis
Visualização de Dados: Tabela responsiva mostrando todos os defeitos filtrados
Estatísticas Automáticas:
Total de registros
Status mais comum
Mediana de dias em aberto
Primeira e última data de abertura
Primeira e última data de fechamento
Breakdown por Status: Distribuição percentual dos defeitos por status

Tecnologias Utilizadas:
Python 3.13
Streamlit - Interface web interativa
Pandas - Manipulação e análise de dados
OpenPyXL - Leitura de arquivos Excel

Pré-requisitos:
Python 3.7 ou superior
Bibliotecas listadas em requirements.txt

Como Executar:
Clone este repositório:
  git clone https://github.com/seu-usuario/dashboard-defeitos-funcionais.git
  cd dashboard-defeitos-funcionais

Instale as dependências:
  pip install -r requirements.txt

Execute o dashboard:
  streamlit run app.py

📁 Estrutura do Projeto
dashboard-defeitos-funcionais/

├── app.py # Aplicação principal

├── requirements.txt # Dependências do projeto

├── dados/ # Pasta com dados

│ └── Defeitos abertos Maio e Junho 2025.xlsx

└── README.md # Este arquivo

Métricas Disponíveis
Total de Registros: Quantidade total de defeitos filtrados
Status Mais Comum: Status que aparece com maior frequência
Mediana Dias Aberto: Valor central de dias que os defeitos ficam em aberto
Datas de Abertura: Primeira e última data de abertura dos defeitos
Datas de Fechamento: Primeira e última data de fechamento dos defeitos
Breakdown por Status: Distribuição percentual detalhada por status

Como Usar
Selecione os filtros: Use os checkboxes para escolher quais ciclos visualizar
Analise os dados: Visualize a tabela filtrada com todos os defeitos
Acompanhe as métricas: Observe as estatísticas calculadas automaticamente
Compare status: Analise a distribuição percentual na seção breakdown

Fonte dos Dados
Os dados utilizados são provenientes do ALM (Application Lifecycle Management) do projeto Vale, contendo informações sobre defeitos funcionais identificados durante os meses de maio e junho de 2025.


Resultado
![image](https://github.com/user-attachments/assets/6f9951ce-5ff1-4536-9ee9-769a3c68c774)
