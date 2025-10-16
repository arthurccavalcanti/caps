import streamlit as st
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# Page configuration (should be first Streamlit command)
st.set_page_config(
    page_title="Empresas do Recife",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2E86AB;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
        padding: 1rem;
        background: linear-gradient(135deg, #2E86AB, #A23B72);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.5rem;
        color: #F18F01;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 600;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2E86AB;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
        height: 140px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .metric-card h3 {
        color: #2E86AB;
        margin: 0 0 10px 0;
        font-size: 1rem;
        line-height: 1.2;
    }
    .metric-card h1 {
        color: #2E86AB;
        margin: 0;
        font-size: 2.5rem;
        line-height: 1;
    }
    .metric-card p {
        margin: 5px 0 0 0;
        font-weight: bold;
        line-height: 1.2;
    }
    .chart-container {
        background-color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .tab-content {
        padding: 1rem 0;
    }
    /* Customize Streamlit tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 5px 5px 0 0;
        gap: 1rem;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #2E86AB;
        color: white;
    }
    .data-table {
        background-color: white;
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-header">🏢 Empresas do Recife</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="sub-header">Painel de Análise de Dados Empresariais</h2>', unsafe_allow_html=True)

# Load data function
@st.cache_data
def load_data():
    current_dir = Path().cwd()

    data_file_ativo = current_dir / 'data' / 'empresasativender_tratado.csv'
    data_file_inativo = current_dir / 'data' / 'empresasinativender_tratado.csv'

    df_ativo = pd.read_csv(data_file_ativo, delimiter=";")
    df_inativo = pd.read_csv(data_file_inativo, delimiter=";")

    return df_ativo, df_inativo

# Load data
df_ativo, df_inativo = load_data()

# Calculate metrics
ativos_count = df_ativo["cnpj"].nunique()
inativos_count = df_inativo["cnpj"].nunique()
total_empresas = ativos_count + inativos_count
percentual_ativos = (ativos_count / total_empresas) * 100

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Visão Geral",
    "🏢 Empresas Ativas",
    "📈 Empresas Inativas",
    "🔍 Análises Detalhadas"
])

with tab1:
    st.markdown('<div class="tab-content">', unsafe_allow_html=True)

    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Total de Empresas</h3>
            <h1>{total_empresas:,}</h1>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Empresas Ativas</h3>
            <h1>{ativos_count:,}</h1>
            <p style="color: #28a745;">({percentual_ativos:.1f}%)</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Empresas Inativas</h3>
            <h1>{inativos_count:,}</h1>
            <p style="color: #dc3545;">({100 - percentual_ativos:.1f}%)</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        taxa_ativacao = (ativos_count / total_empresas) * 100
        st.markdown(f"""
        <div class="metric-card">
            <h3>Taxa de Ativação</h3>
            <h1>{taxa_ativacao:.1f}%</h1>
        </div>
        """, unsafe_allow_html=True)

    # Charts Row
    col_chart1, col_chart2 = st.columns([2, 1])

    with col_chart1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)

        # Enhanced Pie Chart
        sizes = [ativos_count, inativos_count]
        labels = ['Ativas', 'Inativas']
        colors = ['#28a745', '#dc3545']
        explode = (0.05, 0)

        fig, ax = plt.subplots(figsize=(10, 6))
        wedges, texts, autotexts = ax.pie(sizes,
                                        colors=colors,
                                        labels=labels,
                                        autopct='%1.1f%%',
                                        startangle=90,
                                        explode=explode,
                                        shadow=True)

        plt.setp(autotexts, size=12, weight="bold", color='white')
        plt.setp(texts, size=12)
        ax.set_title('Distribuição de Empresas por Status', fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()

        st.pyplot(fig)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_chart2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("📈 Tendência")
        st.metric(
            label="Status do Ecossistema",
            value="Em Análise",
            delta="Coleta de dados"
        )
        st.info("Mais análises serão adicionadas em futuras atualizações.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="tab-content">', unsafe_allow_html=True)
    st.header("🏢 Empresas Ativas")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown('<div class="data-table">', unsafe_allow_html=True)
        st.subheader("Dados das Empresas Ativas")

        # Display sample data or basic info
        if len(df_ativo) > 0:
            st.dataframe(df_ativo.head(10), use_container_width=True)
            st.caption(f"Mostrando 10 de {len(df_ativo)} registros de empresas ativas")
        else:
            st.warning("Nenhum dado disponível para empresas ativas")

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("Estatísticas")

        # Additional metrics in fixed height cards
        col2_1, col2_2 = st.columns(2)

        with col2_1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Total de Registros</h3>
                <h1>{len(df_ativo):,}</h1>
            </div>
            """, unsafe_allow_html=True)

        with col2_2:
            numeric_columns = df_ativo.select_dtypes(include=['number']).columns
            st.markdown(f"""
            <div class="metric-card">
                <h3>Colunas Numéricas</h3>
                <h1>{len(numeric_columns)}</h1>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="metric-card">
            <h3>Total de Colunas</h3>
            <h1>{len(df_ativo.columns)}</h1>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="tab-content">', unsafe_allow_html=True)
    st.header("📈 Empresas Inativas")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown('<div class="data-table">', unsafe_allow_html=True)
        st.subheader("Dados das Empresas Inativas")

        if len(df_inativo) > 0:
            st.dataframe(df_inativo.head(10), use_container_width=True)
            st.caption(f"Mostrando 10 de {len(df_inativo)} registros de empresas inativas")
        else:
            st.warning("Nenhum dado disponível para empresas inativas")

        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("Estatísticas")

        # Additional metrics in fixed height cards
        col2_1, col2_2 = st.columns(2)

        with col2_1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Total de Registros</h3>
                <h1>{len(df_inativo):,}</h1>
            </div>
            """, unsafe_allow_html=True)

        with col2_2:
            numeric_columns = df_inativo.select_dtypes(include=['number']).columns
            st.markdown(f"""
            <div class="metric-card">
                <h3>Colunas Numéricas</h3>
                <h1>{len(numeric_columns)}</h1>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="metric-card">
            <h3>Total de Colunas</h3>
            <h1>{len(df_inativo.columns)}</h1>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="tab-content">', unsafe_allow_html=True)
    st.header("🔍 Análises Detalhadas")

    st.info("""
    🚧 **Seção em Desenvolvimento**

    Esta área será expandida com:
    - Análises temporais
    - Comparativos por setor
    - Mapas de localização
    - Indicadores econômicos
    - Relatórios personalizados
    """)

    # Placeholder for future content with consistent metric cards
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("Análise Temporal")

        # Placeholder metrics
        col1_1, col1_2 = st.columns(2)

        with col1_1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Período Analisado</h3>
                <h1>--</h1>
            </div>
            """, unsafe_allow_html=True)

        with col1_2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Variação</h3>
                <h1>--</h1>
            </div>
            """, unsafe_allow_html=True)

        st.write("Gráficos de evolução ao longo do tempo serão exibidos aqui.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader("Análise Setorial")

        # Placeholder metrics
        col2_1, col2_2 = st.columns(2)

        with col2_1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Setores</h3>
                <h1>--</h1>
            </div>
            """, unsafe_allow_html=True)

        with col2_2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>Principal Setor</h3>
                <h1>--</h1>
            </div>
            """, unsafe_allow_html=True)

        st.write("Distribuição por setores econômicos será mostrada aqui.")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p>Painel Empresas do Recife • Desenvolvido para análise de dados empresariais</p>
    <p>Atualizado em Outubro 2025</p>
</div>
""", unsafe_allow_html=True)
