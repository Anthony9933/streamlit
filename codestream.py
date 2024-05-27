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
   
    # Lista de arquivos CSV
    arquivos = ['BLAZER - Página1.csv', 'BERMUDA - Página1.csv', 'BLUSA - Página1.csv', 'CALÇA - Página1.csv', 'CAMISA - Página1.csv', 'CROPPED - Página1.csv', 'SAIA - Página1.csv', 'SHORT - Página1.csv', 'T-SHIRT - Página1.csv']
    
    # Lendo e concatenando os DataFrames de todos os arquivos CSV
    dfs = [pd.read_csv(arquivo, encoding='latin-1', delimiter=',') for arquivo in arquivos]
    df = pd.concat(dfs)
    
    st.header('Gráficos')
    st.dataframe(df)

###FASE DE TESTE PARA GRAFICOS###

   # Lista de arquivos CSV
    arquivos = ['dados (8).csv']
    
    # Lendo e concatenando os DataFrames de todos os arquivos CSV
    dfs = []
    for arquivo in arquivos:
        df_temp = pd.read_csv(arquivo, encoding='latin-1', delimiter=',')
        st.write(f"Colunas do arquivo {arquivo}: {df_temp.columns.tolist()}")
        dfs.append(df_temp)
    
    df = pd.concat(dfs)
    
    # Verifique se a coluna 'Data' está presente
    if 'Data' not in df.columns:
        st.error("A coluna 'Data' não foi encontrada nos arquivos CSV.")
        return
    
    # Convertendo a coluna de data para datetime, lidando com erros, e extraindo mês e ano
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y', errors='coerce')
    
    # Identificar e exibir valores inválidos na coluna 'Data'
    invalid_dates = df[df['Data'].isna()]
    if not invalid_dates.empty:
        st.warning("Foram encontrados valores inválidos na coluna 'Data'.")
        st.dataframe(invalid_dates)
    
    # Filtrando linhas com valores válidos na coluna 'Data'
    df = df.dropna(subset=['Data'])
    
    # Extraindo mês e ano
    df['MesAno'] = df['Data'].dt.to_period('M').dt.to_timestamp()
    
    # Verifique se a coluna 'Vendas' está presente
    if 'Vendas' not in df.columns:
        st.error("A coluna 'Vendas' não foi encontrada nos arquivos CSV.")
        return
    
    # Agrupando as vendas por mês e ano
    vendas_por_mes = df.groupby('MesAno')['Vendas'].sum().reset_index()
    
    # Ordenando os dados por data
    vendas_por_mes = vendas_por_mes.sort_values('MesAno')
    
    # Criando o gráfico de evolução de vendas ao longo do tempo
    fig = px.line(vendas_por_mes, x='MesAno', y='Vendas', title='Evolução de Vendas ao Longo do Tempo')
    
    # Exibindo o gráfico e os dados
    st.header('Gráficos')
    st.plotly_chart(fig)
    st.dataframe(df)

# Página de Visão Geral
if page == "Visão Geral":
    show_overview()


elif page == "Filtros e Dados":
    show_filters_data()
    