import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# 🎯 Configuração da página
st.set_page_config(page_title="Defeitos Funcionais", layout="wide")
st.title("📊 Dashboard de Defeitos")


# -------------------------------
# 🚀 Função para carregamento de dados
@st.cache_data
def carregar_dados():
    try:
        df = pd.read_excel('dados/Defeitos abertos Maio e Junho 2025.xlsx')
        df['Status_normalizado'] = df['Status'].str.lower().str.strip()  # Normaliza status
        return df
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None


# -------------------------------
# 📥 Carregar dados
df = carregar_dados()

if df is not None:
    st.success("✅ Dados carregados com sucesso!")

    # -------------------------------
    # 🔍 Filtros Interativos
    st.subheader("🔍 Filtros Interativos")

    coluna_filtro = 'Detected in Cycle'

    if coluna_filtro in df.columns:
        valores_unicos = sorted(df[coluna_filtro].dropna().unique())
        selecionar_todos = st.checkbox("Selecionar todos", value=True)

        if selecionar_todos:
            valores_selecionados = st.multiselect(
                f"Selecione {coluna_filtro}",
                options=valores_unicos,
                default=valores_unicos
            )
        else:
            valores_selecionados = st.multiselect(
                f"Selecione {coluna_filtro}",
                options=valores_unicos
            )

    if not valores_selecionados:
        st.warning("⚠️ Selecione pelo menos um item para visualizar os dados")
        st.stop()

    df_filtrado = df[df[coluna_filtro].isin(valores_selecionados)]

    st.divider()

    # -------------------------------
    # 🗂️ Criar abas
    aba_status, aba_aging, aba_taxa, aba_dados = st.tabs(
        ["📋 Status", "⏳ Aging Detalhado", "🚦 Taxa de Fechamento", "🗂️ Dados"]
    )

    # -------------------------------
    # 📋 Aba Status
    with aba_status:
        st.subheader("🔍 Detalhes por Status")

        status_breakdown = df_filtrado['Status'].value_counts().sort_index()
        # 🔥 Controle de estado
        if 'clicked_status' not in st.session_state:
            st.session_state.clicked_status = None

        cols = st.columns(len(status_breakdown))

        for i, (status, count) in enumerate(status_breakdown.items()):
            with cols[i]:
                percentage = (count / len(df_filtrado)) * 100
                st.metric(status, f"{count} ({percentage:.1f}%)")
                if st.button(f"🔍 Ver {status}"):
                    st.session_state.clicked_status = status

        # 🔥 Mostrar a tabela filtrada
        if st.session_state.clicked_status:
            st.subheader(f"🗂️ Defeitos com status: {st.session_state.clicked_status}")
            df_status = df_filtrado[df_filtrado['Status'] == st.session_state.clicked_status]
            st.dataframe(df_status, use_container_width=True)

            # ❌ Botão para remover o filtro
            if st.button("❌ Remover filtro"):
                st.session_state.clicked_status = None

        st.divider()
        st.subheader("📋 Análise por Status")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total de defeitos registrados", len(df_filtrado))

        with col2:
            if 'Dias Defeito aberto' in df_filtrado.columns:
                try:
                    mediana_dias = df_filtrado['Dias Defeito aberto'].median()
                    st.metric("Média de aging de defeito", f"{mediana_dias:.1f} dias")
                except:
                    st.metric("Média de aging", "Erro no cálculo")

        status_breakdown = df_filtrado['Status'].value_counts().sort_index()

        # Gráfico de status
        fig = px.bar(
            x=status_breakdown.index,
            y=status_breakdown.values,
            labels={'x': 'Status', 'y': 'Quantidade'},
            title="Distribuição dos Defeitos por Status",
            color=status_breakdown.index
        )
        st.plotly_chart(fig, use_container_width=True)

    # -------------------------------
    # ⏳ Aba Aging Detalhado
    with aba_aging:
        st.subheader("⏳ Aging Detalhado")

        if 'Dias Defeito aberto' in df_filtrado.columns:
            df_aging = df_filtrado.copy()

            bins = [0, 7, 14, 30, 9999]
            labels = ['Até 7 dias', '8-14 dias', '15-30 dias', 'Mais de 30 dias']

            df_aging['Faixa Aging'] = pd.cut(
                df_aging['Dias Defeito aberto'], bins=bins, labels=labels
            )

            aging_counts = df_aging['Faixa Aging'].value_counts().sort_index()

            fig = px.bar(
                x=aging_counts.index,
                y=aging_counts.values,
                labels={'x': 'Faixa de Aging', 'y': 'Quantidade'},
                title="Distribuição de Aging dos Defeitos",
                color=aging_counts.index
            )
            st.plotly_chart(fig, use_container_width=True)

    # -------------------------------
    # 🚦 Aba Taxa de Fechamento
    with aba_taxa:
        st.subheader("🚦 Taxa de Fechamento")

        df_taxa = df_filtrado.copy()

        total_fechados = len(df_taxa[df_taxa['Status_normalizado'] == 'closed'])
        total_abertos = len(df_taxa[df_taxa['Status_normalizado'] != 'closed'])

        taxa = (
            (total_fechados / (total_abertos + total_fechados)) * 100
            if (total_abertos + total_fechados) > 0 else 0
        )

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Abertos", total_abertos)
        with col2:
            st.metric("Fechados", total_fechados)
        with col3:
            st.metric("Taxa de Fechamento", f"{taxa:.1f}%")

        fig = px.pie(
            names=['Abertos', 'Fechados'],
            values=[total_abertos, total_fechados],
            title="Distribuição Abertos vs Fechados"
        )
        st.plotly_chart(fig, use_container_width=True)

    # -------------------------------
    # 🗂️ Aba Dados
    with aba_dados:
        st.subheader("🗂️ Dados Filtrados")
        st.write(f"Mostrando {len(df_filtrado)} de {len(df)} registros")
        st.dataframe(df_filtrado, use_container_width=True)

    st.divider()