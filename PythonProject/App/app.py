import streamlit as st
import pandas as pd

st.set_page_config(page_title="Defeitos Funcionais (Mai-Jun)", layout="wide")
st.title("Dashboard")


# função para carregamento de dados
@st.cache_data
def carregar_dados():
    try:
        df = pd.read_excel('dados/Defeitos abertos Maio e Junho 2025.xlsx')
        return df
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None


# carregar dados
df = carregar_dados()

if df is not None:
    st.success("✅ Dados carregados com sucesso!")

    # Seção de filtros - ocupando toda a largura
    st.subheader("🔍 Filtros Interativos")

    # Container para os filtros
    with st.container():
        # Criar colunas para os filtros
        col1, col2 = st.columns([1, 1])

        with col1:
            coluna_filtro = 'Detected in Cycle'

            if coluna_filtro in df.columns:
                st.write(f"**Filtrar por {coluna_filtro}:**")

                # Obter valores únicos da coluna
                valores_unicos = sorted(df[coluna_filtro].unique())

                # Inicializar session state se não existir
                if 'checkboxes' not in st.session_state:
                    st.session_state.checkboxes = {valor: True for valor in valores_unicos}

                # Checkbox para selecionar todos
                todos_selecionados = all(st.session_state.checkboxes.values())

                selecionar_todos = st.checkbox("Selecionar Todos", value=todos_selecionados)

                # Se o usuário mudou o "Selecionar Todos"
                if selecionar_todos != todos_selecionados:
                    for valor in valores_unicos:
                        st.session_state.checkboxes[valor] = selecionar_todos

                # Criar checkboxes individuais
                valores_selecionados = []

                for valor in valores_unicos:
                    checkbox_atual = st.checkbox(
                        f"{valor}",
                        value=st.session_state.checkboxes.get(valor, True),
                        key=f"check_{valor}"
                    )

                    # Atualizar o estado
                    st.session_state.checkboxes[valor] = checkbox_atual

                    if checkbox_atual:
                        valores_selecionados.append(valor)

        with col2:
            st.write("**Itens selecionados:**")
            if valores_selecionados:
                for item in valores_selecionados:
                    st.write(f"✅ {item}")
            else:
                st.write("Nenhum item selecionado")

    # Separador visual
    st.divider()

    # Filtrar dados baseado na seleção
    if valores_selecionados:
        df_filtrado = df[df[coluna_filtro].isin(valores_selecionados)]

        # Mostrar dados filtrados - ocupando toda a largura
        st.subheader("📊 Dados Filtrados")
        st.write(f"Mostrando {len(df_filtrado)} de {len(df)} registros")

        # Tabela ocupando toda a largura
        st.dataframe(df_filtrado, use_container_width=True)

        # Separador visual
        st.divider()

        # Estatísticas personalizadas - ocupando toda a largura
        st.subheader("📈 Estatísticas dos Defeitos")

        # Container para estatísticas
        with st.container():
            # Primeira linha de métricas
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Total de Registros", len(df_filtrado))

            with col2:
                # Contagem por Status
                if 'Status' in df_filtrado.columns:
                    status_counts = df_filtrado['Status'].value_counts()
                    st.metric("Status Mais Comum",
                              f"{status_counts.index[0]} ({status_counts.iloc[0]})")

            with col3:
                # Mediana de dias em aberto (valor central)
                if 'Dias Defeito aberto' in df_filtrado.columns:
                    try:
                        mediana_dias = df_filtrado['Dias Defeito aberto'].median()
                        st.metric("Mediana Dias Aberto", f"{mediana_dias:.1f} dias")
                    except:
                        st.metric("Mediana Dias Aberto", "Erro no cálculo")

            # Segunda linha de métricas - Datas reais
            st.write("")  # Espaço entre as linhas
            col1, col2 = st.columns(2)

            with col1:
                # Primeira e última data de abertura
                if 'Opening Date' in df_filtrado.columns:
                    try:
                        df_temp = df_filtrado.copy()
                        df_temp['Opening Date'] = pd.to_datetime(df_temp['Opening Date'], errors='coerce')
                        datas_abertura = df_temp['Opening Date'].dropna()

                        if len(datas_abertura) > 0:
                            primeira_abertura = datas_abertura.min()
                            ultima_abertura = datas_abertura.max()

                            st.metric("Primeira Abertura", primeira_abertura.strftime('%d/%m/%Y'))
                            st.metric("Última Abertura", ultima_abertura.strftime('%d/%m/%Y'))
                        else:
                            st.metric("Primeira Abertura", "-")
                            st.metric("Última Abertura", "-")
                    except:
                        st.metric("Primeira Abertura", "Erro")
                        st.metric("Última Abertura", "Erro")
                else:
                    st.metric("Primeira Abertura", "Coluna não encontrada")
                    st.metric("Última Abertura", "Coluna não encontrada")

            with col2:
                # Primeira e última data de fechamento
                if 'Closing Date' in df_filtrado.columns:
                    try:
                        df_temp = df_filtrado.copy()
                        df_temp['Closing Date'] = pd.to_datetime(df_temp['Closing Date'], errors='coerce')
                        datas_fechamento = df_temp['Closing Date'].dropna()

                        if len(datas_fechamento) > 0:
                            primeiro_fechamento = datas_fechamento.min()
                            ultimo_fechamento = datas_fechamento.max()

                            st.metric("Primeiro Fechamento", primeiro_fechamento.strftime('%d/%m/%Y'))
                            st.metric("Último Fechamento", ultimo_fechamento.strftime('%d/%m/%Y'))
                        else:
                            st.metric("Primeiro Fechamento", "-")
                            st.metric("Último Fechamento", "-")
                    except:
                        st.metric("Primeiro Fechamento", "Erro")
                        st.metric("Último Fechamento", "Erro")
                else:
                    st.metric("Primeiro Fechamento", "Coluna não encontrada")
                    st.metric("Último Fechamento", "Coluna não encontrada")

            # Breakdown por Status - ocupando toda a largura
            if 'Status' in df_filtrado.columns:
                st.write("")  # Espaço
                st.subheader("📋 Análise detalhada por Status")
                status_breakdown = df_filtrado['Status'].value_counts()

                # Criar colunas dinâmicas para mostrar cada status
                if len(status_breakdown) > 0:
                    cols = st.columns(len(status_breakdown))
                    for i, (status, count) in enumerate(status_breakdown.items()):
                        with cols[i]:
                            percentage = (count / len(df_filtrado)) * 100
                            st.metric(status, f"{count} ({percentage:.1f}%)")

    else:
        st.warning("⚠️ Selecione pelo menos um item para visualizar os dados")

else:
    st.error("❌ Não foi possível carregar os dados")
