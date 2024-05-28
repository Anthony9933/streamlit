import streamlit as st
import pandas as pd 
import plotly.express as px
import numpy as np
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

    # Modificar os valores da quantidade de roupas vendidas
    data['Quantidade'] = np.random.randint(1, 43, size=len(data))
    
    # Salvar a base de dados modificada
    data.to_csv('dados_(8).csv', index=False)
    
    # Carregar a base de dados
    data = pd.read_csv('dados_(8).csv')

    # Exibir tabela de dados
    st.write(data)

    # Criar gráfico de evolução das vendas
    fig = px.line(data, x='Data', y='Quantidade', title='Evolução de Vendas')
    
    # Exibir gráfico
    st.plotly_chart(fig)
    

#####


# Página de Visão Geral
if page == "Visão Geral":
    show_overview()


elif page == "Filtros e Dados":
    show_filters_data()
    