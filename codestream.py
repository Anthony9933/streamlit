import streamlit as st
import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plt

# Sidebar (Menu Lateral)
page = st.sidebar.selectbox("Escolha a Página", ["Visão Geral", "Filtros e Dados"])
def show_overview():
    
    # Visão Geral do Projeto
    st.header("Visão Geral do Projeto")
    st.write("Bem-vindo ao projeto de Visualização de dados da loja Moda Antiga! Este projeto gira em torno da análise e apresentação "
             "de dados do estoque e de vendas de produtos da loja Moda Antiga. O conjunto de dados contém várias colunas fornecendo insights "
             "sobre os produtos e informações relativas a vendas, incluindo data, produtos mais vendidos, melhores e piores meses de venda.")
    
    # Como Funciona
    st.header("Como Funciona")
    st.write("O projeto utiliza um conjunto de dados com informações sobre as vendas e o estoque da loja. Aqui está uma breve visão "
             "geral dos principais componentes:")
    
    # Objetivo do Projeto
    st.header("Objetivo do Projeto")
    st.write("O principal objetivo deste projeto é obter insights pela análise dos dados e gráficos criados. Isso inclui entender "
             "o que os dados estão nos dizendo, identificar e explorar padrões dos compradores "
             "prevendo e criando estratégias para aumentar as vendas.")
    
    # Como Utilizar
    st.header("Como Utilizar")
    st.write("Para explorar o projeto, você pode navegar por diferentes seções usando a barra lateral. As principais seções incluem:")
      
    st.header("Conclusão")
    st.write("Sinta-se à vontade para analisar o conjunto de dados, obter insights e tirar conclusões significativas a partir "
               "dos dados apresentados. Para análises específicas ou dúvidas, novos recursos podem ser incorporados com base nos "
               "objetivos do seu projeto.")
  
    st.write("Aproveite a exploração do projeto!")

def show_filters_data():
    st.header("Filtros e Dados")
    st.warning("⚠️ ESTAMOS EM FASE DE TESTES! ASS: DESENVOLVEDORES ⚠️")
    # Lista de arquivos CSV
    arquivos = ['BLAZER - Página1.csv', 'BERMUDA - Página1.csv', 'BLUSA - Página1.csv', 'CALÇA - Página1.csv', 'CAMISA - Página1.csv', 'CROPPED - Página1.csv', 'SAIA - Página1.csv', 'SHORT - Página1.csv', 'T-SHIRT - Página1.csv']
    
    # Lendo e concatenando os DataFrames de todos os arquivos CSV
    dfs = [pd.read_csv(arquivo, encoding='latin-1', delimiter=',') for arquivo in arquivos]
    df = pd.concat(dfs)
    
    st.header('Gráficos')
    st.dataframe(df)
    st.divider()
    ###FASE DE TESTE PARA GRAFICOS###
    # Título do aplicativo
    st.title('Evolução de Vendas ao Longo do Tempo')

    # Carregar dados
    data = pd.read_csv('dados (8).csv')

    # Exibir tabela de dados
    st.write(data)

    # Criar gráfico de evolução das vendas
    fig = px.line(data, x='Data', y='Quantidade', title='Evolução de Vendas')
    
    # Exibir gráfico
    st.plotly_chart(fig)
    

#####
def gerar_vendas_variadas(base, incremento_inicial, incremento_final, variacao):
    base['Data'] = pd.to_datetime(base['Data'])
    base = base.sort_values(by='Data')
    base = base.reset_index(drop=True)

    quantidade_inicial = base.loc[0, 'Quantidade']
    meses = len(base)

    np.random.seed(42)  # Para reprodutibilidade

    incremento = np.linspace(incremento_inicial, incremento_final, meses)
    variacao_aleatoria = np.random.normal(loc=0, scale=variacao, size=meses)

    vendas_ajustadas = quantidade_inicial + incremento + variacao_aleatoria
    vendas_ajustadas[vendas_ajustadas < 0] = 0  # Garantir que não haja vendas negativas

    base['Quantidade'] = vendas_ajustadas.round().astype(int)
    return base

# Aplicar a função na base de dados
df_ajustada = gerar_vendas_variadas(df, incremento_inicial=10, incremento_final=200, variacao=30)

# Verificar o resultado
print(df_ajustada.head())

# Página de Visão Geral
if page == "Visão Geral":
    show_overview()


elif page == "Filtros e Dados":
    show_filters_data()
    