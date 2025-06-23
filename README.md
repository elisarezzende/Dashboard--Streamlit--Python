
# 📊 Dashboard de Análise de Dados

Este projeto consiste em um dashboard interativo desenvolvido em **Streamlit**, que permite a análise de dados de forma dinâmica e visual. A aplicação conta com filtros inteligentes, gráficos interativos e indicadores de desempenho, oferecendo uma visão clara e objetiva dos dados. Feito a partir de uma necessidade em testes, onde se faz necessário consolidar todas as informações de defeitos funcionais encontrados durantes ciclos de teste de regressão. Dessa forma, facilitando análises e tomadas de decisão.

---

## 🚀 Funcionalidades

- ✅ Upload de base de dados (.csv, .xlsx)
- 🔍 Filtros interativos por múltiplos critérios (com seleção múltipla)
- 📈 Gráficos dinâmicos (linha, barras, pizza, etc.)
- 🕓 Análise de **Aging Detalhado**
- 📅 Visualização de **Tendência Temporal**
- ✔️ Cálculo da **Taxa de Fechamento**
- 🗂️ Navegação intuitiva através de **abas** e **expanders**
- 🎯 Dashboard responsivo e de fácil utilização

---

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)
- [NumPy](https://numpy.org/)

---

## 📦 Instalação e Execução

1. Clone o repositório:

```bash
git clone https://https://github.com/elisarezzende/Dashboard--Streamlit--Python
```

2. Acesse a pasta do projeto:

```bash
cd Dashboard--Streamlit--Python
```

3. (Opcional) Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

4. Execute a aplicação:

```bash
streamlit run app.py
```

---

## 📂 Organização dos Arquivos

```
📦 nome-do-projeto
 ┣ 📜 app.py
 ┣ 📂 dados
 ┃ ┗ 📜 exemplo.xlsx
 ┗ 📜 README.md
```

---

## ✨ Melhorias Futuras

- Integração com bancos de dados
- Exportação de relatórios automáticos
- Implementação de autenticação de usuários
- Melhoria no design responsivo
- Cenários com maior número de defeitos
