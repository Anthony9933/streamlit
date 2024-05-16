import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


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
    df = pd.read_csv('dados.csv', encoding='latin-1', delimiter=';')
    st.header('Gráficos')
    st.dataframe(df)

    # Calcular o lucro provável
    df['LUCRO'] = df['P/VENDA'] - df['P/ CUSTO']
    
    # Gráfico de barras para comparar o estoque de cada item
    fig1 = px.bar(df, x='DESCRIÇÃO', y='ESTOQUE', title='Estoque de cada item')
    fig1.show()
    
    # Gráfico de dispersão para analisar o preço de venda versus o preço de custo
    fig2 = px.scatter(df, x='P/ CUSTO', y='P/VENDA', color='DESCRIÇÃO', title='Preço de venda vs Preço de custo')
    fig2.show()
    
    # Gráfico de barras para comparar o lucro provável de cada item
    fig3 = px.bar(df, x='DESCRIÇÃO', y='LUCRO', title='Lucro provável de cada item')
    fig3.show()


# Página de Visão Geral
if page == "Visão Geral":
    show_overview()

# Página de Filtros e Dados
elif page == "Filtros e Dados":
    show_filters_data()
    
# Página de Filtros de acidentes
#elif page == "Gráficos de Acidentes e Casualidades ao Longo do Tempo":
    #show_graphs()

#elif page == "Número de Acidentes por Hora do Dia":
    #show_accidents_by_hour()
